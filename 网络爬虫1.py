#-*-coding:utf-8-*-
__author__ = 'iswing'
import urllib
# print dir(urllib)  可以输出urllib里的方法
# print help(urllib.urlopen)
# url='http://www.huodongjia.com'
#
# html=urllib.urlopen(url)
# print html.read()
#是utf-8的编码可以直接读取出来
#如果不是，如gb2312,gb2312都写作gbk
# print html.read().decode('gbk','ignore').encode('utf-8')
#加ignore会忽略无法转换的模块
# print html.info()
#读头部信息
# print html.getcode()
#获得网页状态码，状态码是200才能抓取
#200表示可以正常访问
#301永久重定向
#302临时重定向
#404网页不存在
#403禁止访问
#500服务器无响应，服务器问题
# print html.geturl()
#获取传入url
# html.close()
#关闭打开的文件
# urllib.urlretrieve(url,"c:\\123.html")
#保存到本地
# urllib.urlretrieve(url,"c:\\python.html")
"""
参数
1.传入网址，为字符串
2.传入本地保存路径+文件名称
3.一个函数的调用，可以任意定义函数的行为，单数必须有三个参数
参数1.传递数据块数量
    2.数据块大小byte（字节）
    3.获取远程文件大小，有时候返回-1
"""

# def callback(a,b,c):
#     down_pro = 100.0*a*b/c
#     if down_pro > 100:
#         down_pro = 100
#     print '%.2f%%'%down_pro,
#     #%.2f是保留两个小数位
# url = 'http://www.360.cn'
# local = "c:\\python.html"
# urllib.urlretrieve(url,local,callback)
# import urllib
# url = 'http://www.jd.com'
# info = urllib.urlopen(url).info()
# print info.getparam('charset')
#获取网页编码
#返回None，是因为头部没有声明
#有些网站服务器声明的编码和页面编码不一样，防爬的
# import chardet #字符集检测
# import  urllib
# url = 'http://www.jd.com'
# content = urllib.urlopen(url).read()
# result = chardet.detect(content)
# #confidence 为可信度，原理是监测内容判断，不是读声明的编码
# print result['encoding']#输出编码

# def automatic_detect(url):
#     content =urllib.urlopen(url).read()
#     result = chardet.detect(content)
#     encoding = result['encoding']
#     return  encoding
# url='http://jd.com'
# # print automatic_detect(url)
#
# urls = [
#     'http://www.weibo.com',
#     'http://www.jd.com',
#     'http://www.dangdang.com'
#
# ]
# for s in urls:
#     print s,automatic_detect(s)

# import urllib
# url = 'http://blog.csdn.net/wolf96/article/details/44057915'
# html = urllib.urlopen(url)
# print html.read().decode('gbk').encode('utf-8')

# import urllib2
my_headers=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            "Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"


            ]
url = 'http://blog.csdn.net/wolf96/article/details/44057915'
# url = 'http://blog.csdn.net/wolf96/article/details/44057915'
#
# req = urllib2.Request(url,headers=my_headers)
# html = urllib2.urlopen(req)

#
# print html.read()
# print req.headers.items()
import urllib2
import random
def get_content(url,headers):
   random_header = random.choice(headers)
   req = urllib2.Request(url)
   req.add_header("User-Agent",random_header)
   req.add_header("Host","blog.csdn.net")
   req.add_header("Referer","http://blog.csdn.net/")
   req.add_header("GET",url)

   content = urllib2.urlopen(req).read()
   return content

print get_content(url,my_headers)
