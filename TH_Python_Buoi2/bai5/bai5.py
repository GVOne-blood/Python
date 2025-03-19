from vector_io.io import input_vec, display_vec, display
from vector_calculator.formular import plus, subtract, distance
A = input_vec()
display_vec(A)
B = input_vec()
display_vec(B)
print (f"Tong 2 vec : {plus(A, B)}")
print(f"Hieu 2 vec {subtract(A, B)}")
print(f"Khoang cach 2 vec : {round(distance(A, B), 3)}")

dict = {
    'A' : tuple(A),
    'B' : tuple(B),
}
display(**dict)