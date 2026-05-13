# Problem: Top K Frequent Elements
# Pattern: Bucket Sort
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res


# 🔥 Driver code
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
    print(sol.topKFrequent([1], 1))            # [1]