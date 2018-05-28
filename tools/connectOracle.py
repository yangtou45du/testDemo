#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import cx_Oracle
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
sql=" SELECT t.*, t.rowid FROM BUS_T_LOAN_OVERDUE_CASE t WHERE t. OVERDUE_LEVEL='1' AND   t. DEAL_STATUS='046003'and rownum=1 "
f=connectOracle("ORCL_ODS").sqlSelect(sql)