def check(str1, str2):
    len1= len(str1)
    len2=len(str2)
    if len1 > len2:
        return False
    if str2.startswith(str1):
        return str1 == str2[len2 - len1:]
    return False
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if check(words[i], words[j]):
                    count += 1

        return count

