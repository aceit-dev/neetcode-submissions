class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atLeast(g):
            if g == 0: return 0
            seen = dict()
            l = 0
            cnt = 0
            for r, v in enumerate(nums):
                if v not in seen:
                    seen[v] = 1
                else:
                    seen[v] += 1                

                while len(seen) > g:
                    seen[nums[l]] -= 1
                    if seen[nums[l]] == 0:
                        seen.pop(nums[l])
                    l += 1
                
                if len(seen) <= g:
                    cnt += r - l + 1
            return cnt


        return atLeast(k) - atLeast(k - 1)
