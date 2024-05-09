#189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = []            
        # for index in range(len(nums)):
        #     if len(nums) > k:
        #         val = index - k
        #         temp.append(nums[val])
        #     else:
        #         temp.append(nums[index])
        # nums.clear()
        # nums.extend(temp)
        #####LIST SLICING#### 
        if len(nums) == 1:
            pass
        elif k < len(nums):
            nums[:] = nums[-k:] + nums[:-k]
        elif k > len(nums):
            value = k % len(nums)
            nums[:] = nums[-value:] + nums[:-value]            
        elif k == len(nums):
            pass
