# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
from take_photo_picam import take_photo
from upload_s3 import upload_img_to_s3
import os
import traceback
import logger as log

TOKEN = None
with open('bebotte_token', 'r') as f:
    TOKEN = f.readlines()[0]
TOPIC = "IoT_Refrigerator/take_req"
HOSTNAME = "mqtt.beebotte.com"
PORT = 8883
CACERT = "mqtt.beebotte.com.pem"
REQ_TYPE = 'req_type'
BUCKET_NAME = 's3_bucket'


def on_connect(client: object, userdata: object, flags, respons_code: int):
    """Connection event handler

    Arguments:
        client {object} -- mqtt clinet
        userdata {object} -- unknown
        flags {[type]} -- unknown
        respons_code {int} -- status of connection
    """
    print('status {0}'.format(respons_code))
    log.Info('status {0}'.format(respons_code))
    client.subscribe(TOPIC)
    log.Info("start to subscribe: " + TOPIC)


def on_message(client: object, userdata: object, msg: str) -> None:
    """Message recieve event handler

    Arguments:
        client {object} -- mqtt clinet
        userdata {object} -- unknown
        msg {str} -- recieved message
    """
    try:
        data = json.loads(msg.payload.decode("utf-8"))["data"]
        if type(data) is str:
            # データが文字列で渡されてるので、そこだけ再度、オブジェクト化
            data = json.loads(data)
        else:
            data = data

        data = {key: value.strip() for key, value in data.items()}
        action = data[REQ_TYPE]

        if BUCKET_NAME in data:
            bucket_name = data[BUCKET_NAME]
        else:
            bucket_name = None

        log.Info("aciton='{0}', bucket_name='{1}'".format(action, bucket_name))
        if action == "take_photo":
            file_name = "tmp.jpg"
            take_photo(file_name)
            if os.path.exists(file_name):
                upload_img_to_s3(file_name, bucket_name)
                log.Info("finish process for a take_req")
            else:
                log.Error("failed to take photo")
        else:
            log.Warn(data)
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    client = mqtt.Client()
    client.username_pw_set("token:%s" % TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set(CACERT)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()
