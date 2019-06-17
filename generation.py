import random

header = "55 AA "
inc = 0xc304
li = []
for i in range(20):
	a = f"{inc :x}"
	#str = [f"{random.rand_int() :x"}" for j in range(19):]
	str = ""
	for j in range(19):
		b = f"{random.randint(0,pow(16,2)-1):x}"
		b = f"{b:0>2}"
		c = b[:2].upper()+" "
		str = str + c
	li.append(f"{header}{a[:2].upper()} {a[2:].upper()} {str}"+'00 '*7)
	inc = inc + 1

for i in range(30):
	str = ""
	for j in range(21):
		b = f"{random.randint(0,pow(16,2)-1):x}"
		b = f"{b:0>2}"
		c = b[:2].upper()+" "
		str = str + c
	li.append(f"{header}{str}"+'00 '*7)
"""
for i in li:
	print(i)
"""
random.shuffle(li)

with open("sample.txt","w") as f:
	for packet in li:
		f.write("%s\n"%packet)
print("Text file is created")