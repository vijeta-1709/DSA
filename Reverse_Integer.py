class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x <= 2**31 -1:
            negative = x<0
            x = abs(x)
            count = 0
            while x>0:
                ld = x%10
                count = count*10 + ld
                x = x//10

            if negative:
                count = -count

            return count
        
        else:
            return 0
        
C = Solution()
print(C.reverse(20))
print(C.reverse(-145))
print(C.reverse(58694))
