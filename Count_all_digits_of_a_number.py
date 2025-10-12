class Solution:
    def countDigit(self, n):
        count = 0
        while n>0:
            
            n = n//10
            count += 1
        return count
C = Solution()
print(C.countDigit(45))
print(C.countDigit(8))
