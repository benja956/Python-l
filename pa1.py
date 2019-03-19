import requests as re
r = re.get("http://www.baidu.com")
r.status_code
r.enconding = "utf-8"
print(r.text,r.encoding,r.apparent_encoding)
r.encoding = "utf-8"
print(r.text)
