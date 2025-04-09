config = {
    "n": 1500,
    "CLUSTERS": 3,
    "ITER": 1000,
    "METHOD": "DCA CLUSTERING",
    "MEASURE": "EUCLIDEAN",
    "YEARS": 9,
    "MAX": 200
}

print(config)

config['MEASURE'] = 'MANHATAN'
print("Config sau khi sua thong so MEASURE : ", config)

print("Gia tri hien tai cua METHOD : ", config.get("METHOD"))

config.update({'LOSS FUNCTION': 'SOFT MAX'})
print("Config sau khi update : ", config)

config.pop('YEARS')
print("Config sau khi xoa YEARS : ", config)

list_val = list(config.values())
# list_key = list(config.keys())
S = input("Nhap gia tri : ")
if S.isdigit():
    S = int(S)

if list_val.count(S) > 0:
    print(f"Tim thay gia tri {S} trong CONFIG ")
else:
    print(f"Khong tim thay gia tri {S} trong CONFIG")

temp = set(list_val)
print("Set values cua CONFIG : ", temp)

print("List values cua CONFIG : ", list_val)