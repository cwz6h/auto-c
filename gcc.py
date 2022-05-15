import os

print("Specify A C File To Compile")
inp = input()
inp
os.system(f"gcc " + inp + " -lwinmm")
print("Done")
input()