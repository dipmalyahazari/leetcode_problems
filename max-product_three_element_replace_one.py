# Input: nums = [-5,7,0]
#
# Output: 3500000
#
# Explanation:
#
# Replacing 0 with -105 gives the array [-5, 7, -105], which has a product (-5) * 7 * (-105) = 3500000. The maximum product is 3500000.
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_1=0
        max_2=0
        for i in range(len(nums)):
            if abs(nums[i])>=abs(max_1):
                max_2=max_1
                max_1=nums[i]
            elif abs(nums[i])>=abs(max_2):
                max_2=nums[i]
        product=abs(max_1)*abs(max_2)*(10**5)

        return product  

s=Solution()
print(s.maxProduct([-5,7,0]))
