class Solution:
    def twoSum(self, nums, target):
        
          for i in range(len(nums)):
              for j in range(i+1,len(nums)):
                  if((nums[i]+nums[j])==target):
                      result = [i,j]
                      return result
test = Solution()
nums = [3,2,4]
target = 6
print(test.twoSum(nums,target))