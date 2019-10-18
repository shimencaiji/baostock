'''
@Description: 查询市场交易、股票基本信息
@Author: 石门菜鸡
@Date: 2019-10-18 18:12:14
@LastEditTime: 2019-10-18 22:20:09
@LastEditors: Please set LastEditors
'''
import baostock as bs
import pandas as pd

'''
@description: 获取指定时间段所有交易日
@param {start_date：开始日期，str类型
        end_date：截至日期，str类型} 
@return: 
'''
def get_trade_dates(start_date,end_date):
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取交易日信息 ####
    rs = bs.query_trade_dates(start_date, end_date)
    print('query_trade_dates respond error_code:'+rs.error_code)
    print('query_trade_dates respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    bs.logout()
    return result

'''
@description: 获取指定日期节点所有证券
@param {date：指定日期，str类型}} 
@return: 
'''
def get_all_stocks(date):
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取证券信息 ####
    rs = bs.query_all_stock(date)
    print('query_all_stock respond error_code:'+rs.error_code)
    print('query_all_stock respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    bs.logout()
    return result

'''
@description: 获取证券基本信息
@param {stock_code:证券代码，str类型}} 
@return: 
'''
def get_stock_basic_message(stock_code):
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取证券基本资料
    rs = bs.query_stock_basic(code=stock_code)
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    print('query_stock_basic respond error_code:'+rs.error_code)
    print('query_stock_basic respond  error_msg:'+rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    bs.logout()
    return result
'''
@description: 获取证券所属行业
@param {stock_code:证券代码，str类型}} 
@return: 
'''
def get_stock_industry(stock_code):
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取证券基本资料
    rs = bs.query_stock_industry(code=stock_code)
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    print('query_stock_industry respond error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    bs.logout()
    return result