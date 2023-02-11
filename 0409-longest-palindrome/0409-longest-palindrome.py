class Solution:
    def longestPalindrome(self, s: str) -> int:
        mySet = set(s)
        countOfChars = dict()
        for element in mySet:
            countOfChar = s.count(element)
            countOfChars[element] = countOfChar
            #print("Count of character '{}' is {}".format(element, countOfChar))

        print(len(s))
        print(countOfChars)

        maxlen = 0
        oddnum = 0
        flag =  True
        for element in countOfChars:
            if countOfChars[element] % 2 == 0:
                maxlen += countOfChars[element]
                # print(element, ",", countOfChars[element])
                # print("maxlen: ", maxlen)
            elif countOfChars[element] % 3 == 0:
                maxlen += countOfChars[element] -1
                # print(element, ",", countOfChars[element])
                # print("maxlen: ", maxlen)
                if oddnum == 0:
                    oddnum = 1
            elif countOfChars[element] % 5 == 0:
                maxlen += countOfChars[element] -1
                # print(element, ",", countOfChars[element])
                # print("maxlen: ", maxlen)
                if oddnum == 0:
                    oddnum = 1
            elif countOfChars[element] % 7 == 0:
                maxlen += countOfChars[element] -1
                # print(element, ",", countOfChars[element])
                # print("maxlen: ", maxlen)
                if oddnum == 0:
                    oddnum = 1
            elif countOfChars[element] == 1:
                if oddnum == 0:
                    oddnum = 1
            else:
                # print(countOfChars[element])
                maxlen += countOfChars[element] -1
                if oddnum == 0:
                    oddnum = 1


        print(maxlen)

        return maxlen + oddnum
        

