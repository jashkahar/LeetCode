class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1
        
        # Step 1: Convert string to a list of characters
        s = list(s)
        
        # Step 2: Reverse the entire list of characters
        reverse(0, len(s) - 1)
        
        # Step 3: Reverse each word
        i = 0
        while i < len(s):
            if s[i] != ' ':
                start = i
                while i < len(s) and s[i] != ' ':
                    i += 1
                reverse(start, i - 1)
            i += 1
        
        # Step 4: Remove extra spaces and return the result
        return ' '.join(''.join(s).split())
        # # x = s.split()
        # # print(x)
        # # return " ".join(x[::-1])
        # l = s.split(' ')
        # rev=[]
        # word=0
        # space=0
        # for i in reversed(l):
        #     # print(i)
        #     # if i=='':
        #         # print('blank space')
        #     if(i=='' and word == 0 and space == 0):
        #         # print('Blank space not needed', word, space)
        #         word=0
        #         space=1
        #     elif(i=='' and word == 0 and space == 1):
        #         # print('Blank space not needed', word, space)
        #         word = 0
        #         space=1
        #     elif(i=='' and word == 1 and space == 0):
        #         # print('Blank space not needed', word, space)
        #         # rev.append(i)
        #         word = 0
                
        #     else:
        #         # print(i,' -->word', word, space)
        #         rev.append(i)
        #         word=1
        #         space=0
        # return ' '.join(rev)
        # # return rev
