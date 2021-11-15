from typing import List


# def trap(height: List[int]) -> int:
#     result = 0
#     n = len(height)
#
#     for i in range(1, n - 1):
#
#         left = height[i]
#         for j in range(0, i):
#             left = max(left, height[j])
#
#         right = height[i]
#         for j in range(i + 1, n):
#             right = max(right, height[j])
#
#         result += min(left, right) - height[i]
#     return result

# def trap(height: List[int]) -> int:
#     if not height:
#         return 0
#
#     volume = 0
#     left = 0
#     right = len(height) - 1
#     left_max = height[left]
#     right_max = height[right]
#
#     while left < right:
#         left_max = max(left_max, height[left])
#         right_max = max(right_max, height[right])
#
#         if left_max <= right_max:
#             volume += (left_max - height[left])
#             left += 1
#         else:
#             volume += (right_max - height[right])
#             right -= 1
#
#     return volume

def trap(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
