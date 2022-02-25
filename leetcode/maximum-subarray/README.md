# Solutions

## Brute-force
- Nested loops over all subarrays and keeping track of the maximum sum
- Time: O(n^2)
- Space: O(1)

## Kadane Algorithm
- Loop over the array and sum the elements, keep track of the maximum sum so far (update only if the current sum is higher)
- Time: O(n)
- Space: O(1)

## Divide-and-Conquer
- The subarray either lies in the left half, right half or it's crossing the midpoint
- Thus, recursively find maximum in the left half and right half, and looping over the array between the current left/right points accross the midpoint
- Return the maximum of these
- Time: O(nlogn), 2T(n/2) + O(n) (recurrence relation)
- Space: O(1)
