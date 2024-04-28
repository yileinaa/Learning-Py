import requests
import re
#url=('https://tuostudy.com/zh-CN/?ref=lovejay.top')
#resp=requests.get(url)
#resp.enconding='utf-8'
#print(resp.text)
#se=re.findall('sss([\u3e00-\u9fa5]+)sss',resp.text)
#爬取图片
url =('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
resp=requests.get(url)
with open('logo.png','wb')as file:
    file.write(resp.content)
