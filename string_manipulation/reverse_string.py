# def reverseString(s):
#     s[::-1]

# def reverseString(s: list):
#     s.reverse()


def reverseString(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"];
    reverseString(s)
    print(s)
