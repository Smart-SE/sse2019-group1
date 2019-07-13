import logging

import os
import urllib.request, urllib.parse
import json
import boto3
import base64
import hashlib
import hmac

import requests
from time import sleep

AWS_S3_BUCKET_NAME = 'sse02-group1-fridgepics'
s3 = boto3.resource('s3')      # ③S3オブジェクトを取得

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

        # LINE に発言する
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['LINE_CHANNEL_ACCESS_TOKEN'],
        }

        logger.info(json.dumps(request))
        logger.info(json.dumps(event))

        # 反応する発言内容を絞り込む
        if event['message']['text'] == '冷蔵庫':
            clientLambda = boto3.client("lambda")
            clientLambda.invoke(
                FunctionName="arn:aws:lambda:ap-northeast-1:058683116442:function:bridgeFunction",
                InvocationType="Event",
                Payload=json.dumps(event)
            )
            body = {
                'replyToken': event['replyToken'],
                'messages': [
                    {
                        'type': "image",
                        'originalContentUrl': os.environ['PICTURE_S3_URL']+"tmp.jpg",
                        'previewImageUrl': os.environ['PICTURE_S3_URL']+"tmp.jpg"
                    }
                ]
            }
        else:
            bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
            print(bucket.name)
            print(bucket.objects.all())
            print([obj_summary.key for obj_summary in bucket.objects.all()])
            body = {
                'replyToken': event['replyToken'],
                'messages': [
                    {
                        'type': 'text',
                        'text': event['replyToken']
                    }
                ]
            }
        req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST', headers=headers)
        with urllib.request.urlopen(req) as res:
            res_body = res.read().decode('utf-8')
            if res_body != '{}':
                logger.info(res_body)

    return {'statusCode': 200, 'body': '{}'}