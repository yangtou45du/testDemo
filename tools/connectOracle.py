#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import cx_Oracle
class connectOracle():
    def __init__(self,ora="PH_CS "):
        self.db = cx_Oracle.connect("pcltest/Phtest123@221.236.20.222:15218/orcl")  # �������ݿ�
        self.cr = self.db.cursor()  # ����cursor
        if ora=="ORCL_ODS":
            self.db = cx_Oracle.connect("pcl/Phpcl321@221.236.20.211:15213/orcl")  # �������ݿ�
            self.cr = self.db.cursor()  # ����cursor

    def sqlSelect(self,sql):
        self.cr.execute(sql)#zִ��sql���
        rs=self.cr.fetchall()#һ�η������н����
        self.cr.close()
        print rs
    def sqlDML(self,sql):
        self.cr.execute(sql)  # zִ��sql���
        rs = self.cr.fetchall()  # һ�η������н����
        self.cr.close()
        self.db.commit()
        print rs
    def sqlFlashBack(self):
        self.cr.execute("select sql_text,last_load_time from v$sql where sql_text like '%update%' order by last_load_time desc")  # ����SQLִ����ʷȷ�����ݻع�ʱ���
        self.cr.execute("alter table tablename enable row movement")#�ٽ����ݻع�����Ҫ��ʱ���
        self.cr.execute("flashback table tablename to timestamp to_timestamp('xxxx-xx-xx xx:xx:xx', 'yyyy-mm-dd hh24:mi:ss')")
sql=" SELECT t.*, t.rowid FROM BUS_T_LOAN_OVERDUE_CASE t WHERE t. OVERDUE_LEVEL='1' AND   t. DEAL_STATUS='046003'and rownum=1 "
f=connectOracle("ORCL_ODS").sqlSelect(sql)