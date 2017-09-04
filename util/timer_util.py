#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'
from threading import Timer
from util import date_util

def executeEvery(seconds,callback):
    def f():
        print '=============',date_util.getNow(),'================='
        callback()
        t = Timer(seconds,f)
        t.start()
    def stop():
        t.cancel()

    t = Timer(seconds,f)
    t.start()

    return stop