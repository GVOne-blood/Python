S = input("Nhap xau S : ")
Q = "he"

if S.find(Q) != -1:
    print("Q la xau con cua S : ")
else:
    print("Q khong phai xau con cua S : ")

P = S + Q
print("Chuoi sau khi hop nhat : ", P)

while P.find("Ha") != -1:
    P = P.replace("Ha", "Ba")
print("Chuoi sau khi thay the : ", P)

l = P.split()
digit = [i for i in l if i.isdigit()]
word = [i for i in l if i.isalpha()]

# print(digit)
# print(word)

dic = {k: v for k, v in zip(digit, word)}
if dic == {}:
    print("Khong the tao dictionary tu xau da cho")
else:
    print("Tu dien duoc tao : ", dic)