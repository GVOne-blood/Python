class Tamthuc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return "0"

        terms = []

        if self.a != 0:
            if self.a == 1:
                terms.append("x^2")
            elif self.a == -1:
                terms.append("-x^2")
            else:
                terms.append(f"{self.a}x^2")

        if self.b != 0:
            if self.b == 1:
                terms.append("x" if not terms else "+x")
            elif self.b == -1:
                terms.append("-x")
            elif self.b > 0:
                terms.append(f"+{self.b}x" if terms else f"{self.b}x")
            else:
                terms.append(f"{self.b}x")

        if self.c != 0:
            if self.c > 0:
                terms.append(f"+{self.c}" if terms else f"{self.c}")
            else:
                terms.append(f"{self.c}")

        if not terms:
            return "0"

        return " ".join(terms)

    def __neg__(self):
        return Tamthuc(-self.a, -self.b, -self.c)

    def __add__(self, other):
        return Tamthuc(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other):
        return Tamthuc(self.a - other.a, self.b - other.b, self.c - other.c)


tt1 = Tamthuc(2, 3, 4)
tt2 = Tamthuc(5, 6, 7)
tt11 = tt1.__neg__()
tt21 = tt2.__neg__()

print(f"2 tam thuc truoc khi doi dau : {tt1.__str__()} \t {tt2.__str__()} ")
print(f"2 tam thuc sau khi doi dau : {tt11.__str__()} \t {tt21.__str__()} ")

tt3 = tt1.__add__(tt2)
tt4 = tt1.__sub__(tt2)
print(f"Tong 2 tam thuc : {tt3.__str__()}")
print(f"Hieu 2 tam thuc : {tt4.__str__()}")