Brute force approach would be to iterate the string in reverse and move the pointer `i` till we find a non space character.
​
Once found we can iterate till we find another white space and maintain a counter, as soon as we find a space, we return the counter as it will be the length of the last word.