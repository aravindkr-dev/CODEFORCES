def Split(s):
	s = str(s)
	ls = []
	for x in s:
		ls.append(x)
	return ls
 
l = int(input())
s = Split(str(input()))
cnt = 0
for i in range(l):
	for j in range(l):
		if i != j and j == i+1 and i+1 < l:
			if s[i] == s[j] and '!' not in s[i]:
				cnt+=1
				s[i] += "!"
		else:
			pass
print(cnt)
	
