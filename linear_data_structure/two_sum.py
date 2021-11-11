from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i, num in enumerate(nums):
#         complement = target - num
#
#         if complement in nums[i + 1:]:
#             return [nums.index(num), nums[i + 1:].index(complement) + (i + 1)]


# def twoSum(nums: List[int], target: int) -> List[int]:
#     nums_map = {}
#     for i, num in enumerate(nums):
#         nums_map[num] = i
#
#     for i, num in enumerate(nums):
#         if target - num in nums_map and i != nums_map[target - num]:
#             return [i, nums_map[target - num]]

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]

        nums_map[num] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
