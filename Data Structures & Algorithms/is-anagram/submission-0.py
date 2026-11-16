class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

        for char in t:
            if char in chars:
                if chars[char] > 0:
                    chars[char] -= 1
                else:
                    return False
            else:
                return False
        
        for char in chars:
            if chars[char] != 0:
                return False
        
        return True
