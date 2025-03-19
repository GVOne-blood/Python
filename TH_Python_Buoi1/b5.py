n = 1000000
str = ''
while n >= 1000000 :
    str = input('Nhap so nguyen n co it hon 7 chu so : ')
    n = int(str)

n = int(str)
isPrime = True
for i in range (2, int(n**(1/2)) + 1) :
    if n % i == 0 :
        isPrime = False
        break
if (str == str[::-1] and isPrime == True) :
    print("so {0} la so doi xung ".format(n))
else :
    print("so {0} khong phai la so doi xung ".format(n))