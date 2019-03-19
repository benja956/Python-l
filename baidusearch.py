import requests
try:
     
     kv = {"wd":"python"}
     r = requests.get("http://www.baidu.com/s",params = kv)
     print(r.status_code,len(r.text))
     
except:
     
     print(r.request.url)
