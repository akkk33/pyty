"""
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium

Description:
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrings = []
        if not s:
            return 0
        for index, letter in enumerate(s):
            if not substrings:
                substrings.append(letter)
            elif letter in substrings[-1]:
                substrings.append(substrings[-1][substrings[-1].index(letter) + 1:] + letter)
            else:
                substrings[-1] += letter
        return len(max(substrings, key=len))


example = Solution()
print(example.lengthOfLongestSubstring("repeating"))
print(example.lengthOfLongestSubstring("aaaa"))
print(example.lengthOfLongestSubstring(""))

"""
My result:
Runtime: 84 ms, faster than 87.41% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""