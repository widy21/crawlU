# -*- coding: utf-8 -*-
import time
#!/usr/bin/env python
import sys
from selenium.webdriver.common.keys import Keys
from util.crawl_util import CrawlUtil

__author__ = 'Administrator'
from selenium import webdriver


def printContent(ps):
    f = open(sys.path[0] + '/result_file/%s.%s' % (time.time(), 'txt'), 'w+')
    for p in ps:
        f.write(p.text.encode('utf-8'))
        f.write('\n')
    f.close()



def get_cookie():
    driver = webdriver.Chrome("D:/chromedriver.exe")
    driver.get("http://www.ajxxgk.jcy.gov.cn/index.php?m=search")
    time.sleep(5)
    elem_pwd = driver.find_element_by_id("q")
    str = unicode('起诉书',encoding='utf-8', errors='ignore')
    elem_pwd.send_keys(str)
    elem_pwd.send_keys(Keys.RETURN)
    # driver.implicitly_wait(20)
    print 'load over...'
    # print driver.find_element_by_class_name('title').text;
    # print  [e.get_attribute('href') for e in driver.find_elements_by_css_selector('div.title a')]
    href_list = [e.get_attribute('href') for e in driver.find_elements_by_css_selector('div.title a')]
    # driver.close()
    # driver = webdriver.Chrome("D:/chromedriver.exe")
    for href in href_list:
        # temp_url = 'http://www.ajxxgk.jcy.gov.cn' + e.get_attribute('href')
        driver.get(href)
        # driver.implicitly_wait(3)
        printContent(driver.find_elements_by_css_selector('#contentArea p'))
        # time.sleep(15)

    driver.close()


def export_file(res_data,file_format):
    doc=pq(res_data)
    data=doc('ul.wrap li')
    # for i in data:
    #     temp_url = 'http://www.ajxxgk.jcy.gov.cn'+pq(i).find('a').attr('href')
    #     temp_ret_data = crawlUtil.get_data_with_header(temp_url,cf.header_info)['data']
    #     temp_doc=pq(temp_ret_data)
    #     temp_data=temp_doc('#contentArea')
    #     title=temp_doc('title').text()
    #     # title = temp_data.find('span[name=\'title\']>span:eq(0)').text()+\
    #     #         temp_data.find('span[name=\'title\']>span:eq(1)').text()
    #     print title.split('-')[0]
    #     content = temp_data.find('p:gt(4)')
    #     file_name = title+'_'+str(du.getNow())
    #     f = open(sys.path[0] + '/result_file/%s.%s' % (file_name,file_format), 'w+')
    #     for j in content:
    #         f.write(pq(j).text().encode('utf-8'))
    #         f.write('\n')
    #     f.close()
    #     print '====================================='

if __name__ == '__main__':
    get_cookie();