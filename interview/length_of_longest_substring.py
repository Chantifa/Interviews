class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        for i in enumerate(s):
            if not substring.contains(s[i]):
                substring += s[i]
            return len(substring)
        