#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'hua.xiao'
import requests
from util.crawl_util import CrawlUtil


header_info = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'__jsluid=e95ffa92ca9bede37e8f57c36ae34416; PHPSESSID=i25qqs661eqmj1fb9771qu80g7; sYQDUGqqzHsearch_history=%u8D77%u8BC9%u4E66%7C; __jsl_clearance=1502196063.752|0|TqS7xA2G0%2BW5fMgDvj0z%2FbwLtUY%3D; Hm_lvt_2e64cf4f6ff9f8ccbe097650c83d719e=1502099288; Hm_lpvt_2e64cf4f6ff9f8ccbe097650c83d719e=1502196065; sYQDUGqqzHpid=page_0; sYQDUGqqzHtid=tab_0',
    'Host':'www.ajxxgk.jcy.gov.cn',
    # 'If-Modified-Since':'Mon, 07 Aug 2017 09:21:20 GMT',
    # 'If-None-Match':'W/\"310b8f-6d6d-556265ea64acf\"',
    'Referer':'http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

# resp = requests.get(url = 'http://www.ajxxgk.jcy.gov.cn/html/index.html',headers=header_info)
resp = requests.get(url = 'http://www.ajxxgk.jcy.gov.cn/html/index.html')
print resp
# print 'resp', resp.cookies._cookies
# print 'req',  resp.request._cookies._cookies
print {c.name: c.value for c in resp.cookies}