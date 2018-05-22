#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import xlrd,sys
from openpyxl import load_workbook
from openpyxl import Workbook
import cx_Oracle
class Excel():
    def read_it(self, path, index=0):
        data=xlrd.open_workbook(path)
        sheet=data.sheets()[index]
        return sheet
def removeExcel():
    wb=load_workbook("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    sheet=wb.active
    wb.remove(sheet)#s删除上一次报告的内容
    wb1=Workbook("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    wb1.create_sheet(title="test_result",index=0)#新建一个工作表
    wb1.save("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    wb1.close()
def write_log(msg):
    f=open("C:\\Users\\Lenovo\\PycharmProjects\\testdemo\\testdata\\log.txt","a")
    f.write(msg)
    f.close()
def write(list):
    filename="C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx"
    wb=load_workbook(filename)
    sheet = wb.active # 激活工作页
    sheet.append(list)
    wb.save("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
def get_dc(string):
    list=string.split("\n")
    dc={}
    for i in list:
        list1=i.split("=")
        dc[list1[0]]=list1[1]
    return dc
class connectOracle():
    def __init__(self,ora="PH_CS "):
        self.db = cx_Oracle.connect("pcltest/Phtest123@221.236.20.222:15218/orcl")  # 连接数据库
        self.cr = self.db.cursor()  # 创建cursor
        if ora=="ORCL_ODS":
            self.db = cx_Oracle.connect("pcl/Phpcl321@221.236.20.211:15213/orcl")  # 连接数据库
            self.cr = self.db.cursor()  # 创建cursor

    def sqlSelect(self,sql):
        self.cr.execute(sql)#z执行sql语句
        rs=self.cr.fetchall()#一次返回所有结果集
        self.cr.close()
        print rs
    def sqlDML(self,sql):
        self.cr.execute(sql)  # z执行sql语句
        rs = self.cr.fetchall()  # 一次返回所有结果集
        self.cr.close()
        self.db.commit()
        print rs
    def sqlFlashBack(self):
        self.cr.execute("select sql_text,last_load_time from v$sql where sql_text like '%update%' order by last_load_time desc")  # 根据SQL执行历史确定数据回滚时间点
        self.cr.execute("alter table tablename enable row movement")#再将数据回滚到需要的时间点
        self.cr.execute("flashback table tablename to timestamp to_timestamp('xxxx-xx-xx xx:xx:xx', 'yyyy-mm-dd hh24:mi:ss')")
sql="select t.*, t.rowid from bus_t_case_manage_log t where t.LOAN_NO='652902017071401097'"
f=connectOracle().sqlSelect(sql)
