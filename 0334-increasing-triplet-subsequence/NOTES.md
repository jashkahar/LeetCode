use 2 pointers from start and end
​
if i<k
check if there is any j
if not then move k
​
if i>k
move i
ptr1 = 0
ptr2 = len(nums)-1
​
```
while ptr1<ptr2:
if nums[ptr1] > nums[ptr2]:
ptr1 += 1
elif nums[ptr1] < nums[ptr2]:
for temp in nums[ptr1+1:ptr2]:
​
print(nums[ptr1],temp,nums[ptr2])
​
if(nums[ptr1]<temp<nums[ptr2]):
return True
ptr1 +=1
return False
```
​
​
​