#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http.client, urllib.parse
import json

def http_post(ip,port,method,src):
    input_str = json.dumps({"input":src})
    print(input_str)
    headers = {"Content-type": "Content-Type: application/json", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(ip,port)
    conn.request('POST', method, input_str, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read().decode('utf-8')
    conn.close()
    #print(json.loads(data))
    result = json.loads(data)
    return result

src = "原告王素文诉称，我与二被告系同村村民。1999年8月6日，被告冯立凡与被告袁杰安签订转让协议书，被告冯立凡将其承包的三亩地转让给被告袁杰安，由于转让费是我出的，后被告袁杰安又为我出字据，承认我为该地的承包经营权人。要求法院确认我是该地的承包经营权人。"
result = http_post("172.23.7.101","8400","/predict",src)
print(result)