import os
root = "D:\\txt\\"
for dirpath, dirnames, filenames in os.walk(root):
    for filepath in filenames:
        t = open(root + filepath,"r")
        txt = t.read()
        print(txt)
        txt.replace("\r", "").replace("\n", "")
        t.close()