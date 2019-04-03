import requests,re

def gethtmltxt(url):
    try:
        r = requests.get(url , timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsepage(ilt,html):

 #plt = re.findall(r"\"view_price\"\:\"[\d\.]*\"",html)
    tlt = re.findall(r"\"title\"\:\".*?\"",html)
    for i in range(len(tlt)):
 #price = eval(plt[i].split(":")[1])
        title = tlt
        ilt.append([title])

def printgoodlist(ilt):
    tplt = "{:4}\t{:8}"
    print(tplt.format("序号", "title"))
    count = 0
    iltstror = str(ilt[0])

    for i in "[]'":

        iltstr = iltstror.replace(i,"").split(",")
    for le in range(len(iltstr)):
        print(iltstr[le])


    #print(iltstr[0])
    #print(type(iltstr[0]))
    ma = re.compile(r"\(\"([^\"]*)\"\)")
    lsq = []
    for x in iltstr[0]:
        x.replace('"',"")
        lsq.append(x)
        print(lsq)



def main():
    infolist = []
    url = 'https://www.bilibili.com/ranking'
    html = gethtmltxt(url)
    parsepage(infolist,html)

    printgoodlist(infolist)


main()