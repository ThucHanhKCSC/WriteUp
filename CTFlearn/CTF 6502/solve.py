flag = [
0x4B,0x5C,0x4E,0x64,0x6D,0x69,0x7A,0x66]  

flag2 = [
0x73,0x60,0x38,0x65,0x3B,0x57,0x6B,0x38,
            0x65,0x78,0x7D,0x7C,0x3B,0x7A,0x57,0x7A,
            0x3B,0x7E,0x38,0x64,0x7D,0x7C,0x39,0x38,
            0x66,0x75]
count = 0
count2 = 0
for i in flag:
	if(count == 3):
		count = 0
		print(chr(i+8), end = "")
	else:
		count += 1
		print(chr(i-8), end = "")

al = "++-+-+--+-----+----+----++"
count = 0
count2 = 0
for i in range(len(flag2)):
		if(al[i] == "+"):
			print(chr(flag2[i]+8), end = "")
		else:
			print(chr(flag2[i]-8), end = "")


