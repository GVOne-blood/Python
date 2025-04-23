file5 = open("image.data", "+r")
for i in file5:
    print(i)
file5.seek(0)
n, m = map(int, file5.readline().split())
print("=================================")
print(n, m)
k = []
for i in file5:
    k.append(list(map(float, file5.readline().split())))
print(k)
file51 = open("image2.txt", "+w")
print("So phan tu 0 trong k : ", sum(row.count(0.0) for row in k))
# for j in range(m):
#     for i in range(n):
#         temp = k[i][j::m]
#         avg = sum(temp) / n
#         if k[i][j] == 0.0:
#             k[i][j] = avg
for row in k:
    file51.write(" ".join(map(str, row)) + "\n")

file52 = open("image51_5.txt", "+w")
file52.write(f"{n} {m} \n")
i = 0
for row in k:
    i += 1
    file52.write(" ".join(map(str, row)) + "\n")
    if i == 100:
        break
file521 = open("image51_51.txt", "+w")
file521.write(f"{n} {m} \n")
for row in k:
    i -= 1
    if i == 0:
        file521.write(" ".join(map(str, row)) + "\n")
        i = 1

