
import sys
import xlwt
import datetime
import xlsxwriter
import mysql_info
import pymysql


def xlwt_workbook():

    sql='select * from baostock.hs300_stocks limit 1000'

    conn=pymysql.connect(mysql_info.host,mysql_info.user,mysql_info.pwd,mysql_info.database_name,char_set='utf8')
    cursor=conn.cursor()
    result=cursor.execute(sql)
    print(result)

    # workbook=xlwt.Workbook()
    # sheet=workbook.add_sheet('analysis_table',True)

def create_workbook():
    workbook=xlsxwriter.Workbook('D:/new_excel111.xlsx')

    worksheet=workbook.add_worksheet('sheet1')

    headings = ['Number','testA','testB']     #设置表头
 
    data = [
        ['2017-9-1','2017-9-2','2017-9-3','2017-9-4','2017-9-5','2017-9-6'],
        [10,40,50,20,10,50],
        [30,60,70,50,40,30],
    ]

    worksheet.write_row('A1',headings)
    worksheet.write_column('A2',data[0])
    worksheet.write_column('B2',data[1])
    worksheet.write_column('C2',data[2])

    workbook.close()      


if __name__ == '__main__':
    create_workbook()
    