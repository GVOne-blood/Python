a = list(map(str, input("Nhap vao mang gom cac xau : ").split()))

b = tuple(a)
cnt = 0
# builtins
for i in b:
    if i.isdigit():
        cnt += 1
print(f"So xau ky tu la so la : {cnt}")

cnt = 0
# loop
# def isNumber(n : int, number : list):
#     for i in n:
#         if n not in number :
#             return False
#     return True
# number = [str(i) for i in range(0, 10)]
# for i in b:
#     for j in i:
#         if isNumber(j, number):
#             cnt += 1
# print(f"So xau ky tu la so la : {cnt}")
