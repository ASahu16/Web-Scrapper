import requests as r
import urllib.request
import bs4
data=r.request('get','https://dubai.dubizzle.com/motors/used-cars/jeep/wrangler/2019/10/5/aed1257month-2016-jeep-wrangler-sport-36l--2/?back=L21vdG9ycy9zZWFyY2gvP2tleXdvcmRzPSZpc19zZWFyY2g9MSZpc19iYXNpY19zZWFyY2hfd2lkZ2V0PTE%3D&pos=1')
s=bs4.BeautifulSoup(data.text,'html.parser')
q=0
for j in s.findAll('div'):
	if(j.get('id')=="photos"):
		for i in j.findAll('img'):
			urllib.request.urlretrieve(i.get('src'),'D://img%r.jpg'%(q))
			q+=1