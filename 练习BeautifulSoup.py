import requests
import json
from bs4 import BeautifulSoup
import bs4

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)#x只列出20所大学的相关信息
    writeText(uinfo,20)
def getHTMLText(url):
    try:

        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:             #找到tbody，并且用tr遍历tbody中的元素
        if isinstance(tr,bs4.element.Tag):             #检测是不是Tag类型
            tds = tr('td')                             #把td元素封装到tds中，用ulist储存
            ulist.append([tds[0].string,tds[1].string,tds[3].string])



def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print("{0:^10}\t{1:^6}\t{2:^17}".format("排名","学校名称","总分",chr(12288)))#打印表头,chr(12288)使用中文填充，美观
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def writeText(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    with open('中国大学.txt','a') as f:
        f.write("{0:^10}\t{1:^6}\t{2:^17}".format("排名", "学校名称", "总分", chr(12288))+'\n')
        for i in range(num):
            u=ulist[i]
            f.write(tplt.format(u[0],u[1],u[2],chr(12288))+'\n')
        f.close()
    print("爬取成功")



main()
