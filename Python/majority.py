class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elementFrequency = {}
        for element in nums:
            if element in elementFrequency:
                elementFrequency[element] += 1
            else:
                elementFrequency[element] = 1

        majorityElement = 0
        maxFrequency = 0

        for element, frequency in elementFrequency.items():
            if frequency > maxFrequency:
                majorityElement = element
                maxFrequency = frequency
    
        return majorityElement
