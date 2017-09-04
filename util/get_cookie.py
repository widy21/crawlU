__author__ = 'Administrator'
from selenium import webdriver

def get_cookie():
    driver = webdriver.Chrome("/Users/huaxiao/Downloads/chromedriver")
    driver.get("http://www.ajxxgk.jcy.gov.cn/html/index.html")
    c =driver.get_cookies()
    cl = []
    for cookie in c:
        print cookie['name'],'-->',cookie['value']
        if(cookie['name'] == '__jsluid' or cookie['name'] == '__jsl_clearance'):
            cl.append(cookie['name']+"="+cookie['value'])
    f = open('cookies.txt','w+')
    print ';'.join(cl)
    f.write(';'.join(cl))
    f.close()
    driver.close()
    return ';'.join(cl)