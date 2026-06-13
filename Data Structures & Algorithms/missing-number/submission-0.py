class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expectedTotal = 0
        for i in range(N + 1):
            expectedTotal += i
        
        actualTotal = 0
        for n in nums:
            actualTotal += n
        return expectedTotal - actualTotal