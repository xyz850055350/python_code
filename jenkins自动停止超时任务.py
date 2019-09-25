#jenkins登录

import jenkinsapi
from jenkinsapi.jenkins import Jenkins
username='zhangzhang'
password='Aa123456'
api_token='cce529148db2e7d98735ba2ebd0d9cae'

J = Jenkins('http://10.10.10.10:8080',username,password)
print(J.version)

#[Jenkins]如何自动停止超时任务？
for key,job in J.iteritems():
  last_build = job.get_last_buildnumber()//获得最后一个构建的编号
  running = build.is_running()//任务是否在运行
  start_time =  last_build.get_timestamp()//获得构建的开始时间
  last_build.stop()//停止构建
