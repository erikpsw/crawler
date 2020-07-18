import re
import requests
import time,random

cookies = {
    '_ntes_nnid': 'c0a9486ed4e5d91c72812668fe88891c,1587290454965',
    '_ntes_nuid': 'c0a9486ed4e5d91c72812668fe88891c',
    'Device-Id': 'TMjvh9JnECyAvbziFjqs',
    '_ga': 'GA1.2.1244979980.1587298259',
    '_gid': 'GA1.2.1284201187.1587950146',
    'P_INFO': '13026205006|1588030063|1|netease_buff|00&99|jix&1587985821&netease_buff#jix&360900#10#0#0|&0|null|13026205006',
    'client_id': 'Atefq2lOu5gKTo0rMBgAOA',
    'Locale-Supported': 'zh-Hans',
    'game': 'csgo',
    '_gat_gtag_UA_109989484_1': '1',
    'csrf_token': 'ImQ3MmI1YmY5MzMzMGQwNTUzMGVmZTMwM2NkNWQzYzdlNjg4NGU0OWYi.EYkAJA.DtypdwIX6KqnfCWN6tdjv3NxCjc',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://buff.163.com/market/?game=csgo',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}



min=str(1)
max=str(5)
num=3

idList = []
urlList= []
for i in range(num):
    url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(
    i + 1) + "&sort_by=price.desc&min_price=" + min + "&max_price=" + max
    r = requests.get(url, headers=headers, cookies=cookies)
    html = r.text
    print(html)
    id = re.findall(r'\"id\"\:\d+', html)
    print(id)
    for e in range(len(id)):
        idnum = eval(id[e].split(':')[1])
        idList.append(idnum)
    if i % 9 == 0:
            time.sleep(random.random() * 3)
    print("1_"+str(round(i/num,1)*100)+'%')
print(idList)
    
for x in range(len(idList)):
    items_url = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id="+str(idList[x])+"&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1"
    buy_url = "https://buff.163.com/market/goods?goods_id=" + str(idList[x]) + "&from=market#tab=selling"
    t = requests.get(items_url, headers=headers, cookies=cookies)
    good_text = t.text
    items_fraudwarnings = re.findall(r'\"fraudwarnings\"\:\"', good_text)
    if len(items_fraudwarnings)>0:
        print(len(items_fraudwarnings))
        print(buy_url)
        urlList.append(buy_url)
    if x % 9 == 0:
            time.sleep(random.random() * 3)
    print("2_"+str(round(x/len(idList),2)*100)+'%')