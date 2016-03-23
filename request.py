#!/usr/bin/python

import urllib2
import urllib
import json
data={}
#����
data['sha1']='14a7fbbf6d51e32e6138e1482e6ead778f382aee'
data['token']='wolfeye'
#�����ַ
url_query  = 'http://wolfeye.baidu.com/api/query/'
post_data=urllib.urlencode(data)
#Я������������
req=urllib2.urlopen(url_query,post_data)
#�õ�Ӧ��
content=req.read()
#s��loads����Ӧ��
s=json.loads(content)
#�����ڵ�
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
#type�õ���������
#print '--'+str(type(static))
#print '---'+str(type(vulnresult))
#print type(exported_components)
print '---------'+'©������'+'------------------------------------'
print 'high level:'+str(high_count)
print 'mid  level:'+str(mid_count)
print 'low  level:'+str(low_count)
print '---------'+'����©����Ϣ'+'---------------------------------'
#��ӡlist
#print '-----'+repr(static.get('vulnresult'))
for i in vulnresult:
        risk_level=i.get('risk_level')
        vuln_count=i.get('vuln_count')
        vuln_description=i.get('vuln_description')
        print risk_level
        print vuln_count
        print vuln_description
        print '-----------------------------------------------------------'       
print '---------'+'meta��Ϣ'+'----------------------------------------'
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
