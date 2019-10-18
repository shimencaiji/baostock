'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 15:11:34
@LastEditTime: 2019-10-18 15:25:51
@LastEditors: Please set LastEditors
'''
import get_stock_k_data
import stock_data_to_mysql

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