class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seen = deque()
        res = []
        for rb,v in enumerate(nums):
            lb = rb - k + 1
            while seen and (seen[0][0] < lb):
                seen.popleft()

            while seen and (v > seen[-1][1]):
                seen.pop()
            
            seen.append((rb, v))
            if seen and lb >= 0 and rb - lb + 1 == k:
                res.append(seen[0][1])
        return res


            