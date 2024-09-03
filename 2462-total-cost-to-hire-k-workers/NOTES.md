# Trick: Finding the Total Cost to Hire K Workers
​
## Key Insight
​
To efficiently find the total cost to hire `K` workers, use a two min-heap approach:
​
- **Two Min-Heaps**: Maintain two min-heaps to handle candidates from each side of the list (one for the smallest candidates from the left, and one for the smallest from the right).
- **Process**:
- Start by filling the heaps with initial candidates from each end of the list.
- Compare the smallest elements from both heaps.
- **Remove and Add**: Remove the smallest element from the appropriate heap and add its value to the total cost.
- **Move Pointers**: Adjust the pointers to the next candidates in the list and add them to their respective heaps.
- **Repeat** until you have hired `K` workers, always ensuring that the heaps are balanced and only the smallest elements are added to the total.
​
This approach allows you to dynamically select the least costly workers, efficiently managing the candidate pool using heaps.
​