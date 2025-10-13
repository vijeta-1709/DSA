class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check 32-bit range
        if -2**31 <= x <= 2**31 - 1:
            if x < 0:  # Negative numbers are not palindromes
                return False

            original = x  # Store the original number
            reversed_num = 0

            while x > 0:
                ld = x % 10
                reversed_num = reversed_num * 10 + ld
                x = x // 10

            return original == reversed_num

        else:
            return False
