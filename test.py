
vlist = []
timelist = []
def fun(v, t, T = 0):
	from math import e
	mlist = []
	if T != 0:
		
		vlist.append(v)
		timelist.append(t)	
	else:
		vlist.append(v)
		timelist.append(t)
		for i in range(len(vlist)):
			vlist[i] = vlist[i] * (e**(timelist[i]-T))
		for j in range(len(vlist)):
			mlist.append(vlist[j] // 1)
		myset = set(mlist)
		for item in myset:
			print("%d ~ %d: %d" %(item,item+1,mlist.count(item)))	
 
k = 4
for j in range(4):
	k -= 1
	fun(2, 3, k)
