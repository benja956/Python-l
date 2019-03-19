import requests
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/"
try:
     kv = {"user-agent":"Mozilla/5.0"}
     r = requests.get(url,headers = kv)
     r.encoding = r.apparent_encoding
     
     print(r.status_code,r.text,r.request.headers)
except:
     print("爬取失败")
