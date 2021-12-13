from urllib import request
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from urllib.request import urlopen
import random
import time
from tqdm import tqdm, trange
import re
from requests.exceptions import HTTPError
from lxml import html
import pymysql
import sqlite3


url = 'https://lol.inven.co.kr/dataninfo/champion/compare.php'


requests.get(url)
resp = requests.get(url)
print(resp)

#tree = html.fromstring(resp.content)

#데이터 출력
#print(resp.text)

soup = bs(resp.content, 'html.parser')
#dmg = soup.find_all(class_='')
#print(soup)

#제목 
title = soup.find("thead").find_all("th")
title_list=[]
for th in title:
    title_list.append(th.text)

print(title_list)

#주요 내용
body = soup.find("tbody").find_all("tr")
body_list=[]
for tr in body:
    body_list.append(tr.text)
print(body_list)



#관계형 데이터베이스에 연결
conn = sqlite3.connect('data.db')

cur = conn.cursor()

cur.execute("select * from title_list")

rows =cur.fetchall()
for row in rows:
    print(row)

conn.close()



#파일 저장
'''
f = open('c:\coding/test.txt', 'w')
for th in title_list:
    f.write(th+"\n")
f.close()
'''



#df = pd.read_html(url, header=0)







print("LAMO")