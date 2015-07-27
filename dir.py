#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Author:Jumbo
Website:http://www.chinabaiker.com
Thanks:ziwen
'''
import requests,sys
import re
from bs4 import BeautifulSoup
#定义URL和payload放在try里 要不然用户没有按照格式输入时会报错 而不提示except
#try:
url = sys.argv[1]
payload = sys.argv[2]
errorr = open('error.txt','r')
aaaa = str(errorr.readline())
print aaaa
zhPattern = re.compile(aaaa)
#    filename = sys.argv[3]
f = open(url + '.txt', 'w+')
if not url.startswith('http://'):
    url = 'http://%s' % url
if payload == 'php':
    for a in open('php.txt','r'):
        x = a.strip()
        sm = requests.get(str(url) + str(x))
        body = BeautifulSoup(sm.text)
        body = str(body)
        match = zhPattern.search(body)
        if sm.status_code == 200:
            if match == None:
                print 'the urls :\n' + sm.url + ' found - 200'
                print >> f,sm.url
        elif sm.status_code == 403:
            print 'the urls :\n' + sm.url + ' found - 403'
        elif sm.status_code == 404:
            print 'the urls :\n' + sm.url + ' no found - 404'

elif payload == 'asp':
    for b in open('asp.txt','r'):
        y = b.strip()
        sn = requests.get(str(url) + str(y))
        body = BeautifulSoup(sn.text)
        body = str(body)
        match = zhPattern.search(body)
        if sn.status_code == 200:
            if match == None:
                print 'the urls :\n' + sn.url + ' found - 200'
                print >> f,sn.url
        elif sn.status_code == 403:
            print 'the urls :\n' + sn.url + ' found - 403'
        elif sn.status_code == 404:
                print 'the urls :\n' + sn.url + ' no found - 404'
elif payload == 'jsp':
    for c in open('jsp.txt','r'):
        z = c.strip()
        so = requests.get(str(url) + str(z))
        body = BeautifulSoup(so.text)
        body = str(body)
        match = zhPattern.search(body)
        if so.status_code == 200:
            if match == None:
                print 'the urls :\n' + so.url + ' found - 200'
                print >> f,so.url
        elif so.status_code == 403:
            print 'the urls :\n' + so.url + ' found - 403'
        elif so.status_code == 404:
            print 'the urls :\n' + so.url + ' no found - 404'
elif payload == 'aspx':
    for d in open('aspx.txt','r'):
        w = d.strip()
        sp = requests.get(str(url) + str(w))
        body = BeautifulSoup(sp.text)
        body = str(body)
        match = zhPattern.search(body)
        if sp.status_code == 200:
            if match == None:
                print 'the urls :\n' + sp.url + ' found - 200'
                print >>f,sp.url
        elif sp.status_code == 403:
            print 'the urls :\n' + sp.url + ' found - 403'
        elif sp.status_code == 404:
            print 'the urls :\n' + sp.url + ' no found - 404'

f.close()
#except:
#   print ("usage: %s www.chinabaiker.com php(asp,aspx,jsp)" % sys.argv[0])

error.txt放自定义的404关键词，不要太长
