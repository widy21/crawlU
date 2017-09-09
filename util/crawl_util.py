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
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "Cookie":"__jsl_clearance=1504966913.336|0|dZVeCwMNZC%2FCaT0w5wLzpqf6IgA%3D; __jsluid=7d10b9d772d982dfbcda279fca44c2ff",
        "Host":"www.ajxxgk.jcy.gov.cn",
        "Pragma":"no-cache",
        "Referer":"http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6&page=1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    }


    s = requests.session();
    #s.cookies.set('__jsluid','b635d57aac832ae2965dc0f0b9e08e6d');
    #s.cookies.set('__jsl_clearance','1504936895.309|0|vBoZIhocTd%2Bx6Mgbwj4dTwC4IRE%3D');
    res = s.get('http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6', headers=headers)
    print res




