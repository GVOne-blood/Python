file3 = open("DATA54.txt", "r")
n, m = map(int, file3.readline().split())
a = []
print(n, m)
for i in file3:
    a.append(list(map(float, i.split())))
print(a)
avg = 0
for j in range(m):
    for i in range(n):
        temp = a[i][j::m]
        avg = sum(temp) / n
        # print(sum(a[i][j::m]))
    # print("++++++")
    print(f"Trung binh cong cua cot thu {j + 1} : {round(avg, 3)}")

