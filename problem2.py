a=list()
print(" enter 10 numbers")
for i in range(0,10):
	a.append(input())
ele=5
for i in range(0,10):
	if(int(a[i])<ele):
		print(a[i])