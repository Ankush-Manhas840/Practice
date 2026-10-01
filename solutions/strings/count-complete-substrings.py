def count_checker(hashmap, k):
    for a in hashmap.values():
        if a != k:
            return False
    return True

def checker(s):
    hashmap = dict()
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1
    return hashmap

def diff_checker(sub):
    for i in range(1, len(sub)):
        if abs(ord(sub[i]) - ord(sub[i-1])) > 2:
            return False
    return True

def len_checker(word, k):
    total = 0
    n = len(word)
    for num_len in range(1, 27):
        L = num_len * k
        if L > n:
            break

        sub = word[0:L]
        hashmap = checker(sub)

        diff_bad = 0
        for i in range(1, L):
            if abs(ord(word[i]) - ord(word[i-1])) > 2:
                diff_bad += 1

        if count_checker(hashmap, k) and diff_bad == 0:
            total += 1

        for start in range(1, n - L + 1):
            left = word[start - 1]
            hashmap[left] -= 1
            if hashmap[left] == 0:
                del hashmap[left]
            right = word[start + L - 1]
            hashmap[right] = hashmap.get(right, 0) + 1

            if abs(ord(word[start]) - ord(word[start-1])) > 2:
                diff_bad -= 1
            if abs(ord(word[start+L-1]) - ord(word[start+L-2])) > 2:
                diff_bad += 1

            if count_checker(hashmap, k) and diff_bad == 0:
                total += 1
    return total


class Solution(object):
    def countCompleteSubstrings(self, word, k):
        return len_checker(word, k)
