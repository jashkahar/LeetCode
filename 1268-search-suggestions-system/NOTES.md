# Trick: Search Suggestions System Using Sorting and Two-Pointer Approach
​
## Key Insight
​
Instead of using a Trie, we can simplify the problem by:
​
- **Sorting the Product List**: Sort the products in lexicographical order to make it easier to find suggestions in the required order.
- **Two-Pointer Technique**: Use two pointers to efficiently find the range of products that match the current search prefix:
- Move the left pointer to skip products that don't match the prefix.
- Adjust the right pointer to limit the range to relevant products.
- This approach allows us to build the search suggestions efficiently without the complexity of Trie data structures.
​