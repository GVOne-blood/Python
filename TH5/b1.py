with open("file1.txt", "w") as file1:
    m, n = map(int, input("Nhap m, n: ").split())
    file1.write(f"{m} {n}\n")

    a = []
    for i in range(n):
        print(f"Nhap dong thu {i + 1}:")
        while True:
            row = list(map(float, input().split()))
            if len(row) != m:
                print(f"Chieu dai cua dong phai bang {m}")
                continue
            a.append(row)
            file1.write(" ".join(map(str, row)) + "\n")
            break

    print("Ma tran da nhap:")
    print(a)