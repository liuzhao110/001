__author__ = 'liusir'
#!/usr/bin/env python
#coding:utf-8
import requests,json
url="http://httpbin.org"
headers={'Content-Type':'application/json;charset=UTF-8'}
request_param={
    "phone":"18200000000",
    "password":"111111"
}
response=requests.post(url+'/post',data=json.dumps(request_param), headers=headers)
#return response.json()["object"]["token"],response.text
print ('响应文本：\f',response.text)
print('响应url：\a',response.url)
print('响应header：\t',response.headers)
print('响应json：\n',response.json())
print('响应状态：',response.status_code)

#return