from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least
        twice in the array, and return false if every element is distinct.

        Example 1:
        Input: nums = [1,2,3,1]

        Output: true

        Explanation:

        The element 1 occurs at the indices 0 and 3.

        Example 2:
        Input: nums = [1,2,3,4]

        Output: false

        Explanation:

        All elements are distinct.

        Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]

        Output: true

        
        Constraints:

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
        """
        appears = {}
        for number in nums:
            if number in appears:
                return True
            appears[number] = number
        return False
    
    def containsDuplicatePythonAproach(self, nums: List[int]) -> bool:
        """
        Python version: the previous version can be improved using Python's
        built-in utilities. In Python, a set does not contain duplicate
        elements. If we create a set by passing the `nums` list as an argument,
        it will not include any duplicate elements. Comparing the lengths of the
        set and the list will reveal a difference if there were duplicates.
        """
        return len(set(nums)) != len(nums)

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicatePythonAproach(nums))

nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicatePythonAproach(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicatePythonAproach(nums))

nums = [1,1]
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicatePythonAproach(nums))
