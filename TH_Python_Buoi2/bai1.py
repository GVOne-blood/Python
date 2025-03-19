def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def dx(n):
    n = str(n)
    return n == n[::-1]


# def eratosthenes(s, e):
#     l = [1] * (e + 1)
#     l[0] = 0
#     l[1] = 0
#
#     for i in range(2, int(e ** 0.5) + 1):
#         if l[i] == 1:
#             for j in range(i * i, e + 1, i):
#                 l[j] = 0
#
#     return l[s:e + 1] if s > 1 else l[:e + 1]

def eratosthenes(s, e):
    l = []
    for i in range(e + 1):
        l.append(1)
    l[0] = 0
    l[1] = 0
    for i in range(int(e ** 0.5) + 1):
        if l[i] == 1:
            for j in range(i * i, e + 1, i):
                l[j] = 0
    return l
#
# primes = eratosthenes(2, 20)
# for i in range(len(primes)):
#     if primes[i] == 1:
#         print(i + 2, end=" ")  # Prints 2 3 5 7 11 13 17 19


S = "999999999"
E = "999999999"
while len(str(E)) > 8 and int(S) >= int(E):
    S, E = input("Nap S, E(S < E): ").split()

S = int(S)
E = int(E)

sum = 0
# for i in range(S, E + 1):
#     if isPrime(i) and dx(i):
#         sum += i
#         print(i,end=" ")

primes = eratosthenes(S, E)
for i in range (S, len(primes)):
   if primes[i] == 1 and dx(i):
        sum += i
if sum == 0:
    print("Khong co so nao thoa man dieu kien trong doan [S, E]")
else:
    print(f"Tong cac so thoa man : {sum}")
