class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(need):
            if need == 0: return 0
            seen = defaultdict(int)
            l = cnt = have = 0
            for r, v in enumerate(nums):
                seen[v] += 1  
                # if v is a new value, update have 
                if seen[v] == 1:
                    have += 1
                # while have more than we need (invalid), l move right
                while have > need:
                    seen[nums[l]] -= 1
                    # when we removed a value from seen, we have 1 less
                    if seen[nums[l]] == 0:
                        have -= 1
                    l += 1

                # update window when have is at most need
                cnt += r - l + 1
            return cnt


        return atMost(k) - atMost(k - 1)
