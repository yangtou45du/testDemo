#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
from openpyxl import load_workbook
from openpyxl import Workbook
def removeExcel():
    wb=load_workbook("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    sheet=wb.active
    wb.remove(sheet)#sɾ����һ�α��������
    wb1=Workbook("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    wb1.create_sheet(title="test_result",index=0)#�½�һ��������
    wb1.save("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")
    wb1.close()



#removeExcel()