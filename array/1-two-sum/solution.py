class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}
    for index,num in enumerate(nums):
        new_target = target - num
        if new_target in seen:
            return[seen[new_target],index]
        seen[num] = index






solution = Solution()

nums = [2,3,4,5,6]
target = 9
answer = solution.twoSum(nums,target)
print(answer)
