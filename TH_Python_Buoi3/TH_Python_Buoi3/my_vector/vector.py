def vecinput():
    x =  list(map(float, input().split()))
    return x
def vecsum(vec):
    return sum(vec)
def vecinsert(vec:list, idx:int, k:float):
      vec.insert(idx, k)
      return vec

def vecdel(vec : list, k:float):
     vec.remove(k)
     return vec
def vecadd(vec1 : list, vec2 : list):
    if (len(vec1) == len(vec2)):
        l = []
        for i, j in zip(vec1, vec2):
            l.append(i + j)
        return f"Tong la : {l} "
    return []
