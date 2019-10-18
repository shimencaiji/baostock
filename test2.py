'''
@Description: 测试脚本
@Author: 石门菜鸡
@Date: 2019-10-18 15:11:34
@LastEditTime: 2019-10-18 20:50:13
@LastEditors: Please set LastEditors
'''
import get_stock_k_data
import stock_data_to_mysql
import get_dupont_data
import get_forecast_report_data

'''
@description: 单季度现金流量数据提取并保存至数据库
@param {type} 
@return: 
'''
def dupont_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    query_result=get_dupont_data.get_dupont_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'dupont'
    mode='append'

    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)

    return

'''
@description: 数年现金流量数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def dupont_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    query_result=get_dupont_data.get_dupont_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'dupont'
    mode='append'
    
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    
    return

    '''
@description: 业绩快报数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def get_forecast_data_years_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    start_date='2009-01-01'
    end_date='2019-05-25'

    query_result=get_forecast_report_data.get_forecast_report_data(stock_code,stock_name,start_date,end_date)

    database_name='baostock'
    table_name=stock_code+'_'+'perfermance_express'
    mode='append'
    
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    
    return
#dividend_data_to_mysql()
#profit_data_single_quarter_to_mysql()
#profit_data_years_to_mysql()
#operation_data_single_quarter_to_mysql()
#growth_data_single_quarter_to_mysql()
#growth_data_years_to_mysql()
#dupont_data_years_to_mysql()
get_forecast_data_years_to_mysql()
#print('this message is from main function')