from my_vector import vector
print("Ham nhap mang ")
l = vector.vecinput()
print("Tong cac phan tu trong mang ", vector.vecsum(l))

id = len(l) + 1
while (id > len(l)):
    id = int(input("Nhap vi tri can chen :"))
k = float(input("Nhap phan tu can chen : "))
print(f"Ket qua khi chen phan tu {k} vao vi tri {id} trong mang : {vector.vecinsert(l, id, k)}")

d = float(input("Nhap phan tu muon xoa : "))
while (d not in l):
    d = float(input("Phan tu da nhap khong ton tai, nhap lai : "))
else:
    print(f"Mang sau khi xoa phan tu {d} la : {vector.vecdel(l, k)}")

print("Nhap mang thu 2 : ")
l2 = vector.vecinput()
print(vector.vecadd(l, l2))

