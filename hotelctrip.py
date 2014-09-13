#--*coding:utf-8*-
#从携程上获得酒店姓名、酒店地址、酒店星级等信息
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize
import re
import os

os.chdir("E:\Python Code")

# soup=BeautifulSoup('<a data-hotel="375288"  data-ctm="#ctm_ref=hd_0_0_0_0_lst_sr_1_df_ls_1_i_hi_0_0_0" tracekey="nhtllistroomclick" tracevalue="clicktype=htlpic;hotelid=375288;roomid=;isdefaultdisplay=;defaultdisplaypos=;htlpos=1;rompos=;" href="/hotel/375288.html" target="_blank" class="hotel_abbrpic haspic" rel="nofollow">')
# tag=soup.a
# attr=tag.attrs
# print(attr)



htmlfile=urllib.urlopen("http://hotels.ctrip.com/hotel/nanjing12")
soup=BeautifulSoup(htmlfile)

hotel=soup.find_all('a',class_="hotel_abbrpic haspic",title=True,href=True)
attr=hotel[0].attrs
print(attr)

# for tag in soup.findAll('a', hotelid=True):
# 	print(tag)

# info=open('basicinfo.txt','w+')
# for tag in soup.findAll('a',tracekey=True):
# 	link=tag['href']
# 	info.write(link)

# info.close()





