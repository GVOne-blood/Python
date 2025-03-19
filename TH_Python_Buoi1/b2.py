x1, y1 = input('nhap toa do diem A(x1, y1) : ').split(' ')
x2, y2 = input('nhap x2, y2 : ').split(' ')

x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

print('Khoang cach Euclidean : D = ',round (((x2 - x1)**2 + (y2 - y1)**2)**(1/2)), 3)
print('Khonag cach Manhatan giau A va B : M = ', abs(x2 - x1) + abs(y2 - y1))
print('Khoang cach Cosin giua A va B : C = ', round(1 - ((x1*x2 + y1*y2)/(x1**2 + y1**2)**(1/2) * (x2**2 + y2**2)**(1/2)), 3))
# print (x1, x2, y1, y2)

