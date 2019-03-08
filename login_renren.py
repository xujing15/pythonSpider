# coding=utf-8
import requests


session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"15764368231","password":"15764368231"}
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"}

# 使用session发送post请求，cookie保存在其中
session.post(post_url, data=post_data, headers=headers)
# 在使用session进行请求登录之后才能访问的地址
r = session.get("http://www.renren.com/969985344/profile",headers=headers)

# 保存页面
with open("reren1.html","w",encoding="utf-8") as f:
	f.write(r.content.decode())
