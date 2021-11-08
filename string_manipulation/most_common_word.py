import collections
import re


# def mostCommonWord(paragraph: str, banned: list) -> str:
#     words = [
#         word
#         for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split()
#         if word not in banned
#     ]
#
#     counts = collections.defaultdict(int)
#     for word in words:
#         counts[word] += 1
#
#     return max(counts, key=counts.get)

def mostCommonWord(paragraph: str, banned: list) -> str:
    words = [
        word
        for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split()
        if word not in banned
    ]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
