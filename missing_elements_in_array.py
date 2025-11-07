# Input: nums = [1,4,2,5]
#
# Output: [3]
class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        missingnumbers:list[int]=[]
        min_number,max_number=min(nums),max(nums)
        for i in range(min_number,max_number+1):
            if i not in set(nums):
                missingnumbers.append(i)
        return missingnumbers
