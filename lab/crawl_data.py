#B1 : Open connection
from urllib.request import urlopen

from bs4 import BeautifulSoup

from collections import OrderedDict
url = "https://dantri.com.vn"
#urlopen (link): mo 1 duong dan toi link can lay du lieu
 
conn = urlopen(url)

raw_data = conn.read()
# lam min code(utf8 la bo ma danh cho ngon nngu co dau)
html_content = raw_data.decode("utf8")

with open("dantri.html", "wb") as f:
    f.write(raw_data)


#"dantri.html": file ghi ra
# wb: write binary

# #B2 : Find ROI(region of interest):

# soup = BeautifulSoup(html_content, "html.parser")
# # print(soup.prettify())

# ul = soup.find("ul" , "ul1 ulnew")
# #preti: lam dep 
# # print(ul.prettify())


# #3. Extract ROI

# dict_link = []

# import pyexcel
# li_list = ul.find_all("li")
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     title = a.string.strip()
    
#     link = url + a["href"]
#     print(title)
#     print(link)
#     print("*"*20)
#     dict_link.append(OrderedDict({"title" : title , "link" : link}))
    
# pyexcel.save_as(records=dict_link, dest_file_name="dantri.xlsx")




