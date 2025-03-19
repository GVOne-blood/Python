def euclidean(x1, y1, x2, y2):
    return ((x2 - x1)**2    +   (y2 - y1)**2)**0.5
def STriangle(A, B, C):
    ab = euclidean(A[0], A[1], B[0], B[1])
    bc = euclidean( B[0], B[1], C[0], C[1])
    ac = euclidean(A[0], A[1], C[0], C[1])

    return ab * bc * ac