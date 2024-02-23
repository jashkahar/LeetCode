class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        st=list(s)
        stvowels=[]
        for i in range(len(st)):
            if st[i] in vowels:
                stvowels.append(st[i])
        for i in range(len(st)):
            if st[i] in vowels:
                st[i]=stvowels[-1]
                stvowels.pop()
        return ''.join(st)


            
