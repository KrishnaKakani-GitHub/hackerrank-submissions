# Sherlock and the Valid String
# Topic: String Manipulation
from collections import Counter


def isValid(s):
    counts = Counter(s)
    # frequency of frequencies: how many distinct chars share each count
    freqs = Counter(counts.values())
    # all chars already appear the same number of times
    if len(freqs) == 1:
        return "YES"
    # at most two distinct frequencies are fixable by one deletion
    if len(freqs) == 2:
        (f1, c1), (f2, c2) = sorted(freqs.items())
        # one char appears exactly once (delete it entirely)
        if f1 == 1 and c1 == 1:
            return "YES"
        # the higher frequency exceeds the lower by 1 and is unique (delete one occurrence)
        if f2 - f1 == 1 and c2 == 1:
            return "YES"
    return "NO"
