class Person:
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address


class KYSU(Person):
    def __init__(self, name, dob, address, major, graduated):
        super().__init__(name, dob, address)
        self.major = major
        self.graduated = graduated


    def display(self):
        print(f"{self.name} \t {self.dob} \t {self.address} \t {self.major} \t {self.graduated} \n");


n = int(input("Nhap so luong ky su : "))


def init():
    lks = []
    ks = KYSU("Do Tuan", "13/12/2000", "Ha Noi", "Software Engineering", 2024)
    for i in range(n):
        lks.append(ks)
    return lks


l = init()

# for i in range(n):
#     name = input("Nhap ten : ")
#     dob = input("Nhap ngay sinh : ")
#     addr = input("Nhap dia chi : ")
#     major = input("Nhap nganh : ")
#     gradu = int(input("Nhap nam tot nghiep : "))
#     ks = KYSU(name, dob, addr, major, gradu)
#     l.append(ks)

max = -1
print("Thong tin cac ky su ")
for i in l:
    if i.graduated > max:
        max = i.graduated
    i.display()
print("thong tin ky su toot nghiep nam gan nhat : ")

for i in l:
    if i.graduated == max:
        i.display()
