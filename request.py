#!/usr/bin/python

import urllib2
import urllib
import json
data={}
#参数
data['sha1']='14a7fbbf6d51e32e6138e1482e6ead778f382aee'
data['token']='wolfeye'
#请求地址
url_query  = 'http://wolfeye.baidu.com/api/query/'
post_data=urllib.urlencode(data)
#携带参数发请求
req=urllib2.urlopen(url_query,post_data)
#得到应答
content=req.read()
#s是loads到的应答
s=json.loads(content)
#解析节点
result=s.get('result')
static=result.get('static')

meta=result.get('meta')
target_sdk=meta.get('target_sdk')
package_name=meta.get('package_name')
exported_components=meta.get('exported_components')
activity=exported_components.get('activity')
receiver=exported_components.get('receiver')
service=exported_components.get('service')
provider=exported_components.get('provider')
uses_permission=meta.get('uses_permission')

vulnresult=static.get('vulnresult')
high_count=static.get('high_count')
mid_count=static.get('mid_count')
low_count=static.get('low_count')
#type得到数据类型
#print '--'+str(type(static))
#print '---'+str(type(vulnresult))
#print type(exported_components)
print '---------'+'漏洞个数'+'------------------------------------'
print 'high level:'+str(high_count)
print 'mid  level:'+str(mid_count)
print 'low  level:'+str(low_count)
print '---------'+'具体漏洞信息'+'---------------------------------'
#打印list
#print '-----'+repr(static.get('vulnresult'))
for i in vulnresult:
        risk_level=i.get('risk_level')
        vuln_count=i.get('vuln_count')
        vuln_description=i.get('vuln_description')
        print risk_level
        print vuln_count
        print vuln_description
        print '-----------------------------------------------------------'       
print '---------'+'meta信息'+'----------------------------------------'
print 'target_sdk:'+str(target_sdk)
print 'package_name:'+str(package_name)

for k,v in exported_components.items():
        print ("%s=%s" % (k, v))

print '--------'+'uses_permission'+'---------------------------------'
for i in uses_permission:
        sensitive=i.get('sensitive')
        name=i.get('name')
        print 'sensitive:'+str(sensitive)
        print 'name:'+str(name)

print '--------------------------------------------------------------'

def jsonFile(fileData):
	file = open("D:\json.txt","w")
	file.write(fileData)
	file.close()
        
        
if __name__ == "__main__":
	jsonFile(content)
