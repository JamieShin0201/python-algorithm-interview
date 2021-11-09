import collections


def groupAnagrams(strs: list) -> list:
    anagrams = collections.defaultdict(list)
    for str in strs:
        anagrams[''.join(sorted(str))].append(str)

    return list(anagrams.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
