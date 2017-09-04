#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'

from decimal import *


def getFloatNumber(origin_number,round_format_num):

    if origin_number == 0:
        return '0'

    ret = origin_number
    length=len(str(origin_number)[str(origin_number).find('.'):])
    if length>=round_format_num:
        getcontext().rounding = ROUND_HALF_UP
        ret = '{:.2f}'.format(Decimal(origin_number))

    # print ret

    return ret