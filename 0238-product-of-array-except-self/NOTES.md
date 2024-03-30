A simpler approach would be to use 2 lists `prefix` and `postfix`.
​
with `1` in the 0th place, iterate the nums list and store the product of each with the previous prefix and append it to `prefix`.
​
then iterate the nums list in reverse and get the product of the position and the postfix and append it to `postfix`.
​
now simply just multiply the prefix and postfix for each positions to get the result.