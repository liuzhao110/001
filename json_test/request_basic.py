__author__ = 'liusir'
import requests
base_url='http://httpbin.org'
#传递url参数
# param_data={'user':'liuliu','password':'666666'}
# r=requests.get(base_url+'/get',param_data)
# print(r.status_code)
# print(r.url)
#传递body参数
# form_data={'user':'liuliu','password':'444444'}
# r=requests.post(base_url+'/post',form_data)
# print(r.text)
#请求header定制
form_data={'user':'liuliu','password':'444444'}
header={'user-agent':'Mozilla/5.0'}
r=requests.post(base_url+'/post',data=form_data,headers=header)
#获取响应状态码
print(r.status_code)
#获取响应头信息
print(r.headers)
#获取响应内容
print(r.text)
#将响应的信息以json格式返回
print(r.json())


# #请求headers知乎
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
# r=requests.get("https://www.zhihu.com/explore",headers=headers)
# print(r.text)
