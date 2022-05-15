import os

print("Specify CPP File To Compile")
inp = input()
inp
os.system(f"g++ " + inp + " -lwinmm")
print("Done")
input()