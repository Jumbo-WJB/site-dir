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
try:
    url = sys.argv[1]
    payload = sys.argv[2]
    errorr = open('error.txt','r')
    aaaa = str(errorr.readline())
    print aaaa
    zhPattern = re.compile(aaaa)
    f = open('success.txt', 'w+')
#if not url.startswith('http://'):
#    url = 'http://%s' % url
    if payload == 'php':
        for a in open('php.txt','r'):
            x = a.strip()
            sm = requests.get(str(url) + str(x),allow_redirects = False)
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
            sn = requests.get(str(url) + str(y),allow_redirects = False)
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
            so = requests.get(str(url) + str(z),allow_redirects = False)
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
            sp = requests.get(str(url) + str(w),allow_redirects = False)
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
    else:
        for da in open(payload,'r'):
            wa = da.strip()
            spa = requests.get(str(url) + str(wa),allow_redirects = False)
            body = BeautifulSoup(spa.text)
            body = str(body)
            match = zhPattern.search(body)
            if spa.status_code == 200:
                if match == None:
                    print 'the urls :\n' + spa.url + ' found - 200'
                    print >>f,spa.url
            elif spa.status_code == 403:
                print 'the urls :\n' + spa.url + ' found - 403'
            elif spa.status_code == 404:
                print 'the urls :\n' + spa.url + ' no found - 404'

    f.close()
except:
   print ("usage: %s https://www.chinabaiker.com/ php(asp,aspx,jsp,file.txt)" % sys.argv[0])
