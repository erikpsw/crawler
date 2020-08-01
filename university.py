from bs4 import BeautifulSoup
import requests
import bs4

url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,"html.parser")
ulist=[]
for tr in soup.find('tbody').children:
    if isinstance(tr,bs4.element.Tag):    #判断类型，滤去字符串
        tds=tr('td') #等价于tr.find_all('td')
        ulist.append([tds[0].string,tds[1].string,tds[3].string])
#格式化输出

for i in range(int(input())):
    u=ulist[i]
    print(u[0]+"   "+u[1]+"    "+u[2])

