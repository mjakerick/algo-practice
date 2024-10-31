class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        oneSorted = sorted(s)
        twoSorted = sorted(t)
        if oneSorted == twoSorted:
            return True
        else:
            return False
        
print(Solution().isAnagram(s = "racecar", t = "carrace"))
print(Solution().isAnagram(s = "jar", t = "jam"))