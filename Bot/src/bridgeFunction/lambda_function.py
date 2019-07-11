import os
import sys
import json 
import requests
import logging

# log取得用

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def lambda_handler(event, context):
    # 必要な情報
    # beebotteのトークン？

    # 1. JSON Messageの生成
    json_message = { 'data': [{
            'req_type': 'take_photo'}]
            }

    # 2a. Beebotteへメッセージ送信
    url = "https://api.beebotte.com/v1/data/publish/IoT_Refrigerator/take_req?token=token_nKF6BPghiGhTwZ1L"
    response = requests.post(url, data=json.dumps(json_message),headers={'Content-Type': 'application/json'})
    # 2b. 親Lambdaへメッセージ送信
    return response.json()
    
## memo
### 定期実行で呼び出す。
### 親Lambdaからくるメッセージ
#### 特になし！！！！
