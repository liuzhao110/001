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
return response.json()["object"]["token"],response.text
print (response.text)
print(response.url)
print(response.headers)
print(response.json())
return