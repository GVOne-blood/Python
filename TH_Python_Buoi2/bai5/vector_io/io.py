def input_vec():
    X = list(map(float, input("Nhap toa do vector(x, y, z) : ").split()))
    return X

def display(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

def display_vec(X):
    print(f" ({X[0]}, {X[1]}, {X[2]})")
