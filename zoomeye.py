#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

def login_token(username,password):
    url = "http://api.zoomeye.org/user/login"
    login_info = {"username":username,"password":password}
    json_data = json.dumps(login_info)
    req = requests.post(url,data=json_data)
    hjson = json.loads(req.content)
    strToken = hjson['access_token']
    LoginToken = "JWT "+strToken
    return LoginToken
def search_type_info(login_Token,search_type,search_info,search_page):
    url = "http://api.zoomeye.org/%s/search?query=\"%s\"&page=%s" % (search_type,search_info,str(search_page))
    headers = {'Authorization':login_Token}
    req = requests.get(url = url,headers=headers)
    return req.content