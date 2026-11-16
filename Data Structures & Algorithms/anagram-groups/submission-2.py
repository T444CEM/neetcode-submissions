class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        chars = {}

        for word in strs:
            sorted_word = sorted(word)
            sorted_string = "".join(sorted_word)

            if sorted_string not in chars:
                chars[sorted_string] = [word]
            else:
                chars[sorted_string].append(word)
            
        return list(chars.values())

                    


