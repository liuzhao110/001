__author__ = 'liusir'
import requests
base_url='http://httpbin.org'
#设置cookie
cookie={'user':'liuliu'}
r=requests.get(base_url+'/get',cookies=cookie)
print(r.text)
#获取cookie
r=requests.get('https://www.baidu.com')
print(type(r.cookies))
print(r.cookies)
#遍历解析cookie值
for key,value in r.cookies.items():
    print(print,':',value)