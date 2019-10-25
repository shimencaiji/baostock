
import sys
import xlwt
import datetime
import xlsxwriter
import mysql_info
import pymysql



def xlwt_workbook():

    sql='select * from baostock.sz50_stocks limit 1000'

    conn = pymysql.connect("localhost", "root", "", "baostock", charset='utf8')
    cursor=conn.cursor()
    count=cursor.execute(sql)
    print(count)

    cursor.scroll(0,mode='absolute')  
    results = cursor.fetchall()  
    fields = cursor.description  

    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet('analysis_table',True)

    for field in range(0,len(fields)):  
       sheet.write(0,field,fields[field][0])  

    row = 1  
    col = 0  
    for row in range(1,len(results)+1):  
        for col in range(0,len(fields)):  
            sheet.write(row,col,u'%s'%results[row-1][col]) 
    workbook.save('C:/scripts/analysis.xlsx')

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
    xlwt_workbook()
    # create_workbook()
    