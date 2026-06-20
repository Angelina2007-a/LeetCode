class Solution:
    def singleNumber(self, nums):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] == 1:
                return num
