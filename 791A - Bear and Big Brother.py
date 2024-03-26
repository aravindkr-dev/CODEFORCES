n = list(map(int , input().split(" ")))
a , b = n[0] , n[1]
a1 , b1 = int(a), int(b)
yrs = 0
for i in range(max(n)):
	if a1 > b1:
		break
	else:
		yrs+=1
		a1 *= 3
		b1 *= 2 
print(yrs)
