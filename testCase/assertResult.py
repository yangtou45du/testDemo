#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import time
import json
from common.settledAccount import settledAccount
from termcolor import *
from tools.myTools import *
class assertResult():
    def assert_result(self,url,dict,exception):
        re=settledAccount().POST(url,dict)
        result=re.encode('gbk')#将unicode转为str
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if exception==result:
            print  colored(('\n' + nowTime + "  "+dict["loanNo"]+":"+"test  sucessful" + '\n'), "green")
            write_log('\n' + nowTime + "  "+dict["loanNo"]+":"+"test  sucessful" + '\n')
            list=[nowTime,dict["loanNo"],"pass"]
            write(list)
        else:
            print ("exception:%s"%exception)
            print ("result:%s"%result)
            print colored(('\n' + nowTime +"  "+dict["loanNo"]+":"+ " test fail........." + '\n'), "red")
            write_log("exception:%s"%exception)
            write_log("result:%s"%result)
            list=[nowTime,dict["loanNo"],"fail"]
            write(list)
            write_log('\n' + nowTime + "  " + dict["loanNo"] + ":" + "test fail........." + '\n')



'''
url="http://amstest4.phkjcredit.com/ams_web/ContextServlet"
dict={'loanNo':"640102016041803097",'action':' com.hansy.forsaler.action.ForSalerAction',
'method':'queryLoanTypeByLoanNo'}
ec='1'
f=assertResult().assert_result(url,dict,ec)
'''


