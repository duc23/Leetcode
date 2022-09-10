class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # loop through all #'s
        for i in range(len(nums)):
            # loop through all #'s starting with the next index over
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j]) # return a list of the two indices 