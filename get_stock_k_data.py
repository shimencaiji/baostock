'''
@Description: 从baostock平台获取交易数据
@Author: 石门菜鸡
@Date: 2019-10-18 10:14:26
@LastEditTime: 2019-10-18 15:08:35
@LastEditors: Please set LastEditors
'''
import baostock as bs
import pandas as pd
'''
@description: 从baostock平台获取交易数据
@param {stock_number:股票代码
        stock_name:股票名称
        start_day:开始时间
        end_day:截止时间
        freq:数据分析周期，默认为d，日k线；d=日k线、w=周、m=月
        adflag:复权类型，默认不复权：3；1：后复权；2：前复权；3：不复权
        } 
@return: pd.DataFrame类型数据集合
'''
def get_stock_data(stock_number,stock_name,start_day,end_day,freq,adflag):

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
    rs=bs.query_history_k_data(stock_number, "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",start_date=start_day,end_date=end_day,frequency=freq, adjustflag=adflag)

    print('请求历史数据返回代码:'+rs.error_code)
    print('请求历史数据返回信息:'+rs.error_msg)

    data_list=[]
    while(rs.error_code=='0')&rs.next():
        data_list.append(rs.get_row_data())

    result=pd.DataFrame(data_list,columns=rs.fields)
    bs.logout()
    return result



