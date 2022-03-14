from z3 import *

encrypt_flag = [0x10, 0x27, 0xbc, 0x9, 0x0e, 0x17, 0xba, 0x4d, 0x18, 0xf, 0xbe, 0xab]


flag = [BitVec("flag%i" %i, 8) for i in range(0, 12)]

s = Solver()

for i in range(0, 12):
	s.add(  ((flag[i] << 1) | 1) ^ (0xcd+i) == encrypt_flag[i]   )



print(s.check())

m = s.model()

tflag = ""

for i in range(0,12):
	tflag += chr(m[flag[i]].as_long())

print(tflag)
