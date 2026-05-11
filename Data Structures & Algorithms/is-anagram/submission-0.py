class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars=[]
        t_chars=[]
        for ch in s:
            s_chars+=ch
        for ch in t:
            t_chars+=ch
        if sorted(s_chars)==sorted(t_chars):
            return True
        else:
            return False