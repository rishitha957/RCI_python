li = []
with open("sample.txt","r") as f:
	li = f.readlines()

for i in range(len(li)):
	li[i] = li[i].split(" ")

start = input()
start = int(start,16)
end = input()
end = int(end,16)

d = {}

res = list(filter(lambda x:int(x[2]+x[3],16)>start and int(x[2]+x[3],16)<end,li))
for i in range(len(res)):
	a = int(res[i][2]+res[i][3],16)
	b = " ".join(j for j in res[i])
	d[a] = b

#print(d)
li2 = list(d.keys())
list.sort(li2)
sorted_packets = []
for i in li2:
	sorted_packets.append(d[i])

with open("sorted_packets_in_range.txt","w") as f1:	
	for i in sorted_packets:
		f1.write("%s"%i)
