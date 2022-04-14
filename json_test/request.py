__author__ = 'liusir'
import requests
base_url='http://httpbin.org'
#发送GET类型请求
r=requests.get(base_url+'/get')
print(r.status_code)
#发送post类型请求
r=requests.post(base_url+'/post')
print(r.status_code)
#发送put类型请求
r=requests.put(base_url+'/put')
print(r.status_code)
#发送delete类型请求
r=requests.delete(base_url+'/delete')
print(r.status_code)