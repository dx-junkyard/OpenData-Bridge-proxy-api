import azure.functions as func
import os
import logging
import json
from dataclasses import asdict

# from src.utils import get_config
# # デプロイ先で環境変数が設定されないと起動しない
# config = get_config(os.environ['ConfigFileName'])
# KEY_VAULT_URL = config['key-vault']['url']

app = func.FunctionApp()

@app.route(route="health-check", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a health-check request.')
    return func.HttpResponse("ok", status_code=200)

# from src.Swagger import SwaggerService
# @app.route(route="swagger", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def swagger(req: func.HttpRequest) -> func.HttpResponse:
#     # with open(os.path.join(os.path.dirname(__file__), 'swagger', 'html2-client-generated', 'index.html'), 'r', encoding='utf-8') as html_file:
#     #     html_content = html_file.read()
#     html_content = SwaggerService().getUi()
#     return func.HttpResponse(
#         html_content,
#         status_code=200,
#         headers={"Content-Type": "text/html"}
#     )

# @app.route(route="swagger/json", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def swaggerJson(req: func.HttpRequest) -> func.HttpResponse:
#     # with open(os.path.join(os.path.dirname(__file__), 'swagger', 'openapi.json'), 'r', encoding='utf-8') as fp:
#     #     print(fp)

#     #     swaggerJson = json.load(fp)
#     swaggerJson = SwaggerService().getJson()
#     # Convert the JSON object back to a string to send as a response
#     return func.HttpResponse(
#         json.dumps(swaggerJson),
#         status_code=200,
#         headers={"Content-Type": "application/json"}
#     )

    
from src.main.DigitalGoGeocode import DigitalGoGeocodeService
@app.route(route="digital-go-geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def digital_go_geocode(req: func.HttpRequest) -> func.HttpResponse:

    digitalGoGeocodeService = DigitalGoGeocodeService()

    address = req.params.get('address')

    if address:
        geocode_result = digitalGoGeocodeService.get(address)
        return func.HttpResponse(
            json.dumps(asdict(geocode_result)),
            headers={"Content-Type": "application/json"},
            status_code=200
        )
    else:
        return func.HttpResponse(
             "Please pass an address in the query string.",
             status_code=400
        )

from src.main.TranslateJpToEn import TranslateJpToEnService
@app.route(route="japanese-to-english", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def japanese_to_english(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for jp2en executed.')
    translateService = TranslateJpToEnService()

    jp = req.params.get('jp')

    if jp:
        ret = translateService.get(jp)

        return func.HttpResponse(
            json.dumps(asdict(ret)),
            headers={"Content-Type": "application/json"},
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please pass an address in the query string.",
            status_code=400
        )
    
# from src.ExtractLinks import ExtractLinkService
# @app.route(route="extract-links", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def extractLinks(req: func.HttpRequest) -> func.HttpResponse:
#     url = req.params.get('url')

#     try:
#         ret = ExtractLinkService().get(url)

#         return func.HttpResponse(
#             json.dumps(asdict(ret)),
#             headers={"Content-Type": "application/json"}
#         )
#     except Exception as e:
#         return func.HttpResponse(
#             "Please pass an address in the query string.",
#             status_code=200
#         )


# from src.service.geocodeService import GeocodeRepository

# @app.route(route="geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def geocode(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function for geocoding executed.')

#     geocodeService = GeocodeRepository()

#     city_block_id = int(req.params.get('city_block_id'))
#     residence_id = int(req.params.get('residence_id'))
#     address = req.params.get('address')

#     if address:
#         geocode_result = geocodeService.get(city_block_id, residence_id, address)
#         return func.HttpResponse(
#             json.dumps(asdict(geocode_result)),
#             headers={"Content-Type": "application/json"}
#         )
#     else:
#         return func.HttpResponse(
#              "Please pass an address in the query string.",
#              status_code=200
# #         )

# from src.service.digitalGoGeocodeService import DigitalGoGeocodeService

# @app.route(route="digital-go-geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def digital_go_geocode(req: func.HttpRequest) -> func.HttpResponse:

#     digitalGoGeocodeService = DigitalGoGeocodeService(KEY_VAULT_URL, config['digital-go-geocode'])

#     address = req.params.get('address')

#     if address:
#         geocode_result = digitalGoGeocodeService.get(address)
#         return func.HttpResponse(
#             json.dumps(asdict(geocode_result)),
#             headers={"Content-Type": "application/json"}
#         )
#     else:
#         return func.HttpResponse(
#              "Please pass an address in the query string.",
#              status_code=200
#         )

# from src.service.translateService import TranslateService

# @app.route(route="japanese-to-english", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def japanese_to_english(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function for jp2en executed.')
#     translateService = TranslateService(KEY_VAULT_URL, config['azure-translator'])

#     jp_str = req.params.get('jp')

#     if jp_str:
#         en = translateService.jp2en(jp_str)

#         return func.HttpResponse(
#             json.dumps(asdict(en)),
#             headers={"Content-Type": "application/json"}
#         )
#     else:
#         return func.HttpResponse(
#             "Please pass an address in the query string.",
#             status_code=200
#         )
    
# from src.service.extractLinksservice import ExtractLinkService
# @app.route(route="extract-links", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# def extractLinks(req: func.HttpRequest) -> func.HttpResponse:
#     url = req.params.get('url')

#     try:
#         ret = ExtractLinkService().get(url)

#         return func.HttpResponse(
#             json.dumps(ret),
#             headers={"Content-Type": "application/json"}
#         )
#     except Exception as e:
#         return func.HttpResponse(
#             "Please pass an address in the query string.",
#             status_code=200
#         )

# # from src.service.idService import IDService

# # @app.route(route="id", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# # def Id(req: func.HttpRequest) -> func.HttpResponse:
# #     logging.info('Python HTTP trigger function for jp2en executed.')
# #     idService = IDService(KEY_VAULT_URL, config['id'])

# #     header = req.params.get('header', '')
# #     ret = idService.get(header)

# #     return func.HttpResponse(
# #         json.dumps(asdict(ret)),
# #         headers={"Content-Type": "application/json"}
# #     )

# # @app.route(route="id-reset", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# # def resetId(req: func.HttpRequest) -> func.HttpResponse:
# #     logging.info('Python HTTP trigger function for jp2en executed.')

# #     IDService(KEY_VAULT_URL, config['id']).reset()

# #     return func.HttpResponse("Success", status_code=200)

# # from src.service.poiService import POIService

# # @app.route(route="poi", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# # def poi(req: func.HttpRequest) -> func.HttpResponse:
# #     logging.info('Python HTTP trigger function for jp2en executed.')
# #     poiService = POIService()

# #     word = req.params.get('word')

# #     if word:
# #         poiData = poiService.get(word)
        
# #         return func.HttpResponse(
# #             json.dumps(asdict(poiData)),
# #             headers={"Content-Type": "application/json"}
# #         )
# #     else:
# #         return func.HttpResponse(
# #             "Please pass an word in the query string.",
# #             status_code=200
# #         )

# # @app.route(route="main", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
# # def main(req: func.HttpRequest) -> func.HttpResponse:
# #     swagger_json = {
# #         "openapi": "3.0.0",
# #         "info": {
# #             "title": "Sample API",
# #             "version": "1.0.0"
# #         },
# #         "paths": {
# #             "/api/Example": {
# #                 "get": {
# #                     "summary": "Example GET method",
# #                     "responses": {
# #                         "200": {
# #                             "description": "A list of something",
# #                             "content": {
# #                                 "application/json": {
# #                                     "schema": {
# #                                         "type": "array",
# #                                         "items": {"type": "string"}
# #                                     }
# #                                 }
# #                             }
# #                         }
# #                     }
# #                 }
# #             }
# #         }
# #     }
# #     return func.HttpResponse(json.dumps(swagger_json), mimetype="application/json")