#!/usr/bin/env python
import asyncio
from python3_anticaptcha import ImageToTextTask, CallbackClient
from python3_anticaptcha import errors
import urllib
ANTICAPTCHA_KEY = ""
import requests 
import json
import base64
r_post = requests.post("http://playserver.co/index.php/Vote/ajax_getpic/-Miss-Ro--จุติ-800-HI-CLASS-เปิด-030263-1700-20218",
             headers={
                 'accept': 'application/json, text/plain, /',
                 'referer': "http://playserver.in.th/index.php/Vote/prokud/-Miss-Ro--%e0%b8%88%e0%b8%b8%e0%b8%95%e0%b8%b4-800-HI-CLASS-%e0%b9%80%e0%b8%9b%e0%b8%b4%e0%b8%94-030263-1700-20218",
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
                 'referer': "http://playserver.in.th/index.php/Vote/prokud/-Miss-Ro--%e0%b8%88%e0%b8%b8%e0%b8%95%e0%b8%b4-800-HI-CLASS-%e0%b9%80%e0%b8%9b%e0%b8%b4%e0%b8%94-030263-1700-20218",
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
             })

base64_message = get_image.content
#print(base64_message)
message = base64.b64encode(base64_message).decode('utf-8')
#print(message)

#user_answer_base64  = input("Enter Employee Name")
#ser_answer_base64 = """Input__capture"""
#user_answer_base64 = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY).captcha_handler(captcha_base64=message)
#print(user_answer_base64)
url = "http://playserver.co/index.php/Vote/ajax_submitpic/-Miss-Ro--%5E%25%5EE0%5E%25%5EB8%5E%25%5E88%5E%25%5EE0%5E%25%5EB8%5E%25%5EB8%5E%25%5EE0%5E%25%5EB8%5E%25%5E95%5E%25%5EE0%5E%25%5EB8%5E%25%5EB4-800-HI-CLASS-%5E%25%5EE0%5E%25%5EB9%5E%25%5E80%5E%25%5EE0%5E%25%5EB8%5E%25%5E9B%5E%25%5EE0%5E%25%5EB8%5E%25%5EB4%5E%25%5EE0%5E%25%5EB8%5E%25%5E94-030263-1700-20218"

payload=urllib.parse.urlencode((("server_id", "20218"), ("captcha", user_answer_base64), ("gameid", "lanks007"), ("checksum", cut_get_image)))
headers = {
    'connection': "keep-alive",
    'accept': "*/*",
    'origin': "http://playserver.in.th",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'referer': "http://playserver.in.th/index.php/Vote/prokud/-Miss-Ro--^%^e0^%^b8^%^88^%^e0^%^b8^%^b8^%^e0^%^b8^%^95^%^e0^%^b8^%^b4-800-HI-CLASS-^%^e0^%^b9^%^80^%^e0^%^b8^%^9b^%^e0^%^b8^%^b4^%^e0^%^b8^%^94-030263-1700-20218",
    'accept-language': "en-GB,en;q=0.9,en-US;q=0.8"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print("Answer send vote data " + response.text)
  
