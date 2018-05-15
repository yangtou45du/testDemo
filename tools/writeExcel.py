#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
from openpyxl import load_workbook
import openpyxl
import time
def write(list):
    filename="C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx"
    wb=load_workbook(filename)
    sheet = wb.active # 激活工作页
    sheet.append(list)
    wb.save("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")





