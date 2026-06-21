# HackerRank -> Sales by Match (a.k.a. Sock Merchant)
# Topic: Dictionaries and Hashmaps (Warm-up)
# Pattern: frequency count -> floor-divide each count by 2 for pairs
# Time: O(n)   Space: O(k) where k = distinct colors

from collections import Counter


def sockMerchant(n: int, ar: list[int]) -> int:
    count = Counter(ar)
    pairs = 0
    for c in count.values():
        pairs += c // 2
    return pairs
