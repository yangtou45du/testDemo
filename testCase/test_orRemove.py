#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import time
from common.sendJsonRequest import sendRequest
from termcolor import *
from tools.myTools import *
class test_orRemove():
    def assert_orRemove(self,url,dict,exception):
        re = sendRequest().POST(url, dict)
        result = re.encode('gbk')  # 将unicode转为str
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if exception in result:
            print  colored(('\n' + nowTime + "  " + ":" + "test  sucessful" + '\n'), "green")
            write_log('\n' + nowTime + "  "  + ":" + "test  sucessful" + '\n')
            list = [nowTime, url, "pass"]
            write(list)
            #print(result)
        else:
            print ("exception:%s" % exception)
            print ("result:%s" % result)
            print colored(('\n' + nowTime + "  " +  ":" + " test fail........." + '\n'), "red")
            write_log("exception:%s" % exception)
            write_log("result:%s" % result)
            list = [nowTime, url, "fail"]
            write(list)
            write_log('\n' + nowTime + "  " + ":" + "test fail........." + '\n')


url="http://221.236.20.217:8093/pcl/services/loanCenter/account/queryPaymentHistory"
dict={
    "params": {
        "loanNo": "000002017090601542",
        "isPage":1,
        "pageSize":"10",
        "pageNo":"1"
    }
}
ec="\"code\":\"0000\""
#f=test_orRemove().assert_orRemove(url,dict,ec)



