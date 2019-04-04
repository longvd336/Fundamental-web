# bieu dien banr gbang code


bang_luong = [
    {"name":"Hai","muc luong" : 50000 , "Ngay": 25, "gio/ngay": 8},
    {"name":"Duc", "muc luong": 25000, "Ngay": 20, "gio/ngay": 6},
    {"name":"Minh","muc luong": 20000, "Ngay": 27, "gio/ngay": 5},
    {"name":"Long","muc luong": 15000, "Ngay": 30, "gio/ngay": 3}
    ]

luong4ng = 0
for item in bang_luong:
        
    
    luong = item["muc luong"]
    ngay = item["Ngay"]
    gio_ngay = item["gio/ngay"]
    tongluong = luong * ngay * gio_ngay
    luong4ng += tongluong

print(luong4ng)

    
    
    
    





