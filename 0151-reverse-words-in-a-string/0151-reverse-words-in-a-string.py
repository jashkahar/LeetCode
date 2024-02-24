class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        rev=[]
        word=0
        space=0
        for i in reversed(l):
            # print(i)
            # if i=='':
                # print('blank space')
            if(i=='' and word == 0 and space == 0):
                print('Blank space not needed', word, space)
                word=0
                space=1
            elif(i=='' and word == 0 and space == 1):
                print('Blank space not needed', word, space)
                word = 0
                space=1
            elif(i=='' and word == 1 and space == 0):
                print('Blank space not needed', word, space)
                # rev.append(i)
                word = 0
                
            else:
                print(i,' -->word', word, space)
                rev.append(i)
                word=1
                space=0
        return ' '.join(rev)
        # return rev