dic = {
    "2022602123": 4.0,
    "2021606128": 2.6,
    "2023602607": 3.4,
    "2022600231": 1.8,
}

print("So sinh vien co diem so thuoc doan [2.5 , 3.5] : ",
      len([k for k, v in dic.items() if 2.5 <= v <= 3.5]))

dic.update({"2022604200": 3})

print("Ds sau khi them sinh vien moi ", dic)

list_key = [k for k, v in dic.items() if v < 2.0]
for k in list_key:
    dic.pop(k)
print("Ds sinh vien sau khi xoa sinh vien co diem < 2 : ",
      dic)

