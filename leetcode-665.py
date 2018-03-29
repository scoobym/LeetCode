class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])

temp = Solution()
nums1 = [2,4,4,2,2]
nums2 = [2,4,4,2]
print(temp.checkPossibility(nums1))
print(temp.checkPossibility(nums2))
