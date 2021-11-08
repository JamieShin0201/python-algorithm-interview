import collections
import re


def isPalindrome(s: str):
    strs = [char.lower() for char in s if char.isalnum()]
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def isPalindromeByDeque(s: str):
    strs = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def isPalindromeBySlicing(s: str):
    strs = re.sub('[^a-z0-9]', '', s.lower())
    return strs == strs[::-1]


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
    print(isPalindrome(" "))
    print(isPalindromeByDeque("A man, a plan, a canal: Panama"))
    print(isPalindromeBySlicing("A man, a plan, a canal: Panama"))
