#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Author:Jumbo
Website:http://www.chinabaiker.com
Thanks:ziwen
'''
import requests,sys
#定义URL和payload放在try里 要不然用户没有按照格式输入时会报错 而不提示except
try:
    url = sys.argv[1]
    payload = sys.argv[2]
#    filename = sys.argv[3]
    f = open(url + 'txt', 'w+')
    if not url.startswith('http://'):
        url = 'http://%s' % url
    if payload == 'php':
        for a in open('php.txt','r'):
            x = a.strip()
            sm = requests.get(str(url) + str(x))
            if sm.status_code == 200:
                print >> f,'the urls :\n' + sm.url + ' found - 200'
            elif sm.status_code == 403:
                print 'the urls :\n' + sm.url + ' found - 403'
            elif sm.status_code == 404:
                print 'the urls :\n' + sm.url + ' no found - 404'

    elif payload == 'asp':
        for b in open('asp.txt','r'):
            y = b.strip()
            sn = requests.get(str(url) + str(y))
            if sn.status_code == 200:
                print >> f,'the urls :\n' + sn.url + ' found - 200'
            elif sn.status_code == 403:
                print 'the urls :\n' + sn.url + ' found - 403'
            elif sn.status_code == 404:
                    print 'the urls :\n' + sn.url + ' no found - 404'
    elif payload == 'jsp':
        for c in open('jsp.txt','r'):
            z = c.strip()
            so = requests.get(str(url) + str(z))
            if so.status_code == 200:
                print >> f, 'the urls :\n' + so.url + ' found - 200'
            elif so.status_code == 403:
                print 'the urls :\n' + so.url + ' found - 403'
            elif so.status_code == 404:
                print 'the urls :\n' + so.url + ' no found - 404'
    elif payload == 'aspx':
        for d in open('aspx.txt','r'):
            w = d.strip()
            sp = requests.get(str(url) + str(w))
            if sp.status_code == 200:
                print >>f,'the urls :\n' + sp.url + ' found - 200'
            elif sp.status_code == 403:
                print 'the urls :\n' + sp.url + ' found - 403'
            elif sp.status_code == 404:
                print 'the urls :\n' + sp.url + ' no found - 404'

    f.close()

except:
   print ("usage: %s www.chinabaiker.com php(asp,aspx,jsp)" % sys.argv[0])

