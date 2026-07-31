class Solution:
    def majorityElement(self, nums: list[int]) -> int:
       count = {}
       Limit = len(nums) // 2
       print(Limit)
       for i in nums:
          if i in count:
            count[i] += 1
          else:
              count[i] = 1     

          if count[i] > Limit:
                 return i