a = list(input("Nhap mang a : ").split())
b = list(input("Nhap mang b : ").split())
i, j = 0, 0
l = []
while i < len(a) and j < len(b):
    l.append(a[i])
    l.append(b[j])
    i+=1
    j+=1

while i < len(a):
    l.append(a[i])
    i+=1

while j < len(b):
    l.append(b[j])
    j+=1

print(f"mang sau khi merge : {l}")