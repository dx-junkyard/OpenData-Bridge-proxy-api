
@REM set URL=https://dev-fukumoto.azurewebsites.net
set URL=https://odb-test-proxy-api-key.vault.azure.net

curl %URL%/api/health-check

curl %URL%/api/digital-go-geocode?address=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%8D%83%E4%BB%A3%E7%94%B0%E5%8C%BA%E7%B4%80%E5%B0%BE%E4%BA%95%E7%94%BA1-3

curl %URL%/api/japanese-to-english?jp=%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF

curl %URL%/api/extract-links?url=https://yahoo.co.jp

[
    {"href": "href1", "text": "text1"},
    {"href": "href2", "text": "text2"},
    {"href": "hrefn", "text": "textn"},
]