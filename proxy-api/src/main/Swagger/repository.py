import os
import json

class SwaggerRepository(object):
    def __init__(self):
        self.docsPath = __file__
        for i in range(4):
            self.docsPath = os.path.dirname(self.docsPath)
        self.docsPath = os.path.join(self.docsPath, 'docs')

    def getUi(self):
        with open(os.path.join(self.docsPath, 'index.html'), 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()

        return html_content

    def getJson(self):
        with open(os.path.join(self.docsPath, 'openapi.json'), 'r', encoding='utf-8') as fp:
            swaggerJson = json.load(fp)
        
        return swaggerJson
    