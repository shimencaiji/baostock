'''
@Description: 从baostock获取股票除权除息信息数据（预披露、预案、正式都已通过）。
@Author: 石门菜鸡
@Date: 2019-10-18 15:38:07
@LastEditTime: 2019-10-18 16:37:20
@LastEditors: Please set LastEditors
'''
import baostock as bs
import pandas as pd

'''
@description: 查询除权除息信息
@param {stock_number:股票代码
        stock_name:股票名称
        start_year:查询起始年度,int类型
        end_year:查询截至年度
        yearType:年份类别，默认为"report":预案公告年份，可选项"operate":除权除息年份。
        } 
@return: 
'''
def get_dividend_data(stock_number,stock_name,start_year,end_year,yearType):

    print('==========================================================')
    print("开始进行: "+stock_name+"("+stock_number+")"+"的数据处理")
    print("尝试登陆baostock")
    #####login#####
    lg=bs.login(user_id="anonymous",password="123456")
    if(lg.error_code == '0'):
          print("登陆成功")
    else:
          print("登录失败")

    rs_list=[]
    for iter in range(start_year,end_year):
        rs_dividend=bs.query_dividend_data(code=stock_number,year=iter,yearType=yearType)
        while (rs_dividend.error_code == '0')& rs_dividend.next():
            rs_list.append(rs_dividend.get_row_data())
    
    bs.logout()
    return rs_list

