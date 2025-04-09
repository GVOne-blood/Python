A = set(map(str, input("Nhap vao ds sv ban so 1 : ").split()))
B = set(map(str, input("Nhap vao ds sv ban so 2 : ").split()))

print("Set A : ", A)
print("Set B : ", B)
if A | B == set():
    print("Khong co sinh vien nao")
else:
    if A & B == set() :
        print("Khong co sv dang ky o ca 2 ban")
    else:
        print("Sinh vien dang ky hoc o ca 2 ban : ", A & B)

    print("Tong cac sinh vien da dang ky : ", A | B)

    if (A - B == set()):
        print("Ban 1 khong co sinh vien ")
    else:
        print("Ds sinh vien chi dang ky tai ban 1 :", A - B)