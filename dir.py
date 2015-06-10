#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Author:Jumbo
Website:http://www.chinabaiker.com
'''
import requests,sys
try:
	url = sys.argv[1]
	payload = sys.argv[2]
	if not url.startswith('http://'):
		url = 'http://%s' % url
	if payload == 'php':
		for a in open('php.txt','r'):
			x = a.strip()
			sm = requests.get(str(url) + str(x))
			if sm.status_code == 200:
				print 'the urls :\n' + sm.url + ' found - 200'
			elif sm.status_code == 403:
				print 'the urls :\n' + sm.url + ' found - 403'
			elif sm.status_code == 404:
				print 'the urls :\n' + sm.url + ' no found - 404'
	elif payload == 'asp':
		for b in open('asp.txt','r'):
			y = b.strip()
			sn = requests.get(str(url) + str(x))
			if sn.status_code == 200:
				print 'the urls :\n' + sn.url + ' found - 200'
			elif sn.status_code == 403:
				print 'the urls :\n' + sn.url + ' found - 403'
			elif sn.status_code == 404:
				print 'the urls :\n' + sn.url + ' no found - 404'
	elif payload == 'jsp':
		for c in open('jsp.txt','r'):
			z = c.strip()
			so = requests.get(str(url) + str(x))
			if so.status_code == 200:
				print 'the urls :\n' + so.url + ' found - 200'
			elif so.status_code == 403:
				print 'the urls :\n' + so.url + ' found - 403'
			elif so.status_code == 404:
				print 'the urls :\n' + so.url + ' no found - 404'
	elif payload == 'aspx':
		for d in open('aspx.txt','r'):
			w = d.strip()
			sp = requests.get(str(url) + str(x))
			if sp.status_code == 200:
				print 'the urls :\n' + sm.url + ' found - 200'
			elif sp.status_code == 403:
				print 'the urls :\n' + sm.url + ' found - 403'
			elif sp.status_code == 404:
				print 'the urls :\n' + sm.url + ' no found - 404'
except:
	print ("usage: %s www.chinabaiker.com php(asp,aspx,jsp)" % sys.argv[0])
