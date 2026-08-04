class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            # Expand the window by adding s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # Current window size is (right - left + 1)
            # If replacements needed exceed k, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update maximum window length seen so far
            max_length = max(max_length, right - left + 1)

        return max_length