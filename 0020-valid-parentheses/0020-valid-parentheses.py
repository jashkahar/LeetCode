class Solution:
    def isValid(self, s: str) -> bool:
        temp_list = list(s)

        parathesis = {']':'[', '}':'{', ')':'('}
        
        stack = []

        for char in s:
            if char in ["[", "{", '(']:
                stack.append(char)
            else:
                if stack and parathesis[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        
        # for i in range(len(temp_list)):
        #     #print("element added: ",temp_list[i])
        #     if(temp_list[i] in ('(' ,'{','[' )):
        #         stack.append(temp_list[i])
        #         #print("current stack: ",stack)
        #     elif(temp_list[i] in (')','}' ,']' )):
        #         #print("-Closing bracket detected-")
        #         if(stack == []):
        #             return False
        #         elif(temp_list[i] == ')'):
        #             if(stack[-1] == '('):
        #                 stack.pop()
        #                 #print("Element () removed" )
        #             else:
        #                 return False
        #         elif(temp_list[i] == '}'):
        #             if(stack[-1] == '{'):
        #                 stack.pop()
        #                 #print("Element {} removed" )
        #             else:
        #                 return False    
        #         elif(temp_list[i] == ']'):
        #             if(stack[-1] == '['):
        #                 stack.pop()
        #                 #print("Element [] removed" )
        #             else:
        #                 return False
        #     i=i+1
            
        # # print("after process",stack)
        # if(stack == []):
        #     return True
        # else:
        #     return False
                    
        
        
        
    
        
        
        