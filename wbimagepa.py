import requests,os
url = "https://wx4.sinaimg.cn/mw690/75614297ly1g1794n7bcjj20ya6noe82.jpg"
root = "D:/pics/"
path = root + url.split("/")[-1]
if not os.path.exists(root):
     os.mkdir(root)
if not os.path.exists(path):
     r = requests.get(url)
     with open(path,"wb") as f:
          f.write(r.content)
          f.closed
     print("saved successfully")
else:
     print("the jpg is exist")

