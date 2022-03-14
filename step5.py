from z3 import *

target = [0x69, 0x37, 0x1d, 0x46, 0x46]

s = Solver()

flag = [BitVec("flag%i"%i, 8) for i in range(5)]



for i in range(0, 5):
	s.add((     (flag[i]<<(8-i)) | ((flag[i] >> (i+1 - 1))) == target[i]))

# => real:   (flag[i]<<(8-i)) | ((flag[i] >> (i+1 - 1))) 
# => fake:   (flag[i]<<(8-i + 1)) | ((flag[i] >> (i+1 - 1))) 

print(s.check())

m = s.model()

f = ""

for i in range(5):

	f+=(chr(m[flag[i]].as_long()))
