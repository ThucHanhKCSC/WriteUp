from z3 import *

target = [0x9c, 0x8e,   0xa9, 0x89,   0x98, 0x8a,   0x9d, 0x8d,    0xd7, 0xcc,     0xdc, 0x8a, 0xa4, 0xce, 0xdf, 0x8f, 0x81, 0x89]
realTarget = []
xorVal = 0xBEEF
for i in range(0, len(target), 2):
	realTarget.append(target[i+1]<<8 | target[i])

s = Solver()

flag = [BitVec("flag%i"%i, 8*2) for i in range(0, 9)]

for i in range(0, 9):
	s.add(flag[i] ^  realTarget[i] == xorVal)

s.check()
m = s.model()

a = ""

for i in range(0, 9):
	print(m[flag[i]].as_long(), end = " ")


#ha: 0x39: d7
#	 0xde: cc
