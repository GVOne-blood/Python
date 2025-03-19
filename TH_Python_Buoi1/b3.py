# Nhập 3 số a, b, c từ người dùng
a, b, c = input("Nhập 3 số a, b, c: ").split(' ')
a, b, c = float(a), float(b), float(c)

if a == 0:
    if b == 0:
        if c == 0:
            print('Phương trình có vô số nghiệm')
        else:
            print('Phương trình vô nghiệm')
    else:
        print('Phương trình có nghiệm x =', round(-c / b, 3))
else:
    if c == 0:
        if b == 0:
            print('Phương trình có nghiệm x = 0')
        else:
            print('Phương trình có nghiệm x1 = 0, x2 =', round(-b / a, 3))
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            print('Phương trình vô nghiệm')
        elif delta == 0:
            print('Phương trình có nghiệm duy nhất x =', round(-b / (2 * a), 3))
        else:
            x1 = round((-b + delta**(1/2)) / (2 * a), 3)
            x2 = round((-b - delta**(1/2)) / (2 * a), 3)
            print(f'Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}')
