class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for num in nums:
            total = max(num + first, second)
            first = second
            second = total
        return second