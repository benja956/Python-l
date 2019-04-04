from weibopy import WeiboOauth2, WeiboClient
from collections import defaultdict
import time,re


client = WeiboClient("2.00smBtiFZt3nrCbd3c406d87mTFJMB")

# suffix 指定 API 的名称，parmas 是参数，在文档中有详细描述

province_list = defaultdict(list) # 保存按省划分的评论正文
comment_text_list = [] # 保存所有评论正文
provinces = {}

results = client.get(suffix='common/get_province.json', params={'country': '001'})
for prov in results:
    for code, name in prov.items():
        provinces[code] = name
print(provinces)

# 获取「自杀式单身」评论列表
# 共获取 10 页 * 每页最多 200 条评论
for i in range(1, 11):
    result = client.get(suffix='comments/show.json', params={'id': 4322140368509204, 'count': 200, 'page': i})

    comments = result['comments']
    if not len(comments):
        break

    for comment in comments:
        text = re.sub('回复.*?:', '', str(comment['text']))
        province = comment['user']['province']
        province_list[province].append(text)
        comment_text_list.append(text)

    print('已抓取评论 {} 条'.format(len(comment_text_list)))
    time.sleep(1)
fi = open("weibocommits.txt","w",encoding="utf-8")
fi.write(str(result))
print(result)