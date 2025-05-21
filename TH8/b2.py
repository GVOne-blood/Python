f1 = open('random_integers.txt')
for i in f1:
    print(i.strip())
f1.seek(0)
n,m = int(f1.read(1)), int(f1.read(3))
print(n, m)
f1.seek(5)
K = []
for i in f1:
    l = [int(x) for x in i.strip().split()]
    K.append(l)
print(K)
avg = []
temp = -1
for i in range(n):
    avg.append(sum(K[i]) / m)
    temp = max(max(K[i]), temp)

print(avg)

print(max(K))
print(temp)
print(f'Is max element in K is in max avg row in k : {temp in max(K)}')
j = 0
zero = K.count(0)
for i in range(n):
    res = [avg[i] for x in K[i] if x == 0]
print(res)