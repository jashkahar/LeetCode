class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if(str1+str2 != str2+str1):
            return ''
        smallest = min(str1, str2)
        maximum = max(str1, str2) 
        #print(smallest)
        if smallest == maximum:
            return smallest

        if(smallest+smallest == maximum):
            return smallest

       
        res= ''
        for i in range(len(smallest)-1, 0, -1):
            # print(smallest[:i]*2,"twice")
            if((smallest[:i]*(len(smallest)//len(smallest[:i])))==smallest and (smallest[:i]*(len(maximum)//len(smallest[:i])))==maximum):
                print(smallest[:i])
                res=smallest[:i]
                return res
        # return res

        
        