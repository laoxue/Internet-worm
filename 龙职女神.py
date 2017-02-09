# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup
import requests
pictres=[]
names=[]
for page in range(1,6):
	html=requests.get('http://wx.vddl.cn/dz/plugin.php?id=hejin_toupiao&model=votea&vid=1&page=%s'%page).text
	soup = BeautifulSoup(html)
	imgs = soup.select('.img img')
	mings=soup.select('.number')
	for img in imgs:
		pictres.append(img['src'])
y=1
for x in pictres:
	pic=requests.get(x)
	fp=open('h://database/webgirl/%s.jpg'%y,'wb')
	fp.write(pic.content)
	fp.close()
	y+=1
print names

for x in Pic:
	pic = requests.get(x)
	fp = open('h://database/webgirl/%s.jpg'%y,'wb')
	fp.write(pic.content)
	fp.close()
	print 'Now is downloading %s'%y
	y+=1
  
 有很多地方需要优化，整体代码也不复杂
