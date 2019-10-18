'''
@Description: 测试脚本
@Author: 石门菜鸡
@Date: 2019-10-18 15:11:34
@LastEditTime: 2019-10-18 20:22:19
@LastEditors: Please set LastEditors
'''
import get_stock_k_data
import stock_data_to_mysql
import get_dividend_data
import get_profit_data
import get_operation_data
import get_growth_data
import get_balance_data
import get_cash_flow_data
import get_dupont_data
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

'''
@description: 单季度利润数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def profit_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    profit_query_result=get_profit_data.get_profit_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'profit'
    mode='append'

    stock_data_to_mysql.write_data_to_database(profit_query_result,database_name,table_name,mode)

    return

'''
@description: 数年利润数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def profit_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    profit_query_result=get_profit_data.get_profit_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'profit'
    mode='append'
    
    for rs in profit_query_result:
        stock_data_to_mysql.write_data_to_database(rs,database_name,table_name,mode)
    
    return

'''
@description: 单季度经营数据提取并保存至数据库
@param {type} 
@return: 
'''
def operation_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    operation_query_result=get_operation_data.get_operation_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'operation'
    mode='append'

    stock_data_to_mysql.write_data_to_database(operation_query_result,database_name,table_name,mode)

    return

'''
@description: 数年经营数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def operation_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    operation_query_result=get_operation_data.get_operation_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'operation'
    mode='append'
    
    for rs in operation_query_result:
        stock_data_to_mysql.write_data_to_database(rs,database_name,table_name,mode)
    
    return

'''
@description: 单季度经营数据提取并保存至数据库
@param {type} 
@return: 
'''
def growth_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    query_result=get_growth_data.get_growth_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'growth'
    mode='append'

    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)

    return

'''
@description: 数年经营数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def growth_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    query_result=get_growth_data.get_growth_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'growth'
    mode='append'
    
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    
    return

'''
@description: 单季度偿债能力数据提取并保存至数据库
@param {type} 
@return: 
'''
def balance_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    query_result=get_balance_data.get_balance_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'balance'
    mode='append'

    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)

    return

'''
@description: 数年偿债能力数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def balance_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    query_result=get_balance_data.get_balance_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'balance'
    mode='append'
    
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    
    return

    '''
@description: 单季度现金流量数据提取并保存至数据库
@param {type} 
@return: 
'''
def cash_flow_data_single_quarter_to_mysql():
    stock_code='sh.601717'
    stock_name='郑煤机'
    year=2018
    quarter=1

    query_result=get_cash_flow_data.get_cash_flow_data(stock_code,stock_name,year,quarter)

    database_name='baostock'
    table_name=stock_code+'_'+'cash_flow'
    mode='append'

    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)

    return

'''
@description: 数年现金流量数据提取并写入数据库测试脚本
@param {type} 
@return: 
'''
def cash_flow_data_years_to_mysql():
    start_year='2009'
    end_year='2019'
    stock_code='sh.601717'
    stock_name='郑煤机'

    query_result=get_cash_flow_data.get_cash_flow_data_year(stock_code,stock_name,start_year,end_year)

    database_name='baostock'
    table_name=stock_code+'_'+'cash_flow'
    mode='append'
    
    stock_data_to_mysql.write_data_to_database(query_result,database_name,table_name,mode)
    
    return
#dividend_data_to_mysql()
#profit_data_single_quarter_to_mysql()
#profit_data_years_to_mysql()
#operation_data_single_quarter_to_mysql()
#growth_data_single_quarter_to_mysql()
#growth_data_years_to_mysql()
cash_flow_data_years_to_mysql()
#print('this message is from main function')