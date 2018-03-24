class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        temp = copy.copy(nums)
        lens = len(nums)
        k = k%lens
        for i in range(lens):
            nums[(i+k)%lens] = temp[i]
