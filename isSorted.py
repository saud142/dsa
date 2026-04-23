class Solution:
    def isSorted(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
        #your code goes here
       #We iterate from index 0 to n-2 because we compare each element with its next element (i+1).
#If we go till n-1, then i+1 would go out of bounds.
#So we stop one step early to safely compare all adjacent pairs.”
