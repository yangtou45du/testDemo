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
from testCase.test_orRemove import test_orRemove
class Driven:
    #ʵ����������
    def driven_it(self):
        ex = Excel()
        table = ex.read_it("C:\\Users\\Lenovo\\PycharmProjects\\testdemo\\testdata\\testData.xlsx")
        i = 1
        s=0
        removeExcel()##ɾ����һ�α��������,
        list=["time","url","exception","actual","result"]
        write(list)
        for rownum in range(1, table.nrows):
            print "\n##### start Test Case" + str(i) + "  ####"
            write_log("\n##### start Test Case" + str(i) + "  ####")
            '''��ȡ������Ϊ�б���ʽ'''
            list = table.row_values(rownum)
            print(list)
            # ��̬�����
            __import__('testCase.' + list[1])  # testCase.test_orRemove
            #  #����ģ��
            module = sys.modules['testCase.' + list[1]]  # assertResult()
            # #����list[1]��ȡ��
            c = getattr(module, list[1])  # c=test_orRemove
            # #ʵ��������
            obj = c()  # obi=test_orRemove()
            # #����list[2]��ȡ����
            mtd = getattr(obj, list[2])  # mtd=assert_orRemove
            nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            try:
                exce = list[4].encode("gbk").replace(' ','').replace("\n", "")#��unicodeתΪstrȥ���ո�ͻ��з�
                if "=" in list[3]:
                    dict = {}
                    dict = get_dc(list[3])
                    s+=mtd(list[5],dict,exce)
                else:
                    s+=mtd(list[5],eval(list[3].encode('gbk')),exce)
            except Exception as e:
                write_log(nowTime + " error :" + str(e) +"\n")
                print colored((nowTime + str(e)), "red")
                sys.exit()
            print("##### stop Test Case"+str(i)+"  ####\n")
            write_log("##### stop Test Case"+str(i)+"  ####\n")
            list=["pass",s,"fail",i-s]
            write(list)
            i+=1


dr=Driven()
dr.driven_it()




