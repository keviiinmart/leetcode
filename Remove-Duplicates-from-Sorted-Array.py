# Leetcode 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        li = []
        for num in nums:
            if num not in li:
                li.append(num)
        nums.clear()
        nums.extend(li)
        return len(nums) 
