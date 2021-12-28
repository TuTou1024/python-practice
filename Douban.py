import requests
import re
import json
import os
from urllib import request

def parseHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url, headers=headers)
    text = response.text

    regix = '<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?div class="info.*?class="hd".*?class="title">(.*?)</span>.*?class="other">' \
            '(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?class="star.*?<span class="(.*?)"></span>.*?' \
            'span class="rating_num".*?average">(.*?)</span>'

    results = re.findall(regix, text, re.S)
    #爬取当前页面的有关内容
    for item in results:
        #创建文件夹

        root = 'F://pyCharm//电影//'+item[0]+'.'+item[2]
        isExist = os.path.exists(root)
        if not isExist:
            os.makedirs(root)
        else:
            print("文件已存在")
            continue

        r = requests.get(item[1], headers=headers)
        with open(root + '//' + item[2] + '.jpg', 'wb') as f:
            f.write(r.content)


        yield {
            '电影名称' : item[2] ,
            '其他' : re.sub('&nbsp;','',item[3]),
            '导演和演员' : re.sub('&nbsp;','',item[4].strip()),
            '评分': star(item[6].strip()) + '/' + item[7] + '分',
            '排名' : item[0]
        }


def main():
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset) +'&filter='
        #翻页
        for item in parseHtml(url):
            print(item)
            res = [value for value in item.values()]
            root = 'F://pyCharm//电影//'+res[-1]+'.'+res[0]
            print(root)
            with open(root+'//'+res[0]+'.txt','w',encoding='utf-8') as f:
                f.write(json.dumps(item,ensure_ascii=False))
def star(str):
    if str == 'rating5-t':
        return '五星'
    elif str == 'rating45-t' :
        return '四星半'
    elif str == 'rating4-t':
        return '四星'
    elif str == 'rating35-t' :
        return '三星半'
    elif str == 'rating3-t':
        return '三星'
    elif str == 'rating25-t':
        return '两星半'
    elif str == 'rating2-t':
        return '两星'
    elif str == 'rating15-t':
        return '一星半'
    elif str == 'rating1-t':
        return '一星'
    else:
        return '无星'

if __name__ == '__main__':
    main()
