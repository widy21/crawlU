#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import json
import sys
import os
import traceback
import util.date_util as date_util
from util.number_util import *

__author__ = 'Monkey.D.xiao'


class BIUtil(object):
    def __init__(self):
        self.result_data = {}

    def saveBiInfo(self, aaData, flag, game):

        if (flag == 'data_report'):
            result_file = open(sys.path[0] + '/result_file/%s_result_data_report.txt' % game, 'w+')
        elif (flag == 'platData'):
            result_file = open(sys.path[0] + '/result_file/%s_result_platData.txt' % game, 'w+')
        elif (flag == 'channelData'):
            result_file = open(sys.path[0] + '/result_file/%s_result_channelData.txt' % game, 'w+')
        elif (flag == 'serverData'):
            result_file = open(sys.path[0] + '/result_file/%s_result_serverData.txt' % game, 'w+')

        for i in aaData:
            # print str(i)
            result_file.write(json.dumps(i))
            result_file.write('\n')

        result_file.flush()
        result_file.close()

        # for i in aaData:
        # logtime = i['logtime'].encode("utf-8")
        # print 'logtime:',logtime
        #     print logtime == str(yesterday)
        #     if logtime == str(yesterday):
        #         print i.get('pay')

    def getBiInfo(self, aaData):
        yesterday = date_util.getYesterday()
        print 'yesterday:', yesterday
        for i in aaData:
            logtime = i['logtime'].encode("utf-8")
            print 'logtime:', logtime
            print logtime == str(yesterday)
            if logtime == str(yesterday):
                print i.get('pay')

        return self.result_data

    def getBiInfoFromDisk(self, game,biVo):
        result_file = file(sys.path[0] + '/result_file/%s_result_data_report.txt' % game, 'r+')
        for i in result_file.readlines():
            jo = json.loads(i)
            try:
                self.organizeBiData(jo,biVo)
            except Exception as e:
                print 'bi_util组织数据失败...\n'
                print traceback.format_exc()
                return

        result_file.close()
        print '基本数据统计完成...'

        try:
            # 统计环比、同比数据
            self.calculateMoMData(biVo)

            # 统计运营数据
            self.statisticsOperateData(game,biVo)
        except Exception as e:
            print 'bi_util统计环比、同比、运营数据失败...\n'
            print traceback.format_exc()
            return

        #保存统计结果

        #windows路径
        # if not os.path.exists(sys.path[0] + '/result_file/bi_data_%s'%date_util.getToday()):
        #     os.makedirs(sys.path[0] + '/result_file/bi_data_%s'%date_util.getToday())
        #
        # result_BI_file = open(sys.path[0] + '/result_file/bi_data_%s/%s_result_BI.txt' % (date_util.getToday(),game), 'w+')

        #linux服务器路径
        if not os.path.exists('/export/bi/result_file/bi_data_%s'%date_util.getToday()):
            os.makedirs('/export/bi/result_file/bi_data_%s'%date_util.getToday())

        result_BI_file = open('/export/bi/result_file/bi_data_%s/%s_result_BI.txt' % (date_util.getToday(),game), 'w+')

        result_dic = {
            'bi_dic': {
                'data_report': biVo.data_report,
                'added_data': biVo.added_data,
                'added_user_data': biVo.added_user_data,
                'active_data': biVo.active_data,
                'retained_data': biVo.retained_data,
                'PCU_data': biVo.PCU_data,
                'income_data': biVo.income_data,
                'plat_data': biVo.plat_data,
                'server_data': biVo.server_data,
                'channel_data': biVo.channel_data,
                'online_data': biVo.online_data
            }
        }

        #重置文件编码，由ascii编码改为utf-8，防止保存文件出错。
        reload(sys)
        sys.setdefaultencoding('utf-8')

        #保存结果
        result_BI_file.write(json.dumps(result_dic, ensure_ascii=False, indent=2, sort_keys=True))
        result_BI_file.write('\n')

        result_BI_file.flush()
        result_BI_file.close()

    def organizeBiData(self, file_data,biVo):
        yesterday = date_util.getYesterday()
        dayBeforeYestoday = date_util.getBeforDay(2)
        logtime = file_data['logtime']

        # 统计当日(实际上是昨日)数据
        if logtime == str(yesterday):
            # print 'logtime:',logtime
            biVo.data_report['current_day_charge'] = file_data['pay']
            biVo.added_data['current_day_added'] = file_data['newadd']
            biVo.added_user_data['current_day_added'] = file_data['newuser']
            biVo.active_data['current_day_active'] = file_data['login']
            biVo.PCU_data['current_day_pcu'] = file_data['pcu']
            biVo.income_data['pay_accont_num'] = file_data['payacc']
            biVo.income_data['pay_rate'] = file_data['payrate']
            biVo.income_data['pay_ARPU'] = file_data['payarpu']
            biVo.online_data['average_online_time'] = file_data['gametime']
            biVo.online_data['ACU'] = file_data['acu']

        # 统计昨日(实际上是前日)数据
        if logtime == str(dayBeforeYestoday):
            biVo.retained_data['following_day_retained'] = file_data['crlcl']*100
            biVo.income_data['last_day_pay_ARPU'] = file_data['payarpu']

        #统计前8日数据
        before8Date_list = date_util.getBefore8DayDate()
        if logtime in ','.join(before8Date_list):
            biVo.data_report['8day_charge'][logtime] = file_data['pay']
            biVo.added_data['8day_added'][logtime] = file_data['newadd']
            biVo.added_user_data['8day_added'][logtime] = file_data['newuser']
            biVo.active_data['8day_active'][logtime] = file_data['login']
            biVo.PCU_data['8day_pcu'][logtime] = file_data['pcu']
            biVo.income_data['8day_pay_acc'][logtime] = file_data['payacc']
            biVo.income_data['8day_pay_rate'][logtime] = file_data['payrate']
            biVo.online_data['8day_acu'][logtime] = file_data['acu']
            biVo.online_data['8day_average_online_time'][logtime] = file_data['gametime']

        #统计前7日留存数据
        remainedBefore8dayDate_list = date_util.getRemainedBefore8DayDate()
        if logtime in ','.join(remainedBefore8dayDate_list):
            biVo.retained_data['8day_retained'][logtime] = file_data['crlcl']*100

        ##保存10日(第一页)数据
        biVo.data_report['10day_data'][logtime] = file_data['pay']
        biVo.added_data['10day_data'][logtime] = file_data['newadd']
        biVo.added_user_data['10day_data'][logtime] = file_data['newuser']
        biVo.active_data['10day_data'][logtime] = file_data['login']
        biVo.PCU_data['10day_data'][logtime] = file_data['pcu']
        biVo.retained_data['10day_data'][logtime] = file_data['crlcl']*100
        biVo.income_data['10day_data'][logtime] = file_data['payacc']

    def calculateMoMData(self,biVo):
        # 1、获取统计日期
        # 昨日
        yesterday = date_util.getYesterday()
        # 前日
        dayBeforeYestoday = date_util.getBeforDay(2)
        #上周同日
        lastWeekday = date_util.getBeforDay(8)

        #次留前日
        remainedDayBeforeYestoday = date_util.getBeforDay(3)
        #次留上周同日
        remainedLastWeekday = date_util.getBeforDay(9)

        # 2、统计昨日环比数据:

        #充值
        mom_data = self.getYestodayMomData(biVo.data_report['8day_charge'][str(yesterday)],
                                           biVo.data_report['8day_charge'][str(dayBeforeYestoday)])
        biVo.data_report['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #新增(角色)
        mom_data = self.getYestodayMomData(biVo.added_data['8day_added'][str(yesterday)],
                                           biVo.added_data['8day_added'][str(dayBeforeYestoday)])
        biVo.added_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #新增（账号）
        mom_data = self.getYestodayMomData(biVo.added_user_data['8day_added'][str(yesterday)],
                                           biVo.added_user_data['8day_added'][str(dayBeforeYestoday)])
        biVo.added_user_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #活跃
        mom_data = self.getYestodayMomData(biVo.active_data['8day_active'][str(yesterday)],
                                           biVo.active_data['8day_active'][str(dayBeforeYestoday)])
        biVo.active_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #PCU
        mom_data = self.getYestodayMomData(biVo.PCU_data['8day_pcu'][str(yesterday)],
                                           biVo.PCU_data['8day_pcu'][str(dayBeforeYestoday)])
        biVo.PCU_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #留存
        mom_data = self.getYestodayMomData(biVo.retained_data['8day_retained'][str(dayBeforeYestoday)],
                                           biVo.retained_data['8day_retained'][str(remainedDayBeforeYestoday)])
        biVo.retained_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #收入-付费账号
        mom_data = self.getYestodayMomData(biVo.income_data['8day_pay_acc'][str(yesterday)],
                                           biVo.income_data['8day_pay_acc'][str(dayBeforeYestoday)])
        biVo.income_data['yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #收入-付费率
        mom_data = self.getYestodayMomData(biVo.income_data['8day_pay_rate'][str(yesterday)],
                                           biVo.income_data['8day_pay_rate'][str(dayBeforeYestoday)])
        biVo.income_data['pay_rate_yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #在线-acu
        mom_data = self.getYestodayMomData(biVo.online_data['8day_acu'][str(yesterday)],
                                           biVo.online_data['8day_acu'][str(dayBeforeYestoday)])
        biVo.online_data['acu_yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'
        #在线-平均在线时长
        mom_data = self.getYestodayMomData(biVo.online_data['8day_average_online_time'][str(yesterday)],
                                           biVo.online_data['8day_average_online_time'][str(dayBeforeYestoday)])
        biVo.online_data['average_online_time_yestoday_mom'] = getFloatNumber(mom_data*100,2)+'%'


        # 3、统计上周同比数据:

        #充值
        yoy_data = self.getLastWeekYoyData(biVo.data_report['10day_data'][str(yesterday)],
                                           biVo.data_report['10day_data'][str(lastWeekday)])
        biVo.data_report['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'
        #新增（角色）
        yoy_data = self.getLastWeekYoyData(biVo.added_data['10day_data'][str(yesterday)],
                                           biVo.added_data['10day_data'][str(lastWeekday)])
        biVo.added_data['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'
        #新增（账号）
        yoy_data = self.getLastWeekYoyData(biVo.added_user_data['10day_data'][str(yesterday)],
                                           biVo.added_user_data['10day_data'][str(lastWeekday)])
        biVo.added_user_data['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'
        #活跃
        yoy_data = self.getLastWeekYoyData(biVo.active_data['10day_data'][str(yesterday)],
                                           biVo.active_data['10day_data'][str(lastWeekday)])
        biVo.active_data['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'
        #PCU
        yoy_data = self.getLastWeekYoyData(biVo.PCU_data['10day_data'][str(yesterday)],
                                           biVo.PCU_data['10day_data'][str(lastWeekday)])
        biVo.PCU_data['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'
        #留存@留存不需要统计环比同比数据
        # yoy_data = self.getLastWeekYoyData(biVo.retained_data['10day_data'][str(dayBeforeYestoday)],
        #                                    biVo.retained_data['10day_data'][str(remainedDayBeforeYestoday)])
        # biVo.retained_data['last_week_yoy'] = yoy_data

        #收入-付费账号
        yoy_data = self.getLastWeekYoyData(biVo.income_data['10day_data'][str(yesterday)],
                                           biVo.income_data['10day_data'][str(lastWeekday)])
        biVo.income_data['last_week_yoy'] = getFloatNumber(yoy_data*100,2)+'%'

    # 统计昨日环比数据
    def getYestodayMomData(self, yesterday_data, dayBeforeYestoday_data):
        if yesterday_data == None or yesterday_data == 0 or dayBeforeYestoday_data == None or dayBeforeYestoday_data == 0:
            print 'getMomData has none data'
            return 0
        else:
            # 昨日环比 : abs（昨天数据-前天数据）/前天数据
            return (float(yesterday_data) - float(dayBeforeYestoday_data)) / float(dayBeforeYestoday_data)

    # 统计上周同比数据
    def getLastWeekYoyData(self, yesterday_data, lastWeekday):
        if yesterday_data == None or yesterday_data == 0 or lastWeekday == None or lastWeekday == 0:
            print 'getLastWeekYoyData has none data'
            return 0
        else:
            # 上周同比 : abs（昨天数据-上周同日数据））/上周同日数据）
            return (float(yesterday_data) - int(lastWeekday)) / float(lastWeekday)

    def statisticsOperateData(self, game,biVo):
        # 平台
        plat_file = file(sys.path[0] + '/result_file/%s_result_platData.txt' % game, 'r+')
        for i in plat_file.readlines():
            jo = json.loads(i)
            os = jo['os']
            payment = jo['payment']
            biVo.plat_data.append({'os': os, 'payment': payment})
        plat_file.close()
        print '平台数据统计完成...'

        # 渠道
        channel_file = file(sys.path[0] + '/result_file/%s_result_channelData.txt' % game, 'r+')
        for i in channel_file.readlines():
            jo = json.loads(i)
            platform = jo['platform']
            payment = jo['payment']
            biVo.channel_data.append({'platform': platform, 'payment': payment})
        channel_file.close()
        print '渠道数据统计完成...'

        #区服
        server_file = file(sys.path[0] + '/result_file/%s_result_serverData.txt' % game, 'r+')
        for i in server_file.readlines():
            jo = json.loads(i)
            groupname = jo['groupname']
            payment = jo['payment']
            biVo.server_data.append({'groupname': groupname, 'payment': payment})
        server_file.close()
        print '区服数据统计完成...'

    def getAllGame(self):
        ret = []
        ret.append('ahlm')
        ret.append('sd')
        ret.append('moli')
        ret.append('sdsyd')
        return ret

    def inred(self,s):
        return "%s[44;2m%s%s[0m"%(chr(27), s, chr(27))
