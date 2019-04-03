import re
match = re.search(r"[1-9]\d{5}","BIT 100081")
if match:
    print(match.group((0)))

match2 = re.match(r"[1-9]\d{5}","100081")
if match2:
    print(match2.group((0)))

ls = re.findall(r"[1-9]\d{5}","BIT 100081,BIT 165081,BIT 101581")
if ls:
    print(ls)

ls2 = re.split(r"[1-9]\d{5}","BIT 100081,BIT 165081,BIT 101581")
if ls2:
    print(ls2)
for m in re.finditer(r"[1-9]\d{5}","BIT 100081,BIT 165081,BIT 101581"):
    if m:
        print(m.group(0))
v = re.sub(r"[1-9]\d{5}","zipcood","BIT 100081,BIT 165081,BIT 101581")
print(v)