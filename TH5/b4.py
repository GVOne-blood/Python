import os
import shutil

os.chdir(r"D:\TH5")
print(f"Current directory: {os.getcwd()}")

if not os.path.exists("BAI44"):
    os.mkdir("BAI44")
else:
    print("Folder BAI44 already exists")

if os.path.exists("DATA54.txt"):
    shutil.copyfile("DATA54.txt", "Data.dat")
else:
    print("DATA54.txt does not exist")

if os.path.exists("Data.dat"):
    shutil.move("Data.dat", r"BAI44\Data.dat")
else:
    print("Data.dat does not exist")

os.chdir(r"D:\TH5\BAI44")
print(f"Moved to new directory: {os.getcwd()}")

print("List files & folders of TH5:", os.listdir(r"D:\TH5"))

print("List files & folders of TH5/BAI44:", os.listdir(r"D:\TH5\BAI44"))

if os.path.exists("Data.dat"):
    os.remove("Data.dat")
else:
    print("Data.dat does not exist")

print("List files & folders of TH5/BAI44 after removing Data.dat:", os.listdir(r"D:\TH5\BAI44"))

os.chdir(r"D:\TH5")

if os.path.exists("BAI44"):
    os.rmdir("BAI44")
else:
    print("Folder BAI44 does not exist")

print("List files & folders of TH5 after removing BAI44 folder:", os.listdir(r"D:\TH5"))