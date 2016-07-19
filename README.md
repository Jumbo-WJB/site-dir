site dir 
simple python


使用方法:


dir.py https://www.chinabaiker.com/ php(asp,aspx,jsp,file.txt)



比如


python dir.py https://www.chinabaiker.com/ php

python dir.py https://www.chinabaiker.com/ asp

python dir.py https://www.chinabaiker.com/ aspx


python dir.py https://www.chinabaiker.com/ jsp

python dir.py https://www.chinabaiker.com/ file.txt（file.txt为你自定义的字典名）



url一定要是完整形式的url，http://www.chinabaiker.com/  http（s）不可少，最后面的/不可少！！


error.txt放错误关键词，比如有的网站自定义404页面了，访问一个不存在的页面都会跳到一个自定也的404页面，那比如music.163.com，访问http://music.163.com/adadsadada会跳到http://music.163.com/#/404页面，平常扫描器也会把这个页面误报成200，如果在error.txt写上“很抱歉”，那如果当前页面状态是200，但是存在“很抱歉”字样的话，则不写入success.txt中，可以在一定范围内解决误报。
