# Solutions

## Brute-force
- Simply nested for loops; checking each number against the rest
- Time: O(n^2)
- Space: O(1)

## Sorting
- Sorting the array beforhand and then checking the next/previous element
- Time: O(nlogn) (depends on the algorithm)
- Space: O(1) (depends on the algorithm)

## HashSet
- Check if element is already in the set, as it can't contain duplicates
- Can check for the return value upon insertion
- Time: O(n)
- Space: O(n)

## HashSet v2
- As shown in C++, can copy the set directly and compare sizes
- Set would be smaller if the array contained duplicates
- Time: O(n)
- Space: O(n)

