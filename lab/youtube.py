from youtube_dl import YoutubeDL
#B1: download video voi url da co
# dl = YoutubeDL().download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#Youtube download : cac url download phai dc de trong 1 list

#B2: download chi voi audio
#YoutubeDL(options) 
# options = {'format' : 'bestaudio/audio' }

#options
# dl = YoutubeDL(options).download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

#B3: dowload 1 video voi url va lay video dau tien ma search dc

# options = {"default_search":"ytsearch",
#             "max_downloads":1,
# }

# dl = YoutubeDL(options).download(['con điên TAMKA PKL'])

#B4 : search and download 1st audio :

# options = {
#     "default_search": "ytsearch",
#     "max_download": 1,
#     "format":"bestaudio/audio"
# }

# dl = YoutubeDL(options).download(['Nhớ mưa sài gòn lam trường'])

list_song = [{"name": "natural","artist": "imagine dragon"},{"name":"my love", "artist":"westlife"}]

options = {
    "default_search":"ytsearch",
    "max_download":1,
}

for item in list_song:
    name = item["name"]
    artist = item["artist"]
    search = name + artist

    dl = YoutubeDL(options).download([search])




