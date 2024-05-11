# エンドポイント一覧
https://dx-junkyard.github.io/OpenData-Bridge-proxy-api/

# 実行方法
Azure-Functionへデプロイして動かします

# ファイル構造
proxy-api
|- docs : openapi関連
|- src
|  |- main
|  |  |- DigitalGoGeocode: デジタル庁のジオコーディング
|  |  |- ExtractLinks: URLからリンクを抽出
|  |  |- Swagger: swagger関連
|  |  |- TranslateJpToEn: 日本語から英語へ翻訳
|  |- test
|  |- integrationTest
|     |- base.py: テストケースを記述しています
|     |- local.py: ローカルで動作させる場合にこのプログラムを実行させます
|- function_app.py : このプログラムが実行されます

# 設定事項
| 環境変数名 | 内容 |
| -- | -- |
| KEY_VAULT_URL | AzureキーコンテナーのURI |
| AZURE-TRANSLATOR-URL | Azure翻訳のWebAPIのテキスト翻訳のURL |
| TRANSLATE-API-KEY | Azure翻訳のAPIキー |
| digital-go-geocode-url | Docker containerで動かしているhttps://github.com/dx-junkyard/OpenData-Bridge-proxy-api/tree/main/digital-go-geocode へのURL |

# ローカル環境で動かす場合
local.settings.jsonに`KEY_VAULT_URL`を設定します
その他環境変数はAzureキーコンテナー上に設定します
