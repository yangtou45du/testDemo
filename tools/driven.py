#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import sys
import time
from tools.myTools import Excel
from termcolor import *
from tools.myTools import *
from termcolor import *
import sys
class Driven:
    #ʵ����������
    def driven_it(self):
        ex = Excel()
        table = ex.read_it("C:\\Users\\Lenovo\\PycharmProjects\\testdemo\\testdata\\testData.xlsx")
        i = 1
        removeExcel()##ɾ����һ�α��������,
        for rownum in range(1, table.nrows):
            print "\n##### start Test Case" + str(i) + "  ####"
            write_log("\n##### start Test Case" + str(i) + "  ####")
            '''��ȡ������Ϊ�б���ʽ'''
            list = table.row_values(rownum)
            #print(list)
            # ��̬�����
            __import__('testCase.' + list[1])  # import assertResult
            #  #����ģ��
            module = sys.modules['testCase.' + list[1]]  # assertResult()
            # #����list[1]��ȡ��
            c = getattr(module, list[1])  # c=assertResult()
            # #ʵ��������
            obj = c()  # obi=assertResult()
            # #����list[2]��ȡ����
            mtd = getattr(obj, list[2])  # mtd=assert_result
            nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            try:
                  dict = {}
                  dict = get_dc(list[3])
                  exce=list[4].encode("gbk")
                  mtd(list[5],dict,exce)
            except Exception as e:
                print list[5]
                print list[4]
                print list[3]
                write_log(nowTime + " error :" + str(e) +"\n")
                print colored((nowTime + str(e)), "red")
                sys.exit()
            print("##### stop Test Case"+str(i)+"  ####\n")
            write_log("##### stop Test Case"+str(i)+"  ####\n")
            i+=1
dr=Driven()
dr.driven_it()

