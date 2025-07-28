from collections import defaultdict
from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_frequency_to_strings: Dict[str, List[str]] = defaultdict(list)
        
        for string in strs:
            chars_frequency = [0] * 26
            for char in string:
                i = ord(char) - 97
                chars_frequency[i] += 1
            frequency_key = ".".join(map(str, chars_frequency))
            chars_frequency_to_strings[frequency_key].append(string)
        
        return list(chars_frequency_to_strings.values())
