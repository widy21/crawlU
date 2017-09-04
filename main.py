#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'hua.xiao'

import util.config as cf
from util.crawl_util import CrawlUtil
import util.get_cookie as cookie_util
import requests
from pyquery import PyQuery as pq
import util.date_util as du
import os,sys

def get_new_cookie():
    cookies = cookie_util.get_cookie()
    return cookies

def export_file(res_data,file_format):
    doc=pq(res_data)
    data=doc('ul.wrap li')
    for i in data:
        temp_url = 'http://www.ajxxgk.jcy.gov.cn'+pq(i).find('a').attr('href')
        temp_ret_data = crawlUtil.get_data_with_header(temp_url,cf.header_info)['data']
        temp_doc=pq(temp_ret_data)
        temp_data=temp_doc('#contentArea')
        title=temp_doc('title').text()
        # title = temp_data.find('span[name=\'title\']>span:eq(0)').text()+\
        #         temp_data.find('span[name=\'title\']>span:eq(1)').text()
        print title.split('-')[0]
        content = temp_data.find('p:gt(4)')
        file_name = title+'_'+str(du.getNow())
        f = open(sys.path[0] + '/result_file/%s.%s' % (file_name,file_format), 'w+')
        for j in content:
            f.write(pq(j).text().encode('utf-8'))
            f.write('\n')
        f.close()
        print '====================================='

if __name__ == '__main__':

    print '请输入爬取页数和导出文件格式.'
    page = raw_input('爬取页数 : ')
    file_format = raw_input('文件格式 : ')
    if not all([page,file_format]):
        print '输入内容错误...'
        sys.exit()

    crawlUtil = CrawlUtil()
    url = cf.crawl_url+page
    #组织cookie
    f = open('cookies.txt','r+')
    cookies = f.readline()
    headers = cf.header_info
    headers['Cookie'] = cookies

    res_dic = crawlUtil.get_data_with_header(url,headers)
    res_data = res_dic['data']
    print res_dic['status_code']

    if res_dic['status_code'] != requests.codes.ok:
        print 'login false,result_code --> ', res_dic['status_code']
        headers = cf.header_info
        cookies = get_new_cookie()
        headers['Cookie'] = cookies
        print headers

        res_dic = crawlUtil.get_data_with_header(cf.crawl_url,headers)
        res_data = res_dic['data']

    export_file(res_data,file_format)
    # print res_data