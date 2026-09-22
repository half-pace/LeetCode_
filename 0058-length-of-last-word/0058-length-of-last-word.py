class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split() #["hello", "world"]
        size = len(new_s) #2
        for i in range(size):
            if i == size - 1:
                return len(new_s[i])
        
        
        