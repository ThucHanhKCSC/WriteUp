target = [0x59, 0x1, 0x57, 0x67, 0x6, 0x41, 0x78, 0x1, 0x65, 0x2d, 0x7b, 0x0e, 0x57, 0x3, 0x68, 0x5d, 0x7, 0x69, 0x23, 0x55, 0x37, 0x60, 0x14, 0x7e, 0x1d, 0x2f, 0x62, 0x5f, 0x62, 0x5f]

print(chr(0x59),end = "")
for i in range(1, len(target)):
	print(chr(target[i] ^ target[i-1]), end= "")
	
