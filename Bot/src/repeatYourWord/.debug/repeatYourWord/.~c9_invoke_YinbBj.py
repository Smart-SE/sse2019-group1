import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def lambda_handler(event, context):
    print(event)
    print(context)
    
    ok_json = {'isBase64Encoded': False,
               'statusCode': 200,
               'headers': {},
               'body': ""}

#    print(event[0]["message"]["text"])
    message = event["events"][0]["message"]["text"]
    
    ok_json["body"] = message

    return ok_json
