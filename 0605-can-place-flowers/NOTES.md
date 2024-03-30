A more simpler approach would be to assume the edges of the list have an empty spot (we can even add a zero at the begining and the end and it wont cange the problem).
​
we can plant a flower at `i` if `i-1` and `i+1` are empty and decrementing the value of `n` by 1 every time we find a spot and end as soon as` n == 0`.