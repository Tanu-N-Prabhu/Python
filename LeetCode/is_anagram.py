"""
Check if two string is anagram
"""

class Solutions:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

if __name__=="__main__":
    s = Solutions()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
    print(s.isAnagram("aacc", "ccac"))
    print(s.isAnagram("aacc", "ccac"))
    