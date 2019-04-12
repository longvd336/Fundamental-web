from urllib.request import urlopen

from bs4 import BeautifulSoup

from collections import OrderedDict

from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()

html_content = raw_data.decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("section", "section chart-grid")

li_list = ul.find_all("li")
dict_link = []
import pyexcel
for li in li_list:
    
    a = li.a
    link = url + a["href"]
    h3 = li.h3
    b = h3.a
    name = b.string.strip()
    
    h4 = li.h4
    c = h4.a
    artist = c.string.strip()
    
    dict_link.append(OrderedDict({"name" : name , "link" : link,"artist": artist}))
    
options = {
    "default_search":"ytsearch",
    
    "max_download":1,
}

for item in dict_link:
    name = item["name"]
    artist = item["artist"]
    search = name + artist

    dl = YoutubeDL(options).download([search])

# pyexcel.save_as(records=dict_link, dest_file_name="song.xlsx")


