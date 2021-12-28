import requests
def getHTTP(url):#被拒绝时通过修改头字段就行访问
    try:
        kv={'user-agent':'Mozilla/5.0'}#修改头字段，模拟成由浏览器进行的访问
        r=requests.get(url,headers=kv)

        print(r.raise_for_status)
        if r.encoding=='utf-8':
            return r.text

        else:
            r.encoding = r.apparent_encoding
            return r.text
    except:

        return "产生异常1"
def getHtml(url):#常规访问
    try:
        r=requests.get(url,timeout=5)
        print(r.raise_for_status)
        print(len(r.text))
        if r.encoding=='utf-8':
            return r.text
        else:
            r.encoding=r.apparent_encoding
            return r.text

    except:
        return "产生异常2"
def getHTTP1(url):#给网页发送关键字，并获得响应
    try:
        kv={'wd':'Python'}
        r=requests.get(url,params=kv)
        print(r.raise_for_status)
        return len(r.text)
    except:
        return  "产生异常3"
if __name__=="__main__":
    url="http://www.juanpi.com/search/i?keywords=书包"
    print(getHtml(url))
    #print(getHTTP(url))
    #print(getHTTP1(url))