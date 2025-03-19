from bai3 import converter

dis, fee = input("Nhap so dam bay, so tien VND / dam : ").split(" ")

dis = int(dis)
fee = float(fee)
res = 3 * 3.14
res = dis*fee
print(f"So tien phai tra(VND) : {res} vnd")
print(f"So tien phai tra(USD) : ${converter.usd_to_vnd(res)}")
print(f"So tien phai tra(CNY) : {converter.cny_to_vnd(res)} ndt")
print(f"So tien phai tra(EUR) : {converter.eur_to_vnd(res)} euro")
