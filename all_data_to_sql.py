'''
@Description: 获取某只证券所有数据并写入数据库
@Author: 石门菜鸡
@Date: 2019-10-18 15:11:34
@LastEditTime: 2019-10-19 08:32:32
@LastEditors: Please set LastEditors
'''

import datetime
import MySQLdb

import get_stock_k_data
import stock_data_to_mysql
import get_dividend_data
import get_profit_data
import get_operation_data
import get_growth_data
import get_balance_data
import get_cash_flow_data
import get_dupont_data
import get_forecast_report_data
import get_basic_data
import get_index_stock
import get_performance_express_data


def all_data_to_sql(stock_code,stock_name):
    #开始日期，默认为2006-1-1，baostock平台只有该日期后的数据
    start_date='2006-1-1'
    #截止日期，默认为今日
    end_date=datetime.date.today().strftime('%Y-%m-%d')
    #开始年份，默认为2006
    start_year='2006'
    #截至年份，默认为今年
    end_year=datetime.date.today().strftime('%Y')
    #股票代码
    #stock_code='sz.300294'
    #股票名称
    #stock_name='博雅生物'
    #获取数据频率
    frequency='d'
    #复权标志
    adjustflag='2'
    #年份类别，默认为"report":预案公告年份，可选项"operate":除权除息年份。
    year_type='report'

    #数据库名称，默认为baostock
    database_name='zz_500'
    #写入数据库模式，默认为append。 三个模式：fail，若表存在，则不输出；replace：若表存在，覆盖原来表里的数据；append：若表存在，将数据写到原表的后面。默认为fail
    mode='replace'

    #######交易数据######
    print("------------处理交易数据...------------")
    stock_trade_result=get_stock_k_data.get_stock_data(stock_code,stock_name,start_date,end_date,frequency,adjustflag)
    table_name=stock_code+'_'+'trade'
    stock_data_to_mysql.write_data_to_database(stock_trade_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######分红数据######
    print("------------处理分红数据...------------")
    dividend_query_result=get_dividend_data.get_dividend_data(stock_code,stock_name,int(start_year),int(end_year),year_type)
    table_name=stock_code+'_'+'dividend'
    stock_data_to_mysql.write_data_to_database(dividend_query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######盈利数据######
    print("------------处理盈利数据...------------")
    query_result=get_profit_data.get_profit_data_year(stock_code,stock_name,start_year,end_year)
    table_name=stock_code+'_'+'profit'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######经营数据######
    print("------------处理经营数据...------------")
    query_result=get_operation_data.get_operation_data_year(stock_code,stock_name,start_year,end_year)
    table_name=stock_code+'_'+'operation'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######偿债能力数据######
    print("------------处理偿债能力数据...------------")
    query_result=get_balance_data.get_balance_data_year(stock_code,stock_name,start_year,end_year)
    table_name=stock_code+'_'+'balance'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######现金流量数据######
    print("------------处理现金流量数据...------------")
    query_result=get_cash_flow_data.get_cash_flow_data_year(stock_code,stock_name,start_year,end_year)
    table_name=stock_code+'_'+'cash_flow'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######杜邦数据######
    print("------------处理杜邦数据...------------")
    query_result=get_dupont_data.get_dupont_data_year(stock_code,stock_name,start_year,end_year)
    table_name=stock_code+'_'+'dupont'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")

    #######业绩快报######
    print("------------处理业绩快报...------------")
    query_result=get_performance_express_data.get_performance_express_data(stock_code,stock_name,start_date,end_date)
    table_name=stock_code+'_'+'performance_express'
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    print("------------处理完成------------")


def main():
    # all_data_to_sql('sh.600276','恒瑞医药')
    db = MySQLdb.connect("localhost", "root", "891219", "baostock", charset='utf8')
    cursor=db.cursor()
    sql="SELECT * FROM zz500_stocks_copy1"
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            #print(row[1]+" "+row[2])
            all_data_to_sql(row[1],row[2])
    except:
        f=open('D:/test.txt','a+')
        f.write('\n indata error '+row[1])
        f.close()
        print ("Error: Unable to fetch data")
        pass
    db.close()

if __name__ == '__main__':
    main()