#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1

def move_zeroes(arr):
    n = len(arr)
    left = 0  # Pointer for the leftmost non-zero element

    # Iterate through the array
    for i in range(n):
        if arr[i] != 0:
            # Swap the non-zero element with the leftmost non-zero element
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    return arr
