#!/usr/bin/python
#coding:utf-8
import ZoomEye
import json
import sys,os

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
if __name__ == '__main__':

    search_type = 'Host'
    search_page = 3
    search_info = "AC2400"
    username = "xxxx"
    password = "xxxx"
    res = {}
    search_type = search_type.lower()
    login_Token = ZoomEye.login_token(username,password)
    for i in range(1,int(search_page)+1):
        search_resualt = ZoomEye.search_type_info(login_Token,search_type,search_info,i)
        data = json.loads(search_resualt)
        if (data.has_key("total")) == True:
            if search_type == "host":
                for i in range(len(data["matches"])):
                    ip = data["matches"][i]["ip"]
                    print ip
                    with open(cur_file_dir()+"/ip.txt", "a") as code:
                        code.write(ip+"\n")
            if search_type == "web":
                for i in range(len(data["matches"])):
                    url = data["matches"][i]["webapp"][0]["url"]
                    with open(cur_file_dir()+"/url.txt", "a") as code:
                        code.write(url+"\n")
                    print url
        else:
            break
