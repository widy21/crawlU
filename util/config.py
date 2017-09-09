#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'

#抓取地址:

#数据报表
crawl_url = 'http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6&page='

#抓取时请求头信息
header_info = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Cookie":"",
    "Host":"www.ajxxgk.jcy.gov.cn",
    "Pragma":"no-cache",
    "Referer":"http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&siteid=1&q=%E8%B5%B7%E8%AF%89%E4%B9%A6&page=1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
}

#请求数据
payload = {
    'dt_json':"[{\"name\":\"sEcho\",\"value\":1},{\"name\":\"iColumns\",\"value\":19},{\"name\":\"sColumns\",\"value\":\"\"},{\"name\":\"iDisplayStart\",\"value\":0},{\"name\":\"iDisplayLength\",\"value\":10},{\"name\":\"mDataProp_0\",\"value\":\"logtime\"},{\"name\":\"mDataProp_1\",\"value\":\"os\"},{\"name\":\"mDataProp_2\",\"value\":\"newuser\"},{\"name\":\"mDataProp_3\",\"value\":\"newadd\"},{\"name\":\"mDataProp_4\",\"value\":\"crlcl\"},{\"name\":\"mDataProp_5\",\"value\":\"lcl3\"},{\"name\":\"mDataProp_6\",\"value\":\"lcl7\"},{\"name\":\"mDataProp_7\",\"value\":\"acu\"},{\"name\":\"mDataProp_8\",\"value\":\"pcu\"},{\"name\":\"mDataProp_9\",\"value\":\"loginacc\"},{\"name\":\"mDataProp_10\",\"value\":\"login\"},{\"name\":\"mDataProp_11\",\"value\":\"gametime\"},{\"name\":\"mDataProp_12\",\"value\":\"gametimes\"},{\"name\":\"mDataProp_13\",\"value\":\"payacc\"},{\"name\":\"mDataProp_14\",\"value\":\"newpaycount\"},{\"name\":\"mDataProp_15\",\"value\":\"payrate\"},{\"name\":\"mDataProp_16\",\"value\":\"payarpu\"},{\"name\":\"mDataProp_17\",\"value\":\"loginarpu\"},{\"name\":\"mDataProp_18\",\"value\":\"pay\"},{\"name\":\"iSortCol_0\",\"value\":0},{\"name\":\"sSortDir_0\",\"value\":\"asc\"},{\"name\":\"iSortingCols\",\"value\":1},{\"name\":\"bSortable_0\",\"value\":true},{\"name\":\"bSortable_1\",\"value\":true},{\"name\":\"bSortable_2\",\"value\":true},{\"name\":\"bSortable_3\",\"value\":true},{\"name\":\"bSortable_4\",\"value\":true},{\"name\":\"bSortable_5\",\"value\":true},{\"name\":\"bSortable_6\",\"value\":true},{\"name\":\"bSortable_7\",\"value\":true},{\"name\":\"bSortable_8\",\"value\":true},{\"name\":\"bSortable_9\",\"value\":true},{\"name\":\"bSortable_10\",\"value\":true},{\"name\":\"bSortable_11\",\"value\":true},{\"name\":\"bSortable_12\",\"value\":true},{\"name\":\"bSortable_13\",\"value\":true},{\"name\":\"bSortable_14\",\"value\":true},{\"name\":\"bSortable_15\",\"value\":true},{\"name\":\"bSortable_16\",\"value\":true},{\"name\":\"bSortable_17\",\"value\":true},{\"name\":\"bSortable_18\",\"value\":true},{\"name\":\"start\",\"value\":\"start_day\"},{\"name\":\"end\",\"value\":\"end_day\"},{\"name\":\"ostype\",\"value\":\"-1\"},{\"name\":\"type\",\"value\":\"1\"},{\"name\":\"varTargets\",\"value\":\"\"}]"
}
