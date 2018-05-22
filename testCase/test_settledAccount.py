#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import time
from common.sendRequest import sendRequest
from termcolor import *
from tools.myTools import *
class test_settledAcount():
    def assert_settledAcount(self,url,dict,exception):
        re=sendRequest().POST(url,dict)
        result=re.encode('gbk')#将unicode转为str
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if exception == result:
            print  colored(('\n' + nowTime + "  "+dict["loanNo"]+":"+"test  sucessful" + '\n'), "green")
            write_log('\n' + nowTime + "  "+dict["loanNo"]+":"+"test  sucessful" + '\n')
            list=[nowTime,url,"pass"]
            write(list)
        else:
            print ("exception:%s"%exception)
            print ("result:%s"%result)
            print colored(('\n' + nowTime +"  "+dict["loanNo"]+":"+ " test fail........." + '\n'), "red")
            write_log("exception:%s"%exception)
            write_log("result:%s"%result)
            list=[nowTime,url,"fail"]
            write(list)
            write_log('\n' + nowTime + "  " + dict["loanNo"] + ":" + "test fail........." + '\n')




url="http://221.236.20.217:8093/pcl/services/loanCenter/account/queryPaymentHistory"
dict={
    "params": {
        "loanNo": "000002017090601542",
        "isPage":1,
        "pageSize":"10",
        "pageNo":"1"
    }
}
ec='1'




