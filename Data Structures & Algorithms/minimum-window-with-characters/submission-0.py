from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        cNeed,cHave = Counter(t), Counter()
        need, have = len(cNeed), 0
        minStr = ""

        for r in range(len(s)):
          new = s[r]
          if new in cNeed:
            cHave[new] += 1
            if cHave[new] == cNeed[new]:
              have += 1

          while have == need and l <= r: 
            old = s[l]
            if not minStr or len(s[l: r+1]) < len(minStr):
              minStr = s[l: r+1]
            
            if old in cNeed:
              cHave[old] -= 1
              if cHave[old] < cNeed[old]:
                have -= 1
            
            l += 1

        

        return minStr
