class Solution:

    def __init__(self):
        self.hashMap = {}

    def numTrees(self, n: int) -> int:
        ans = 0

        if n == 0 or n == 1:
            return 1

        for i in range(1, n + 1):
            leftCount = (i - 1)
            rightCount = (n - leftCount - 1)

            if not leftCount in self.hashMap:
                self.hashMap[leftCount] = self.numTrees(leftCount)
            
            if not rightCount in self.hashMap:
                 self.hashMap[rightCount] = self.numTrees(rightCount)

            ans += self.hashMap[leftCount] * self.hashMap[rightCount]

        return ans

"""
n = 3

1,        2,         3

#1
1 
  2
3

1
  2
    3

#2
   2
1.     3

#3
    3
   1
  2
    
    3
  1
    2

Time: O(n ^ 2)
Space: O(n)
"""
