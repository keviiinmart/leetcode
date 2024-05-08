class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        lastPosition = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[lastPosition] = nums1[m - 1]
                m = m - 1
            elif nums1[m - 1] == nums2[n - 1]:
                nums1[lastPosition] = nums2[n - 1]
                n = n - 1
            else:
                nums1[lastPosition] = nums2[n - 1]
                n = n - 1
            lastPosition = lastPosition - 1

        while n > 0:
            nums1[lastPosition] = nums2[n - 1]
            n, lastPosition = n - 1, lastPosition - 1

