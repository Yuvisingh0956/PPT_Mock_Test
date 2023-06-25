#!/usr/bin/env python
# coding: utf-8

# In[17]:


def first_unique_character(s):
    char_freq = {}

    # Count the frequency of each character in the string
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the first non-repeating character and return its index
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    # If no non-repeating character is found, return -1
    return -1

