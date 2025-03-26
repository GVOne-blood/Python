a = [3, 2, 1, 4, 5, 6]

n, m = map(int, input("Nhap n va m lan luot la so dong va cot cua matrix : ").split())
l = []
if m * n == len(a):
    for i in range(n):
        l.append(a[i*m: (i + 1)*m])
    print(f"Mang duoc xay dung : {l}")
else :
    print("Khong the xay dung ma tran ")
