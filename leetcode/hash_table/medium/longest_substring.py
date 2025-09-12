# longest substring without repeating characters
# this one sucks

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0               # left edge of window
        max_len = 0

        for j, ch in enumerate(s):          # j is right edge
            while ch in seen:               # shrink until no duplicate
                seen.remove(s[i])
                i += 1
            seen.add(ch)                    # expand
            max_len = max(max_len, j - i + 1)
        return max_len

# I didn't even finish this on my own. I asked chatGPT for so many tips and hints after over an hour on this problem and then I 
# gave up and got the solution. Definitely not a good start to the medium problems, but theres thousands of them so I don't think
# it matters all too much. You live and you learn.