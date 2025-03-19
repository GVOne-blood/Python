from bai4.formular.geometry import euclidean, STriangle
from bai4.validate.triangle import isTriangle
A = list(map(float, input("Nhap toa do diem A : ").split()))
B = list(map(float, input("Nhap toa do diem B : ").split()))
C = list(map(float, input("Nhap toa do diem C : ").split()))

disA = euclidean(A[0], A[1], 0, 0)
disB = euclidean(B[0], B[1], 0, 0)
disC = euclidean(C[0], C[1], 0, 0)

xOy = {
      "A" : disA,
      "B" : disB,
      "C" : disC,
}

print(f"Diem gan tam O nhat : "
      f"{min(xOy, key=xOy.get)}")
print(f"Diem xa tam O nhat : "
      f"{max(xOy, key=xOy.get)}")

if isTriangle(A, B, C):
      print(f"Dien tich tam giac ABC : {STriangle(A, B, C)}")
else :
      print("# diem da cho khong tao thanh 1 tam giac ")