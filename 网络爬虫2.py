#-*-coding:utf-8-*-
__author__ = 'iswing'
import urllib
from bs4 import BeautifulSoup
#用BeautifulSoup就可以不用正则表达式，直接用字典的键值对筛选
def get_content(url):
    html = urllib.urlopen(url)
    content = html.read()
    html.close()

    return content
info = get_content('http://tieba.baidu.com/p/2772656630')
def get_images(info):
     soup = BeautifulSoup(info)
     all_img = soup.find_all('img',class_='BDE_Image')

     x = 1

     for img in all_img:
         print img
         image_name = '%s.jpg' % x
         urllib.urlretrieve(img['src'], image_name)#用字典的键值对来筛选
         x+=1



print get_images(info)