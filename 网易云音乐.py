# -*- coding: utf-8 -*-
import os
import shutil 
from os.path import join
import requests
from bs4 import BeautifulSoup
headers = {'Referer':'http://music.163.com/','Host':'music.163.com','User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
play_url = 'http://music.163.com/playlist?id=439552159'
s = requests.session()
s = BeautifulSoup(s.get(play_url,headers = headers).content)
main = s.find('ul',{'class':'f-hide'})
list = []
for music in main.find_all('a'):
	list.append(music.text)#获取歌单
print(list)
def inlist(str,aim):#判断一首歌是否在列表中
	for i in aim:
		if str==i:
			return True
	return False
source = r'C:\CloudMusic\\'

for root, dirs, files in os.walk( source ):
	for afile in files :
		if afile[-4:]== '.mp3':
			if len(afile.split(' - '))>=2:
				name = afile.split(' - ')[1].replace('.mp3','')
				if inlist(name,list)==True:#在歌单中
					filename1 = source + afile
					open (filename1, "r").close ()
					filename2 = r'C:\Users\watersir zhangga\Music\test\\' + afile
					print(filename1, "=>", filename2)
					shutil.copy(filename1, filename2)
					if os.path.isfile (filename2): 
						print("Success")