class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitsA = int(a[i]) if i < len(a) else 0
            digitsB = int(b[i]) if i < len(b) else 0
            
            total = digitsA + digitsB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
            
        if carry:
            res = "1" + res
        return res
            
        
#         templist=[]
        
#         carry = 0
        
#         if len(a) == len(b):
#             pass
#         elif len(a) > len(b):
#             b = "0" * (len(a)-len(b)) + b
#         elif len(b) > len(a):
#             a = "0" *(len(b)-len(a)) + a
        
#         la = list(a)
#         la.reverse()
#         lb = list(b)
#         lb.reverse()
        
#         #print(la)
#         #print(lb)
        
#         for i in range(len(la)):
#             if int(la[i])+int(lb[i])+carry == 0:
#                 carry=0
#                 templist.append('0')
#                 #print("0+0")
#             elif int(la[i])+int(lb[i])+carry == 1:
#                 templist.append('1')
#                 #print("0+1")
#                 carry=0
#             elif int(la[i])+int(lb[i])+carry == 2:
#                 templist.append('0')
#                 #print("1+1")
#                 carry=1
#             elif int(la[i])+int(lb[i])+carry == 3:
#                 templist.append('1')
#                 #print("1+1+1")
#                 carry=1
            
                
#         if carry == 1:
#             templist.append('1')
#         #print(templist)
        
        
#         templist.reverse()
#         res = ''.join(templist)
        
#         #print(res)
#         return res
        