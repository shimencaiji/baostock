'''
@Description: 查询季度频率企业业绩预告信息，提供2007年至今数据。 
@Author: 石门菜鸡
@Date: 2019-10-18 18:12:14
@LastEditTime: 2019-10-18 20:46:57
@LastEditors: Please set LastEditors
'''
import baostock as bs
import pandas as pd

'''
@description: 获取指定股票季度频率业绩预告数据
@param {stock_number:股票代码
        stock_name:股票名称
        start_date:开始日期,str类型，为空时默认当前年
        end_date:截止日期，str类型，为空时默认当前季度。不为空时只有4个取值：1，2，3，4.
        } 
@return: 
'''
def get_forecast_report_data(stock_number,stock_name,start_date,end_date):

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
    rs=bs.query_forecast_report(stock_number,start_date,end_date)

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


