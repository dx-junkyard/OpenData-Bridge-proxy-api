import azure.functions as func
import os
import logging
import json
from dataclasses import asdict

from src.utils import get_config
config = get_config(os.environ['ConfigFileName'])
KEY_VAULT_URL = config['key-vault']['url']

app = func.FunctionApp()

@app.route(route="hello", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a hello request.')
    return func.HttpResponse("Hello World from /hello", status_code=200)

from src.service.geocodeService import GeocodeRepository

@app.route(route="geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def geocode(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for geocoding executed.')

    geocodeService = GeocodeRepository()

    city_block_id = int(req.params.get('city_block_id'))
    residence_id = int(req.params.get('residence_id'))
    address = req.params.get('address')

    if address:
        geocode_result = geocodeService.get(city_block_id, residence_id, address)
        return func.HttpResponse(
            json.dumps(asdict(geocode_result)),
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
             "Please pass an address in the query string.",
             status_code=200
        )

from src.service.digitalGoGeocodeService import DigitalGoGeocodeService

@app.route(route="digital-go-geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def digital_go_geocode(req: func.HttpRequest) -> func.HttpResponse:

    digitalGoGeocodeService = DigitalGoGeocodeService(KEY_VAULT_URL, config['digital-go-geocode'])

    address = req.params.get('address')

    if address:
        geocode_result = digitalGoGeocodeService.get(address)
        return func.HttpResponse(
            json.dumps(asdict(geocode_result)),
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
             "Please pass an address in the query string.",
             status_code=200
        )

from src.service.translateService import TranslateService

@app.route(route="japanese-to-english", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def japanese_to_english(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for jp2en executed.')
    translateService = TranslateService(KEY_VAULT_URL, config['azure-translator'])

    jp_str = req.params.get('jp')

    if jp_str:
        en = translateService.jp2en(jp_str)

        return func.HttpResponse(
            json.dumps(asdict(en)),
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
            "Please pass an address in the query string.",
            status_code=200
        )
    