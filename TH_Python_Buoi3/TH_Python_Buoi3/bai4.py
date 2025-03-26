a = list(map(int, input("Nhap mang a : ").split()))
b = list(map(int, input("Nhap mang b : ").split()))

a.sort()
b.sort()
l = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        l.append(a[i])
        i += 1
    else:
        l.append(b[j])
        j += 1

while i < len(a):
    l.append(a[i])
    i += 1
while j < len(b):
    l.append(b[j])
    j += 1

print(f"Mang da ket hop : {l}")