from bai4.formular.geometry import euclidean
def isTriangle(A, B, C):
    ab = euclidean(A[0], A[1], B[0], B[1])
    bc = euclidean( B[0], B[1], C[0], C[1])
    ac = euclidean(A[0], A[1], C[0], C[1])

    print(ab, bc, ac)
    return ab * bc * ac > 0