the trick:
We have to find every single solution - brute force - backtracking
​
first map the number to the characters.
​
then for each char in the current digit recuresively call backtrack and build the string
​
stop when the current string lenght is eaqal to the lenght of digits given
​
Time complexity: O(4^n)
​
​
​