seen = set()
li = list(s)
l,r = 0,0
res = 0
while l<r and r < len(s):
if li[r] in seen:
seen.remove(li[l])
l+=1
r+=1
elif li[r] not in seen:
seen.add(li[r])
res = max(res, r-l+1)
r+=1
return res