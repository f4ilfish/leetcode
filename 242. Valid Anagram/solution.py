from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char_frequency: Dict[str, int] = {}
        t_char_frequency: Dict[str, int] = {}
        
        for i in range(len(s)):
            if s[i] in s_char_frequency:
                s_char_frequency[s[i]] += 1
            else:
                s_char_frequency[s[i]] = 1
            
            if t[i] in t_char_frequency:
                t_char_frequency[t[i]] += 1
            else:
                t_char_frequency[t[i]] = 1
            
        if len(s_char_frequency) != len(t_char_frequency):
            return False
        
        for s_char, s_frequency in s_char_frequency.items():
            t_frequence = t_char_frequency.get(s_char, False)
            if not t_frequence or s_frequency != t_frequence:
                return False
        
        return True
