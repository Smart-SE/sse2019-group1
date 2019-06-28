# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import requests
import numpy as np
import cv2
import ipget
from datetime import datetime

TOKEN = ""
TOPIC = ""
HOSTNAME = "mqtt.beebotte.com"
PORT = 8883

CACERT = "mqtt.beebottle.com.pem"
dir_path = "./img/"
ip = ipget.ipget()
ServerIP = "{}:5000".format(ip.ipaddr("wlan0").split("/")[0])

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(TOPIC)

def send_item_change_request(command, item, amount):
    url = "http://{0}/{1}?item={2}&amount={3}".format(ServerIP, command, item, amount)
    print(url)
    requests.get(url)
    return 

def take_and_send_photo():
    cap = cv2.VideoCapture(0)
    file_name = "{0}{1}.jpeg".format(dir_path, datetime.now().strftime("%Y%m%d%H%M%S"))
    ret, frame = cap.read()
    cv2.imwrite(file_name, frame)
    print("send image :{}".format(file_name))
    cap.release()


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))["data"][0]
    data = {key:value.strip() for key, value in data.items()}
    action = data['action']
    print(data)
    if action == u"add":
        item = data['item']
        amount = data['num']
        send_item_change_request("Add", item, amount)
    elif action == u"reduce":
        item = data['item']
        amount = data['num']
        send_item_change_request("Reduce", item, amount)
    elif action == u"take":
        take_and_send_photo()
    else:
        print(data)
        
client = mqtt.Client()
client.username_pw_set("token:%s"%TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(CACERT)
client.connect(HOSTNAME, port=PORT, keepalive=60)
client.loop_forever()
