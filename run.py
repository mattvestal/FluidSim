#!/usr/bin/python3.7
import os
import time

comp = os.system("gfortran param.f95 sub.f95 main.f95 -O3") # step 1 compile
start = time.time()
exec = os.system("./a.out") #step 2 execute
end = time.time()

print(end-start)
#animate = os.system("python3 animation.py") #step 3 profit
print("DONE")
