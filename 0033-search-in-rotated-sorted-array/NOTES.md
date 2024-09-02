​
3. **Determine the Search Half**:
- If the target is greater than `mid`, the potential search area is the right half of the array.
- If the target is smaller than `mid`, further checks are needed:
- Compare the `left` pointer's value with the target.
- If the value at `left` is smaller than the target, this indicates that the left portion is sorted and contains the target. So, search the left half.
- If not, search the right half as the target may be in the rotated portion.
​
4. **Adjust Pointers**:
- Adjust `left` or `right` pointers based on the above checks to narrow down the search space to the half where the target lies.
​
5. **Repeat Until Found**:
- Continue the process until the target is found or the search space is exhausted.
​
## Why It Works
​
- The approach takes advantage of the properties of the rotated sorted array: one half of the array is always sorted.
- By comparing the mid, left, and right values, the algorithm correctly identifies which half to discard, maintaining the logarithmic search time.
​
## Summary
​
This modified Binary Search effectively handles rotated sorted arrays by adapting the search criteria based on comparisons with the mid element and the known sorted half of the array. This ensures that the search remains within **O(log n)** time complexity, providing an optimal solution for finding the target.
​