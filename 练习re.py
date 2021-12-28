import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败1"

def parsePage(ilt,html):
    try:
        plt=re.findall(r'"price-current"><em>￥</em>[\d.]*',html)#\"price-current"><em>￥</em>[\d.]*
        tlt=re.findall(r'k">.*?</a><span',html)    #"_blank">.*?<
        for i in range(len(plt)):
            price = plt[i][26:]
            title = tlt[i][3:-9]
            ilt.append([price,title])
    except:
        return "爬取失败2"

def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'
    depth=2
    start_url='http://www.juanpi.com/search/1?keywords='+goods
    infoList=[]
    for i in range(depth):
        try:
            url='http://www.juanpi.com/search/2?keywords='+goods
            if i==0:
                html=getHTMLText(start_url)
                parsePage(infoList,html)
            else:
                html = getHTMLText(url)
                parsePage(infoList, html)
        except:
            print("爬取失败")
            continue
    printGoodsList(infoList)
main()