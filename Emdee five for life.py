#Emdee five for life
# By M.Teja Vardhan

import requests
import sys
import bs4
import hashlib
url="http://178.128.162.230:31106/"
sess=requests.Session()
raw_response=sess.get(url)
post_data={"hash": hashlib.md5(bs4.BeautifulSoup(raw_response.text,features="lxml").body.h3.text.encode("UTF-8")).hexdigest()}
raw_response=sess.post(url,post_data)
print(bs4.BeautifulSoup(raw_response.text,features="lxml").body.p.text)
sess.close()
