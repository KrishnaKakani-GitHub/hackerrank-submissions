# Ransom Note
# Topic: Dictionaries and Hashmaps
from collections import Counter


def checkMagazine(magazine, note):
    mag_count = Counter(magazine)
    note_count = Counter(note)
    # for loop with tuple unpacking: word = key, needed = its count
    for word, needed in note_count.items():
        # mag_count[word] returns 0 if word is missing (no KeyError)
        if mag_count[word] < needed:
            print("No")
            return
    print("Yes")
