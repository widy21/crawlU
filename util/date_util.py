#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'
import datetime, calendar

#1、返回昨天日期
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

def getToday():
    today=datetime.date.today()
    return today

#1、返回指定偏移天数之前日期
def getBeforDay(num):
    today=datetime.date.today()
    days=datetime.timedelta(days=num)
    result_day=today-days
    return result_day

def getBefore8DayDate():
    ret_list = []
    today=datetime.date.today()
    ret_list.append(str(today-datetime.timedelta(days=1)))
    ret_list.append(str(today-datetime.timedelta(days=2)))
    ret_list.append(str(today-datetime.timedelta(days=3)))
    ret_list.append(str(today-datetime.timedelta(days=4)))
    ret_list.append(str(today-datetime.timedelta(days=5)))
    ret_list.append(str(today-datetime.timedelta(days=6)))
    ret_list.append(str(today-datetime.timedelta(days=7)))
    ret_list.append(str(today-datetime.timedelta(days=8)))
    return ret_list

#获取留存前8日日期
def getRemainedBefore8DayDate():
    ret_list = []
    today=datetime.date.today()
    ret_list.append(str(today-datetime.timedelta(days=2)))
    ret_list.append(str(today-datetime.timedelta(days=3)))
    ret_list.append(str(today-datetime.timedelta(days=4)))
    ret_list.append(str(today-datetime.timedelta(days=5)))
    ret_list.append(str(today-datetime.timedelta(days=6)))
    ret_list.append(str(today-datetime.timedelta(days=7)))
    ret_list.append(str(today-datetime.timedelta(days=8)))
    ret_list.append(str(today-datetime.timedelta(days=9)))
    return ret_list

#2、返回今天日期
def getToday():
    return datetime.date.today()

#3、获取给定参数的前几天的日期，返回一个list
def getDaysByNum(num):
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    li=[]
    for i in range(0,num):
        #今天减一天，一天一天减
        today=today-oneday
        #把日期转换成字符串
        #result=datetostr(today)
        li.append(datetostr(today))
    return li

#4、将字符串转换成datetime类型
def strtodatetime(datestr,format):
    return datetime.datetime.strptime(datestr,format)

#5、时间转换成字符串,格式为2008-08-02
def datetostr(date):
    return   str(date)[0:10]

#6、两个日期相隔多少天，例：2008-10-03和2008-10-01是相隔两天
def datediff(beginDate,endDate):
    format="%Y-%m-%d";
    bd=strtodatetime(beginDate,format)
    ed=strtodatetime(endDate,format)
    oneday=datetime.timedelta(days=1)
    count=0
    while bd!=ed:
        ed=ed-oneday
        count+=1
    return count

#7、获取两个时间段的所有时间,返回list
def getDays(beginDate,endDate):
    format="%Y-%m-%d";
    bd=strtodatetime(beginDate,format)
    ed=strtodatetime(endDate,format)
    oneday=datetime.timedelta(days=1)
    num=datediff(beginDate,endDate)+1
    li=[]
    for i in range(0,num):
        li.append(datetostr(ed))
        ed=ed-oneday
    return li

#8、获取当前年份 是一个字符串
def getYear():
    return str(datetime.date.today())[0:4]

#9、获取当前月份 是一个字符串
def getMonth():
    return str(datetime.date.today())[5:7]

#10、获取当前天 是一个字符串
def getDay():
    return str(datetime.date.today())[8:10]
def getNow():
    return datetime.datetime.now()

if __name__ == '__main__':
    today = datetostr(getToday())
    print today
    print type(today)
    print getYesterday()
    print '------'
    print getBeforDay(14)
    # print getDaysByNum(3)
    # print getDays('2008-10-01','2008-10-05')
    # print '2008-10-04 00:00:00'[0:10]
    #
    # print str(getYear())+getMonth()+getDay()
    # print getToday()
    print getNow()