from pwn import *
# the first step is probably finding the right format of the flag, without the "a" and "d", the flag checker won't work

#case = "T.m.............a.........b.....................}"
'''
case = [
"................................}",
"..........................b.....}",
"........................d.......}",
"........................d.b.....}",
"................a...............}",
"................a.........b.....}",
"................a.......d.......}",
"................a.......d.b.....}",
"..m.............................}",
"..m.......................b.....}",
"..m.....................d.......}",
"..m.....................d.b.....}",
"..m.............a...............}",
"..m.............a.........b.....}",
"..m.............a.......d.......}",
"..m.............a.......d.b.....}",
"T...............................}",
"T.........................b.....}",
"T.......................d.......}",
"T.......................d.b.....}",
"T...............a...............}",
"T...............a.........b.....}",
"T...............a.......d.......}",
"T...............a.......d.b.....}",
"T.m.............................}",
"T.m.......................b.....}",
"T.m.....................d.......}",
"T.m.....................d.b.....}",
"T.m.............a...............}",
"T.m.............a.........b.....}",
"T.m.............a.......d.......}",
"T.m.............a.......d.b.....}"
][::-1]
'''
#warnings.filterwarnings('ignore', module='foo')

case = "CTFlearn{1................a.......d........}"

#print(len(kernel))

#flag = rawflag + kernel + "}"

testcase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+=_{}?./~`|"

#context.log_level = "critical"

p = process(["gdb", "./Rouen"])
p.recvuntil("gef➤  ")

p.sendline("b *0x5555555559ba")
p.recvuntil("gef➤  ")

i = 0
found = 0
count = len(testcase) + 1

rawflag = "CTFlearn{1"
loop = len(rawflag) - 9

numcase = 0
#exit()
while(1):
	count = len(testcase) + 1
	flag = rawflag
	for j in testcase:
		#print(j)
		#flag = rawflag + j + "1"*(0x30 - i) + "}"
		#flag = rawflag + j + case[numcase]
		flag = rawflag + j + "................a.......d........}"
		p.sendline("run " + flag)
		print("flag" + ": " + flag +": ", end = "")
		p.recvuntil("gef➤  ")
		
		for test in range(loop):
			p.sendline("c")
			p.recvuntil("gef➤  ")
		
		#print(b)
		p.sendline("p $eflags")
		a = p.recvuntil("gef➤  ")

		print(a.decode("utf-8"), end = "\n\n")
		if("ZF" in str(a) or "ZF" in a.decode("utf-8")):
			rawflag += j
			print("\n\n\n\n\n\n\nRAWFLAG HERERERERE: " + rawflag + "\n\n\n\n\n\n")
			i+=1
			found += 1
			#p.sendline("c")
			exit()
			break
		count -= 1
		print(count, end = ": count\n")
		if(count == 1):
			if(found == 0):
				numcase += 1
				print("\n\n\n\n\nCASE INCREATED\n\n\n\n\n\n")


print("no solve")
