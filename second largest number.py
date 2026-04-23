class Solution:
    def secondLargestElement(self, nums):
        largestelemnt = float('-inf')
        secondLargestElement = float('-inf')
        
        for num in nums:
            if num > largestelemnt:
                secondLargestElement = largestelemnt
                largestelemnt = num
            elif num < largestelemnt and num > secondLargestElement:
                secondLargestElement = num

        if secondLargestElement == float('-inf'):
            return None

        return secondLargestElement
