x, n = input('Nhap x, n : ').split(' ')
x = float(x)
n = int(n)

if n % 2 != 0 :
    print("Gia tri bieu thuc = 0 ")
else :
    i = 2
    j = 1
    s = 2016 * x
    while j != n and i != n + 1 :
       s += x**i / 3**j
       i += 1
       j += 1
       print("Gia tri bieu thuc : S = ", round(s, 3))

