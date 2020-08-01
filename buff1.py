#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import requests
import time,random

min=str(5)
max=str(10)
num=int(1)

#?game=csgo
cookies = {
    '_ntes_nnid': '057d398e28605b968740fd48763677d3,1586150334401',
    '_ntes_nuid': '057d398e28605b968740fd48763677d3',
    'Device-Id': '0GwqSboIbDrNJfEYlwON',
    '_ga': 'GA1.2.1127483396.1586338586',
    'Locale-Supported': 'zh-Hans',
    'game': 'csgo',
    '_gid': 'GA1.2.2116671957.1587088092',
    '_gat_gtag_UA_109989484_1': '1',
    'NTES_YD_SESS': 'mucMwLWLo7UFqEdUpc2rVaUo20LTKMoIHLeArKiEwwfjhziQhoRng7g0BxZG41JLVOQIqAFB87VIzMKG9NFMh0zJWeFSmP1IGmRiCsCeIN1p7jimKWg_fbzQk.c20DicJtMZc7fDeaXa7qrKWKx14quTS46SPt7jYZUb5XdgDggIS1zw3TjvgGVdPHJ5L2dy8zedMJ0tzim7hPlsxeTfXuVvGDBpD4CVTuQ98U4rw1mqu',
    'S_INFO': '1587088134|0|3&80##|13026205006',
    'P_INFO': '13026205006|1587088134|1|netease_buff|00&99|jix&1587040907&netease_buff#jix&360100#10#0#0|&0|null|13026205006',
    'session': '1-CJjmB8B3SIk-1CkZjhLZ7wUvRb5LTYnU2zFKI1JhapOz2043771529',
    'csrf_token': 'ImVjNDkzZTBmNzQzNDRiOGU0ZTVhYWFkMTEyMzU5MWQyOWMxMWFhNDgi.EXqcjA.7HuL3kBS9nCc-7zYX-0PNPeTF7I',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://buff.163.com/market/?game=csgo',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}



# idList = []
# for i in range(num):
#     # url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(i+1) + "&category_group=sticker&min_price=" + min + "&max_price=" + max #印花
#     url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(
#         i + 1) + "&min_price=" + min + "&max_price=" + max
#     print(url)
#     r = requests.get(url, headers=headers, cookies=cookies)
#     html = r.text
#     id = re.findall(r'\"id\"\:\s\d+', html)
#     for e in range(len(id)):
#         idnum = eval(id[e].split()[1])
#         idList.append(idnum)

# buyList = {}
# print(idList)
# for t in range(len(idList)):
#     goods_id = idList[t]
#     goods_url = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=" + str(
#         goods_id) + "&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&"
#     e = requests.get(goods_url, headers=headers, cookies=cookies)
#     good_text = e.text

#     count = 0
#     for m in re.finditer(r'\"price\"\:\s\"\d+(\.\d+)?\"', good_text):

#         count += 1
#         price = float(eval(m.group(0).split()[1]))
#         if count == 1:
#             p1 = price
#             # print("p1="+str(p1))
#         if count == 2:
#             p2 = price
#             # print("p2="+str(p2))
#             delta = (p2 * 100 - p1 * 100) / 100
#             print(delta)
#         if count == 3:
#             break
#     if round(delta, 3) > 0.5:
#         buy_url = "https://buff.163.com/market/goods?goods_id=" + str(goods_id) + "&from=market#tab=selling"
#         buyList[buy_url] = delta
#         print(buy_url)
#     if t % 9 == 0:
#         time.sleep(random.random() * 3)

# print(sorted(buyList.items(), key=lambda kv: (kv[1], kv[0])))







idDictionary = {}
for i in range(num):
    if i % 9 == 0:
        time.sleep(random.random() * 3)
    # url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(i+1) + "&category_group=sticker&min_price=" + min + "&max_price=" + max #印花
    url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(
        i + 1) + "&min_price=" + min + "&max_price=" + max
    # print(url)
    r = requests.get(url, headers=headers, cookies=cookies)
    html = r.text
    # print(html)
    id = re.findall(r'\"id\"\:\d+', html)
    # steam_url_List=re.findall(r'\"steam_market_url\":\".*?\"',html)
    steam_price_List=re.findall(r'\"steam_price_cny\"\:\"\d+\.\d*\"',html)
    for e in range(len(id)):
        # print(id[e])
        # print(steam_url_List[e])
        idnum = eval(id[e].split(":")[1])
        # steam_url=steam_url_List[e].split(":")[1]+steam_url_List[e].split(":")[2]
        # print(steam_url)
        steam_price=eval(steam_price_List[e].split(":")[1])
        idDictionary[idnum]=[steam_price]

num=0

for key in list(idDictionary.keys()):
    goods_url = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=" + str(
        key) + "&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&"
    buy_url="https://buff.163.com/market/goods?goods_id="+str(key)+"&from=market#tab=selling"
    e = requests.get(goods_url, headers=headers, cookies=cookies)
    good_text = e.text
    count = 0
    for m in re.finditer(r'\"price\"\:\"\d+(\.\d+)?\"', good_text):
        count += 1
        price = float(eval(m.group(0).split(":")[1]))
        if count == 1:
            buff_price=price
            idDictionary[key].append(buff_price)
            break
    idDictionary[key].append(buy_url)
    if type(idDictionary[key][1]) is float and type(eval(idDictionary[key][0])) is float:
        delta=(eval(idDictionary[key][0])*100-(idDictionary[key][1])*100)/100
        print(delta)
        if delta>0.5:
            # print(idDictionary[key])
            idDictionary[key].append(delta)
        else:
            del idDictionary[key]
    print(idDictionary[key])
    num+=1
    print(str(num/len(idDictionary)*100)+'%')
# print(idDictionary)
print(sorted(idDictionary.items(), key=lambda kv:kv[1][3]))




















