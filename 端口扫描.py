# -*- coding: utf-8 -*-
__author__ = 'iswing'
import time
import thread
import socket
#扫描ip端口是否开放
def sock_ip(ip,PORT):
    try:
        if PORT>=2000:#65535
            print 'scanner ending'
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((ip,PORT))
        if (result==0):
            print ip,PORT,u'open'


        s.close()
    except:
        print 'error 1'

def  IP_port(date):
    try:
        t=time.time()
        for i in range(0,2000):
            thread.start_new_thread(sock_ip,(date,int(i)))
            time.sleep(0.003)
        print u'finish time:%f' % (time.time()-t)
    except:
        print u'error 2'
if __name__=='__main__':
    IP_port('127.0.0.1')