class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            bit = (n >> i) & 1
            res ^= bit
        return res