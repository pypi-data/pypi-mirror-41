#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/2
# @Author  : beequants-nick


import pandas as pd
from qbase.common import mySql
from qbase.common import configer as cf
import logging

log = logging.getLogger()
conf = cf.configer()
klineRow = "created_date/1000 as created_date, open, high, low, close, volume, currency_volume, symbol"


def get_kline_list(symbol, period, num=None):
    db = mySql.Mysql(conf.getValueByKey("dbData", "ip"), int(conf.getValueByKey("dbData", "port")),
                     conf.getValueByKey("dbData", "userName"), conf.getValueByKey("dbData", "passwd"),
                     conf.getValueByKey("dbData", "dnName"))
    sql = "select " + klineRow + " from okex_futures_kline_%s where symbol = '" % period + symbol + "_usd' "
    sql += " order by created_date desc"
    if num is not None:
        sql += " limit %s" % num
    kline = pd.read_sql(sql, db.getDb())
    db.closeDb()
    return kline


def get_tick_kline_list(symbol, tick, period, expr=3, unit='day'):
    col_row = "t1.created_date tick_date,t1.close tick_close,t2.*,FROM_UNIXTIME(t1.created_date/1000)"
    sub_col_row = "*,created_date-created_date%(60*60*4*1000)+60*60*4*1000 tick_date"

    db = mySql.Mysql(conf.getValueByKey("dbData", "ip"), int(conf.getValueByKey("dbData", "port")),
                     conf.getValueByKey("dbData", "userName"), conf.getValueByKey("dbData", "passwd"),
                     conf.getValueByKey("dbData", "dnName"))
    
    sql = "select " + col_row + " from ( "
    sql += "SELECT "+sub_col_row+" from okex_futures_kline_%s " % tick
    sql += "where created_date > UNIX_TIMESTAMP( DATE_SUB(NOW(),INTERVAL %s %s))*1000 ) t1, " % (expr, unit)
    sql += "(SELECT * from okex_futures_kline_%s " % period
    sql += "where created_date > UNIX_TIMESTAMP( DATE_SUB(NOW(),INTERVAL %s %s))*1000 ) t2 " % (expr, unit)
    sql += "where t1.tick_date = t2.created_date "
    sql += "and t1.symbol = t2.symbol "
    sql += "and t1.symbol = '_usd' " % symbol
    sql += "ORDER BY tick_date asc "
    sql = "select " + klineRow + " from okex_futures_kline_%s where symbol = '" % period + symbol + "_usd' "
    sql += " order by created_date desc"
    kline = pd.read_sql(sql, db.getDb())
    db.closeDb()
    return kline
