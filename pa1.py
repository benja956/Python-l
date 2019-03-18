import requests as re
r = re.get("http://www.baidu.com")
r.status_code
r.enconding = "utf-8"
print(r.text)
