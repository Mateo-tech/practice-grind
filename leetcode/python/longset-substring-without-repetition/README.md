# Solutions

## Sliding Window
- Keep track of the seen characters and their indexes
- Point at the start of the substring
- If encountered a symbol that has already been seen, move the pointer by one
- Calculate the current length of the substrsing
- Time: O(n)
- Space: O(n)