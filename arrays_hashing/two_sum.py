# Problem: Two Sum
# Pattern: HashMap
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in previous:
                return [previous[diff], i]
            
            previous[n] = i
        
        return []


# 🔥 Driver code
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.twoSum([2,7,11,15], 9))   # [0,1]
    print(sol.twoSum([3,2,4], 6))       # [1,2]
    print(sol.twoSum([3,3], 6))         # [0,1]