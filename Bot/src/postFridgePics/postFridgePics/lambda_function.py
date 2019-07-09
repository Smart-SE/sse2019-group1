import logging

import os
import urllib.request, urllib.parse
import json

import base64
import hashlib
import hmac

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(request, context):

    # リクエストの検証を行う
    channel_secret = os.environ['LINE_CHANNEL_SECRET']
    body = request.get('body', '')
    hash = hmac.new(channel_secret.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash).decode('utf-8')

    # LINE 以外からのアクセスだった場合は処理を終了させる
    if signature != request.get('headers').get('X-Line-Signature', ''):
        logger.info(f'LINE 以外からのアクセス request={request}')
        return {'statusCode': 200, 'body': '{}'}

    for event in json.loads(body).get('events', []):

        logger.info(json.dumps(request))
        logger.info(json.dumps(event))
        
        message =(event['message'])
        text = (message['text'])
        print (text)
        
        # LINE に発言する
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['LINE_CHANNEL_ACCESS_TOKEN'],
        }
#        body = {
#            'replyToken': event['replyToken'],
#            'messages': [
#                {
#                    'type': 'text',
#                    'text': text
#                }
#            ]
#        }
        body = {
            'replyToken': event['replyToken'],
            'messages': [
                {
                      'type': "image",
                      'originalContentUrl': os.environ['PICTURE_S3_URL']+text,
                      'previewImageUrl': os.environ['PICTURE_S3_URL']+text
                }
            ]
        }
        req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST', headers=headers)
        print(req)
        with urllib.request.urlopen(req) as res:
            res_body = res.read().decode('utf-8')
            if res_body != '{}':
                logger.info(res_body)

    return {'statusCode': 200, 'body': '{}'}