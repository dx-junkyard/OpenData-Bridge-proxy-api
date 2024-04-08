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
| lon | float | 130.821747 | 経度 |

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

# サードパーティライブラリのクレジット
このプロジェクトには以下のライブラリが含まれています：
1. pandas
- ライセンス: BSD 3-Clause "New" or "Revised" License
- 著作権:
- - AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.　2008-2011,
- - Open source contributors. 2011-2024,
- このソフトウェアは、上記の著作権表示および条件リストを含めることを条件に、再配布および使用が許可されます。
- BSD-3-Clauseライセンスの詳細: https://opensource.org/license/bsd-3-clause
2. Flask
- ライセンス: BSD 3-Clause "New" or "Revised" License
- 著作権:Pallets 2010 
- このソフトウェアは、上記の著作権表示および条件リストを含めることを条件に、再配布および使用が許可されます。
- BSD-3-Clauseライセンスの詳細: https://opensource.org/license/bsd-3-clause
