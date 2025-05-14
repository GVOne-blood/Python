from typing import Protocol
class Khenthuong(Protocol):
    def khen(self) -> None:
        ...

class SinhVien(Khenthuong):
    def __init__(self, gpa):
        self.gpa = gpa
    def khen(self) -> None:
        if self.gpa > 3.2:
            print("Khen sinh vien")

class GiangVien(Khenthuong):
        def __init__(self, nckh):
            self.nckh = nckh

        def khen(self) -> None:
            if self.nckh >= 2:
                print("Khen giang vien")

class QuanLy(Khenthuong):
    def __init__(self, isComplete):
        self.isComplete = isComplete

    def khen(self) -> None:
        if self.isComplete == True:
            print("Khen quan ly")

sv = SinhVien(3.6)
gv = GiangVien(1)
ql = QuanLy(True)

sv.khen()
gv.khen()
ql.khen()