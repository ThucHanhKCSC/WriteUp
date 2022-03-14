target = [0x5e, 0x7d, 0x8a, 0xf3]
target.reverse()

a = 0

for i in range(len(target)):
	a <<= 8
	a |= target[i]

a &= 0xffffffff
a ^= 0xC0FE1337

b = 0
while(a > 0):
	b = a & 0xff
	a = a >> 8
	print(chr(b), end = "")
