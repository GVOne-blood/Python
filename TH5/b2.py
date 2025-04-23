file2 = open("file1.txt", "r")
#1
for i in file2:
    print(i)
#2
file2.seek(0)
m, n = map(int, file2.readline().split())
a = []
print(m, n)
for i in range(n):
    row = list(map(float, file2.readline().split()))
    a.append(row)
print(a)
