# OpenData-Bridge-proxy-api
https://github.com/dx-junkyard/OpenData-Bridge-proxy-apiをforkして改修を加えたものである

## I/F設計
### /digital-geocode [GET]
デジタル庁のジオコーディング
#### parameters
| name | in | type | required | description |
| -- | -- | -- | -- | -- |
| address | query | string | true | 住所 |

#### responses
| name | type | example | description |
| -- | -- | -- | -- |
| lg_code | string | 401030 | 全国地方公共団体コード |
| town_id | string | 0075001 | 町字ID |
| fulladdress | string | 福岡県北九州市若松区響町一丁目 | 所在地_連結表記 |
| prefecture | string | 福岡県 | 所在地_都道府県 |
| city | string | 北九州市若松区 | 所在地_市区町村 |
| town | string | 響町一丁目 | 所在地_町字 |
| lat | float | 33.940111 | 緯度 |
| lon | float 130.821747 | 経度 |

### /japanese-to-english [GET]
日本語を英語へ翻訳
#### parameters
| name | in | type | required | description |
| -- | -- | -- | -- | -- |
| jp | query | string | true | 翻訳したい日本語 |

#### responses
| name | type | example | description |
| -- | -- | -- | -- |
| en | string | Tokyo | 翻訳された英語のテキスト |


## digital-go-geocode
Flaskでサーバーを立て、内部でhttps://github.com/digital-go-jp/abr-geocoderを呼び出している

## proxy-api
内部でAzure 翻訳を呼び出している

## swagger endpoint
- /apidocs
- /swagger.json