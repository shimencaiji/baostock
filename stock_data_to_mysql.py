'''
@Description: 将获取到的baostock数据写入数据库中
@Author: 石门菜鸡
@Date: 2019-10-18 10:17:06
@LastEditTime: 2019-10-18 15:01:49
@LastEditors: Please set LastEditors
'''
import pandas as pd
#import re
from sqlalchemy import create_engine

sql_login_message="mysql+pymysql://root:891219@localhost:3306/"
'''
@description: 将Dataframe型数据写入数据库中
@param {baostock_result:baostock查询结果
        database_name:将要写入的数据库名称
        table_name：将要写入的表名称
        mode:写入模式
        } 
@return: NULL
'''
def write_data_to_database(baostock_result,database_name,table_name,mode):
    print("尝试建立数据库引擎")
    database_engine=create_engine(sql_login_message+database_name+'?charset=utf8')
    print("尝试写入数据库")
    baostock_result.to_sql(table_name,database_engine,schema=database_name,if_exists=mode,index=False,index_label=False)
    print("结果写入数据库：%s中 的表 %s",database_name,table_name)
    