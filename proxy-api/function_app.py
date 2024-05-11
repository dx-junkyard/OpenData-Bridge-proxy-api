import azure.functions as func
import logging
import json
from dataclasses import asdict

app = func.FunctionApp()

@app.route(route="health-check", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a health-check request.')
    return func.HttpResponse("ok", status_code=200)

from src.main.Swagger import SwaggerService
@app.route(route="swagger", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def swagger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("access")
    html_content = SwaggerService().getUi()
    return func.HttpResponse(
        html_content,
        status_code=200,
        headers={"Content-Type": "text/html"}
    )

@app.route(route="swagger/json", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def swaggerJson(req: func.HttpRequest) -> func.HttpResponse:
    swaggerJson = SwaggerService().getJson()
    return func.HttpResponse(
        json.dumps(swaggerJson),
        status_code=200,
        headers={"Content-Type": "application/json"}
    )

    
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
    
from src.main.ExtractLinks import ExtractLinkService
@app.route(route="extract-links", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def extractLinks(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get('url')

    try:
        ret = ExtractLinkService().get(url)

        return func.HttpResponse(
            json.dumps(asdict(ret)),
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        return func.HttpResponse(
            "Please pass an address in the query string.",
            status_code=200
        )
