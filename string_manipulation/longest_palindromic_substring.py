# def longestPalindrome(s: str) -> str:
#     result = ""
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             word = s[i:j]
#             if word == word[::-1] and len(result) < len(word):
#                 result = word
# 
#     return result


def longestPalindrome(s: str):
    def expand(left: int, right: int, s: str):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]
    
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    for i in range(len(s)):
        result = max(result, expand(i, i + 1, s), expand(i, i + 2, s), key=len)

    return result


if __name__ == "__main__":
    print(longestPalindrome("babad"))
