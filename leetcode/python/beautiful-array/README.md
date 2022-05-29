An array nums of length n is beautiful if:

- nums is a permutation of the integers in the range [1, n].
- For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].

Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

Example 1:

    Input: n = 4
    Output: [2, 1, 4, 3]

Example 2:

    Input: n = 5
    Output: [3, 1, 2, 5, 4]

Constraints:

    1 <= n <= 1000

## Solutions
- Generally, the trick lies in already knowing the odd/even pattern

### Divide and Conquer
- The i, j pointers have to be either both odd or both even
- Thus, split the array into sub-arrays of all evens and odds - if the pointers lie in each of them, we are sound
- Then we need to recursively ensure this property for the sub-arrays
- This can be done by dividing by 2, i.e. right-shifting by one, and from the base case, we translate the values back
- Time: ?
- Space: ?

### Binary Reverse Sort
- Essentially the same as above, just cooler
- Time: ?
- Space: ?
