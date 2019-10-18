'''
@Description: 查询季度频率企业成长性信息，提供2007年至今数据。 
@Author: 石门菜鸡
@Date: 2019-10-18 18:12:14
@LastEditTime: 2019-10-18 20:02:45
@LastEditors: Please set LastEditors
'''
import baostock as bs
import pandas as pd

'''
@description: 获取指定股票季度频率成长性数据
@param {stock_number:股票代码
        stock_name:股票名称
        year:查询年度,int类型，为空时默认当前年
        quarter:查询季度，int类型，为空时默认当前季度。不为空时只有4个取值：1，2，3，4.
        } 
@return: 
'''
def get_growth_data(stock_number,stock_name,year,quarter):

    print('==========================================================')
    print("开始进行: "+stock_name+"("+stock_number+")"+"的数据处理")
    print("尝试登陆baostock")
    #####login#####
    lg=bs.login(user_id="anonymous",password="123456")
    if(lg.error_code == '0'):
          print("登陆成功")
    else:
          print("登录失败")


    #####get stock data#####
    rs=bs.query_growth_data(code=stock_number,year=year,quarter=quarter)

    print('请求历史数据返回代码:'+rs.error_code)
    print('请求历史数据返回信息:'+rs.error_msg)

    data_list=[]
    while(rs.error_code=='0')&rs.next():
        data_list.append(rs.get_row_data())

    result=pd.DataFrame(data_list,columns=rs.fields)
    bs.logout()
    print(stock_name+"("+stock_number+")"+"的数据处理完成")
    print('==========================================================')
    return result


'''
@description: 获取指定股票数年间季度频率的成长性数据
@param {stock_number:股票代码
        stock_name:股票名称
        start_year:查询起始年度,str类型
        end_year:查询截至年度,str类型
        } 
@return: DataFrame集合类型
'''
def get_growth_data_year(stock_number,stock_name,start_year,end_year):
    print('==========================================================')
    print("开始进行: "+stock_name+"("+stock_number+")"+"的数据处理")
    print("尝试登陆baostock")
    data_list=[]
    lg=bs.login(user_id="anonymous",password="123456")
    if(lg.error_code == '0'):
        print("登陆成功")
    else:
        print("登录失败")
    for y in range(int(start_year),int(end_year)+1):
        for  q in range(1,5):
                #####get stock data#####
                rs=bs.query_growth_data(code=stock_number,year=y,quarter=q)
                while(rs.error_code=='0')&rs.next():
                    data_list.append(rs.get_row_data())
    result=pd.DataFrame(data_list,columns=rs.fields)
    bs.logout()
    print(stock_name+"("+stock_number+")"+"的数据处理完成")
    print('==========================================================')
    return result