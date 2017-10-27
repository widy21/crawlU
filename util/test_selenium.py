# -*- coding: utf-8 -*-
import time
#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys

__author__ = 'Administrator'
from selenium import webdriver

def get_cookie():
    driver = webdriver.Chrome("D:/chromedriver.exe")
    driver.get("http://www.ajxxgk.jcy.gov.cn/index.php?m=search")
    time.sleep(5)
    elem_pwd = driver.find_element_by_id("q")
    str = unicode('起诉书',encoding='utf-8', errors='ignore')
    elem_pwd.send_keys(str)
    elem_pwd.send_keys(Keys.RETURN)
    print driver.find_element_by_class_name('title').get_attribute('a').text;


    time.sleep(15)
    # driver.close()

if __name__ == '__main__':
    get_cookie();