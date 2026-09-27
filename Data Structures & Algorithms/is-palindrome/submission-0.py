class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for c in s:
            if c.isalnum():
                check += c.lower()

        n = len(check)
        for i in range(n // 2):
            if check[i] != check[n - i - 1]:
                return False
        return True        
        