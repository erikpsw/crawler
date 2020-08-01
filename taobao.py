#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import requests


#正则表达式：简洁，快速表达一组具有某特征的字符串
#邮政编码
# match=re.search(r'[1-9]\d{5}','bad100081')
# if match:
#     print(match.group(0))
#     print(match.string)
#     print(match.re)
#     print(match.pos)
#     print(match.endpos)
#     print(match.start())
#     print(match.end())  #注意后面的括号
# ls=re.findall(r'[1-9]\d{5}','bad 100081 215656')
# print(ls)   #列表
# sp=re.split(r'[1-9]\d{5}','dkasj100081 sdasd123131')
# print(sp)  #去掉匹配的部分
# for m in re.finditer(r'[1-9]\d{5}','dkasj100081 sdasd123131'):
#     print(m.group(0))  #迭代获得结果
# sub=re.sub(r'[1-9]\d{5}', 'zipcode','dkasj100081 sdasd123131')
# print(sub)  #替换字符串
#面向对象
# pat=re.compile(r'[1-9]\d{5}')
# ret=pat.search('asdknlad100654adasd')
# print(ret)




goods=input("请输入商品名称")
deep=input("输入深度")
start_url="https://s.taobao.com/search?q="+goods
infoList=[]
for i in range(int(deep)):
        url=start_url+'&='+str(43*i+1)
        header = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'sec-fetch-dest': 'document',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'referer': 'https://i.taobao.com/my_taobao.htm?spm=a1z0d.6639537.754894437.3.466674841xc9ZV&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'thw=cn; cna=J8vbFkwjhxACAbfZMkKg8oJ/; t=b6a9532b6612dab19d1561538ac8be29; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; v=0; cookie2=12740fdbbb2457facfc27af8a9e49c00; _tb_token_=393e815eb88b; birthday_displayed=1; alitrackid=www.taobao.com; _samesite_flag_=true; sgcookie=DDMnewwhePuy9mNxtQF2S; unb=2202336448855; uc3=vt3=F8dBxd3yPWoNXA3ejfg%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=F5RDK1PJE9C3BnM%3D&id2=UUphyItpZ6DVgDDKgA%3D%3D; csg=0bdfbd68; lgc=tb670491663; cookie17=UUphyItpZ6DVgDDKgA%3D%3D; dnk=tb670491663; skt=ea1bd1345fdd1e95; existShop=MTU4Mjc5NTM1Mg%3D%3D; uc4=nk4=0%40FY4I6FDzX1a3I0iw88n6aHw2ncLq5w%3D%3D&id4=0%40U2grE1hDDK%2Bj%2B6ZOjFgEvMiSNoahP7Py; tracknick=tb670491663; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=352; _nk_=tb670491663; cookie1=AQXKZZKCH6NIGk7yj1Nk8ACWrdHwvszaOxwicgAvG7A%3D; tfstk=ckXcBg4MasRbJyCZYx9ffJDp6C2dZ6kw-OW5UtVr_BK5nTXPiehrT7XuqEbcBf1..; enc=G5Sm81YgG1URIZ5TYjbwJfq8CLka5n61F2TeUjuqo9tXrdLx64uQUwqQOxXMOF%2FDZufyNdXnWnLg9zAjonUE89Q8NTdM7MsQJ8mn2iHuN4o%3D; mt=ci=1_1; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTUOLRwaKXK%2Fw%3D%3D&cart_m=0&tag=8&lng=zh_CN; JSESSIONID=479EB399924468C4132471CA76C552CD; lastalitrackid=i.taobao.com; isg=BCQkk7PwJsA151KMZACjLsfC9SIWvUgnFL-2wD5FsO-y6cSzZs0Yt1pLrUFxKoB_; l=dBP-txE7QhCR7Zt9BOCwSA5pAN_OSIRYYu8aAn5Mi_5Zd6T12tbOo8vOSF96VjWftQTB4o0COBp9-etkq3DmndK-g3fPaxDc.',
        }

        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html=r.text
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split('\"')[3])
            title = tlt[i].split('\"')[3]
            infoList.append([title,price ])
print("=====================================================================================================")
tplt = "{0:<3}\t{1:<30}\t{2:>6}"
print(tplt.format("序号","商品名称","价格"))
count = 0
for g in infoList:
    count += 1
    print(tplt.format(count,g[0],g[1]))



# +	  匹配前面的子表达式一次或多次。
# *	  匹配前面的子表达式零次或多次。
# .*? 任意字符串

