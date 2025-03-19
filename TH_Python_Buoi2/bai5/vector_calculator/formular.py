def plus(A, B):
    return list(x + y for x, y in zip(A, B))
def subtract(A, B):
    return list(x - y for x, y in zip(A, B))
def distance(A, B):
    return float((sum((x - y)**2 for x, y in zip(A, B)))**0.5)
