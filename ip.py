#归属地查询
import requests
ip = input("IP;")
url = "https://ip.cn/index.php?ip="
r = requests.get(url+ ip)
print(r.status_code,r.text)
