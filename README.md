# OpenData-Bridge-proxy-api
他APIへのリクエストを行うシステム
生成AI使用時にAPIキーが会話ログに残るとよくないので代わりにリクエストを行う

# ファイル構造  
|- proxy-api: Azure-Functionsで動作する。  
|- digital-go-geocode: Dockerfileでimageを作り使用する。Flaskでサーバーを立て、内部でhttps://github.com/digital-go-jp/abr-geocoder を呼び出している  

## I/F設計
https://dx-junkyard.github.io/OpenData-Bridge-proxy-api/

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
