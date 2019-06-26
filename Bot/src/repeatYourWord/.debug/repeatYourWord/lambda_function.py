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

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

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
    reply_token = event["events"][0]["replyToken"]
    message = event["events"][0]["message"]["text"]

    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
    
    return "reply complete"
    
    