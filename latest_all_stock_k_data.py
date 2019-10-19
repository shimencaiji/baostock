'''
@Description: 获取最近一个交易日所有标的交易数据并写入数据库中
@Author: 石门菜鸡
@Date: 2019-10-19 14:33:19
@LastEditTime: 2019-10-19 17:24:39
@LastEditors: Please set LastEditors
'''
import datetime
import MySQLdb

import get_stock_k_data
import get_basic_data
import stock_data_to_mysql

import pandas as pd

#获取股票信息的数据库名称
database_name_source='baostock'
#将数据保存至数据库的名称
database_name='real_time_analysis'

#需要收集信息的股票代码集合表名称
stock_set_table_name='zz500_stocks'
#指定日期的数据，其实为距离该日期最近的一个交易日
specified_date=datetime.date.today().strftime('%Y-%m-%d')
#获取数据频率
frequency='d'
#复权标志
adjustflag='2'

#写入数据库模式，默认为append。 三个模式：fail，若表存在，则不输出；replace：若表存在，覆盖原来表里的数据；append：若表存在，将数据写到原表的后面。默认为fail
mode='append'


def trade_day_judgement(specified_date):
    result=get_basic_data.get_trade_dates('2006-01-01',specified_date)
    result_check=result[result.is_trading_day=='1']
    #取交易日距离specified_date最近的一个日期
    return result_check.iloc[-1][0]

def latest_all_stock_k_data(specified_date):


    db = MySQLdb.connect("localhost", "root", "891219", database_name_source, charset='utf8')
    cursor=db.cursor()
    sql="SELECT * FROM "+stock_set_table_name
    cursor.execute(sql)
    result=cursor.fetchall()
    db.close()

    real_date=trade_day_judgement(specified_date)
    table_name=real_date+'_'+stock_set_table_name+'_'+'trade'
    stock_trade_result=pd.DataFrame()
    for r in result:
        stock_code=r[1]
        stock_name=r[2]
        tmp_result=get_stock_k_data.get_stock_data(stock_code,stock_name,real_date,real_date,frequency,adjustflag)
        stock_trade_result=pd.concat([stock_trade_result,tmp_result])
    stock_data_to_mysql.write_data_to_database(stock_trade_result,database_name,table_name,mode)

# trade_day_judgement('2006-01-15')

def main():
    latest_all_stock_k_data(specified_date)

if __name__ == '__main__':
    main()
