import requests
import os
import json
import re
def parseHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    r = requests.get(url,headers=headers)
    r.status_code
    r.encoding=r.apparent_encoding
    text = r.text
    regix =  '<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?div class="info.*?class="hd".*?class="title">(.*?)</span>.*?class="other">' \
            '(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?class="star.*?<span class="(.*?)"></span>.*?' \
            'span class="rating_num".*?average">(.*?)</span>'
    results = re.findall(regix,text,re.S)
    for item in results:
        print(item)
        root = 'F://pycharm//电影//'+item[0]+'.'+item[2]
        isExists = os.path.exists(root)
        if not isExists:
            os.makedirs(root)
        else:
            print("文件已存在")
            continue
        rpicture = requests.get(item[1],headers=headers)
        ulist = ['排名','','电影名称','称号','演员','地区和类型','星级','评分']
        with open(root+'//'+item[2]+'.jpg','wb') as f:
            f.write(rpicture.content)
        with open(root+'//'+item[2]+'.txt','w',encoding='utf-8') as f:
            for i in range(8):
                if i==1:
                    continue
                elif i==3:
                    f.write(ulist[i]+':'+re.sub('&nbsp;','',item[i])+'\n')
                elif i==4:
                    f.write(ulist[i]+':'+re.sub('&nbsp;','',item[i].strip())+'\n')
                elif i==5:
                    f.write(ulist[i]+':'+re.sub('&nbsp;','',item[i].strip())+'\n')
                elif i==6:
                    f.write(ulist[i]+':'+re.sub('&nbsp;','',star(item[i]))+'\n')
                else:
                    f.write(ulist[i]+':'+item[i]+'\n')
def star(str):
    if str=='rating5-t':
        return '五星'
    elif str=='rating45-t':
        return '四星半'
    elif str=='rating4-t':
        return '四星'
    elif str == 'rating35-t':
        return '三星半'
    elif str =='rating3-t':
        return '三星'
    elif str == 'rating25-t':
        return '二星半'
    elif str == 'rating2-t':
        return '二星'
    elif str == 'rating15-t':
        return '一星半'
    elif str == 'rating1-t':
        return '一星'
    else:
        return '无星'
def main():
    for offset in range(0,250,25):
        url = 'https://movie.douban.com/top250?start='+str(offset)+'&filter='
        parseHtml(url)
    print('爬取成功')
main()