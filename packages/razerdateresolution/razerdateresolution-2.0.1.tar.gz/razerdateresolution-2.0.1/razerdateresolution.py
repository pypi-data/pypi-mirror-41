# -*- coding: utf-8 -*-

import datetime
from enum import Enum


class DateEnum(Enum):
    year = "year",
    month = "month",
    day = "day",
    week = "week",
    hour = "hour",
    minute = "minute",
    second = "second"


# date格式类似于3 days ago
def parse_date_str(date):
    # 解析日期字符串
    datelist = date.split(' ')
    datenum = int(datelist[0])
    delta = datetime.timedelta()
    if datelist[1].find(DateEnum['day'].name) != -1:
        delta = datetime.timedelta(days=-datenum)
    elif datelist[1].find(DateEnum['month'].name) != -1:
        delta = datetime.timedelta(days=-(datenum * 30))
    elif datelist[1].find(DateEnum['year'].name) != -1:
        delta = datetime.timedelta(days=-(datenum * 365))
    elif datelist[1].find(DateEnum['week'].name) != -1:
        delta = datetime.timedelta(weeks=-datenum)
    elif datelist[1].find(DateEnum['hour'].name) != -1:
        delta = datetime.timedelta(hours=-datenum)
    elif datelist[1].find(DateEnum['minute'].name) != -1:
        delta = datetime.timedelta(minutes=-datenum)
    elif datelist[1].find(DateEnum['second'].name) != -1:
        delta = datetime.timedelta(seconds=-datenum)

    thedate = datetime.datetime.now() + delta
    datestr = thedate.strftime('%Y-%m-%d %H:%M:%S.%f')
    totalsecs = str(thedate.timestamp())
    return datestr, totalsecs