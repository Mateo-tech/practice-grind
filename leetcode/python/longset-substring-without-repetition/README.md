Given a string s, find the length of the longest substring without repeating characters.

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


## Solutions

### Sliding Window
- Keep track of the seen characters and their indexes
- Point at the start of the substring
- If encountered a symbol that has already been seen, move the pointer by one
- Calculate the current length of the substrsing
- Time: O(n)
- Space: O(n)