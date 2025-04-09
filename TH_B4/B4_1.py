n = int(input("Nhap n : "))

tup = tuple(map(str, input("Nhap tup gom so tu 0 - 9 ").split()))
new_tup = []

for i in range(len(tup)):
    new_tup.append(int(tup[i]))
new_tup = tuple(new_tup)
print(f"Trung binh cong cua tup  : {sum(new_tup) / len(new_tup)}")

