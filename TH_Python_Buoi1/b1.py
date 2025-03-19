n = 100000
while n >= 100000:
    n = int(input('nhap so nguyen it hon 5 chu so '))

l = ['don vi', 'chuc', 'tram', 'ngan', '']
i = 0

s = []
while n != 0:
    s.append(n % 10)
    n //= 10

i = len(s) - 1
while i >= 0 :
    if i == 4 :
        print(s[i], end='')
    else :
        print(s[i], l[i],sep=' ', end=' ')
    i -= 1





