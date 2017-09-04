#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'

import requests

class CrawlUtil(object):
    def __init__(self):
        self.s = requests.session()

    def login(self,login_url,login_data):
        res = self.s.post(login_url,login_data)
        return res.status_code

    def crawl_json_data(self,crawl_url,post_data):
        res = self.s.post(crawl_url,post_data)
        # print res.text
        # print res.json()
        return res.json()

    def crawl_text_data(self,crawl_url,post_data):
        res = self.s.post(crawl_url,post_data)
        print res.text
        return res.text

    def get_data(self,crawl_url,request_data):
        res = self.s.get(crawl_url,params=request_data)
        print res.content
        # return res.json()
        return res.text


    def get_data_with_header(self,crawl_url,headers_info):
        res = self.s.get(crawl_url,headers=headers_info)
        print res
        # return res.json()
        res_dic = {}
        res_dic['data'] = res.content
        res_dic['status_code'] = res.status_code
        return res_dic

if __name__ == '__main__':


    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'__jsluid=b03eda058b972ee78117931728347242; PHPSESSID=i25qqs661eqmj1fb9771qu80g7; sYQDUGqqzHsearch_history=%u8D77%u8BC9%u4E66%7C; __jsl_clearance=1502180960.679|0|mCVhEFoCpL%2B8ioUK55i9h47Vq88%3D; Hm_lvt_2e64cf4f6ff9f8ccbe097650c83d719e=1502099288; Hm_lpvt_2e64cf4f6ff9f8ccbe097650c83d719e=1502180968; sYQDUGqqzHpid=page_0; sYQDUGqqzHtid=tab_0',
        'Host':'www.ajxxgk.jcy.gov.cn',
        'If-Modified-Since':'Mon, 07 Aug 2017 09:21:20 GMT',
        'If-None-Match':'W/\"310b8f-6d6d-556265ea64acf\"',
        'Referer':'http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    }


    res = requests.session().get('http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6', headers=headers)
    print res.content




