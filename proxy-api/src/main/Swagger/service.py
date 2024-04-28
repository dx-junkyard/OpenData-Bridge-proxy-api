
try:
    from repository import SwaggerRepository
except:
    from .repository import SwaggerRepository

class SwaggerService(object):
    def __init__(self):
        self.repository = SwaggerRepository()

    def getUi(self):
        return self.repository.getUi()

    def getJson(self):
        return self.repository.getJson()
    