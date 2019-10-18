'''
@Description: 测试脚本
@Author: 石门菜鸡
@Date: 2019-10-18 15:11:34
@LastEditTime: 2019-10-18 17:08:59
@LastEditors: Please set LastEditors
'''
import get_stock_k_data
import stock_data_to_mysql
import get_dividend_data
'''
@description:交易数据提取并写入数据库测试脚本 
@param {type} 
@return: 
'''
def stock_k_data_to_mysql():
    start_day='2019-10-10'
    end_day='2019-10-16'
    stock_code='sh.601717'
    stock_name='郑煤机'
    frequency='d'
    adjustflag='3'

    stock_trade_result=get_stock_k_data.get_stock_data(stock_code,stock_name,start_day,end_day,frequency,adjustflag)

    database_name='baostock'
    table_name=stock_code+stock_name
    mode='append'

    stock_data_to_mysql.write_data_to_database(stock_trade_result,database_name,table_name,mode)
'''
@description: 分红数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def dividend_data_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'
    year_type='report'

    dividend_query_result=get_dividend_data.get_dividend_data(stock_code,stock_name,int(start_year),int(end_year),year_type)

    database_name='baostock'
    table_name=stock_code+'_'+'dividend'
    mode='append'

    stock_data_to_mysql.write_data_to_database(dividend_query_result,database_name,table_name,mode)


def main():
    dividend_data_to_mysql()
    print('this message is from main function')


if __name__ == '__main__':
    main()