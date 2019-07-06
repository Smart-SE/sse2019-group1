import os
import sys
from lib.linebot import (
    LineBotApi, WebhookHandler
)
from lib.linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from lib.linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
import logging

# log取得用

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

# reference
# https://github.com/line/line-bot-sdk-python
# https://developers.line.biz/ja/docs/messaging-api/overview/

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    logger.error('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def lambda_handler(event, context):
    logger.info(event) # lambdaが受けた取ったjsonの確認。cloudwatch logで見れる
    
    # reply用のtoken。これで誰のメッセージにレスするかが決まる。
    reply_token = event["events"][0]["replyToken"] 
    # 送信されたtext本文
    message = event["events"][0]["message"]["text"]

    # 必要な情報
    # beebotteのトークン？

    ###
    # ここに実装
    ###

    # 1. messageのパース
    # 2. S3 Pathの生成
    s3path = reply_token + "/" + message
    # 3. JSON Messageの生成
    json_message = "{\"key\", \"value\"}"
    # 4a. Beebotteへメッセージ送信
    # 4b. 親Lambdaへメッセージ送信

    # line botへのメッセージの返信。local test中はreply_tokenの更新が大変なのでreturnするなりしてテストしたほうが良いです。
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
    
    return "reply complete"
    
## memo
### 定期実行で呼び出す。
### 親Lambdaからくるメッセージ
#### 特になし！！！！
