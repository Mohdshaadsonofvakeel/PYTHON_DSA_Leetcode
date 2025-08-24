from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition in nums1
            j = total_left - i       # partition in nums2
            
            nums1_left_max  = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf')  if i == m else nums1[i]
            nums2_left_max  = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf')  if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Found correct partition
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + 
                            min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
        
        # Should never reach here if inputs are valid
        raise ValueError("Input arrays are not sorted or invalid")
