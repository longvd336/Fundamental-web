from urllib.request import urlopen

from bs4 import BeautifulSoup
import pyexcel
# from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf8")

soup = BeautifulSoup(html_content, "html.parser")
# Q1/ Q2/ Q3/ Q4
div = soup.find("div", style ="background-color:#e1e1e1;overflow:hidden")
tr = div.tr
list_div = tr.find_all('td')
all_data =[]
title = ['',]
for td in list_div:
    tit = td.string
    if tit != None  :
        tit = tit.strip()
        if tit != "Tăng trưởng":
            title.append(tit)

div = soup.find("div",style ="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

list_tr = div.find_all('tr')
#  noi dung  bang
for tr in list_tr:
    mean = []
    data ={}
    list_td = tr.find_all('td')
    for td in list_td:
        a = td.string
        if a != None:
            a = a.strip()
            mean.append(a)
    
    if len(mean) == len(title):#lan luot gan value cho tung hang
        for i in range (len(title)):
            data[title[i]] = mean[i]
        all_data.append(data)
    elif mean != []:# hang chi co  1 gia tri
        
        data[title[0]] = mean[0] 
        all_data.append(data)

pyexcel.save_as(records=all_data, dest_file_name="scafe.xlsx")






