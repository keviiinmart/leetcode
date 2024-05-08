#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index in range(len(nums)):
            if val in nums:
                nums.remove(val)
                k += 1
