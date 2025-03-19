import exchange_rate.exchange_rate
dis, fee = input("Nhap so dam bay, so tien VND / dam : ").split(" ")

dis = int(dis)
fee = float(fee)
res = dis*fee
print(f"So tien phai tra(VND) : {res} vnd")
print(f"So tien phai tra(USD) : ${exchange_rate.usd_to_vnd(res)}")
print(f"So tien phai tra(CNY) : {exchange_rate.cny_to_vnd(res)} ndt")
print(f"So tien phai tra(EUR) : {exchange_rate.eur_to_vnd(res)} euro")
