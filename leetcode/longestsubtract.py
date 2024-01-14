class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1

            char_index_map[s[end]] = end

            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length


solution_instance = Solution()
result = solution_instance.lengthOfLongestSubstring("abcabcbb")
print(result)
