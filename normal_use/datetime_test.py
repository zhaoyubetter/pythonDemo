# 日期测试

from datetime import datetime
import time
import re

####### datetime
print(datetime.now()) # 2018-09-25 21:51:49.106615
print(datetime.today()) #2018-09-25 21:52:46.890815

#获取当前时间戮
a=datetime.now()
print(a.timestamp())    # 1537883747.945216

####### time
print(time.time()) #1537883747.945216

###### 格式化
localTime = time.localtime()
strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime) #2018-09-25 21:58:51
print( time.strftime('%Y', localTime )) #2018-09-25
print(strTime)

print(time.strftime('%Y-%m-%d',time.localtime(1511515800)))

