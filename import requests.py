#!/usr/bin/env python
import asyncio
from captcha2upload import CaptchaUpload


import urllib

import requests 
import json
import base64
captcha = CaptchaUpload(<YOURKEY>)
print captcha.solve(<PATHFILE>)
# while 1:
r_post = requests.post("http://playserver.co/index.php/Vote/ajax_getpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218",
            headersz={
                'accept': 'application/json, text/plain, /',
                'content-type': "application/x-www-form-urlencoded",
                'referer': urllib.parse.quote_plus("http://playserver.co/index.php/Vote/ajax_getpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218"),
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            })
#print(r_post.content)
a = r_post.text 
cut_get_image = a[28 :44] ##cut get only checksum
print("\n"+"checksum : " + cut_get_image + "\n") 
URL_image = "http://playserver.co/index.php/VoteGetImage/"+cut_get_image ##URL
print("URL :  " + URL_image+ "\n")
get_image = requests.get("http://playserver.co/index.php/VoteGetImage/"+cut_get_image,
                headers={
                'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'content-type': "application/x-www-form-urlencoded",
                'referer': urllib.parse.quote_plus("http://playserver.co/index.php/Vote/ajax_getpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218"),
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            })

base64_message = get_image.content
#print(base64_message)
message = base64.b64encode(base64_message).decode('utf-8')
print(message)

user_answer_base64  = input()
#print(user_answer_base64)
#user_answer_base64 = """Icapture"""
#user_answer_base64 = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY).captcha_handler(captcha_base64=message)
#print(user_answer_base64)
url = "http://playserver.co/index.php/Vote/ajax_submitpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218"

payload=urllib.parse.urlencode((("server_id", "20218"), ("captcha", user_answer_base64), ("gameid", "lanks007"), ("checksum", cut_get_image)))
print(payload)
headers = {
        'accept': "application/json, text/plain, /",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109",
        'content-type': "application/x-www-form-urlencoded",
        'referer': urllib.parse.quote_plus("http://playserver.co/index.php/Vote/ajax_getpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218")
    }

response = requests.request("POST", url, data=payload, headers=headers)
print("Answer send vote data " + response.text)
