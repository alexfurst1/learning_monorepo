#Write a function to find the longest common prefix string amongst an array of strings. 
# If there is no common prefix, return an empty string "".

def common_prefix(self, strs: List[str]) -> str:
    counter = 0
    for str in strs:
        help = 1