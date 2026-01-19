class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = []

        # Use first string as reference
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check if this character exists at position i in ALL strings
            for s in strs[1:]:
                # If string is too short OR character doesn't match
                if i >= len(s) or s[i] != char:
                    return "".join(prefix)

            # Character matches in all strings
            prefix.append(char)

        return "".join(prefix)