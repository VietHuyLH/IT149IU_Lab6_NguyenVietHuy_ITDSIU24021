# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

text = 'Unique keys, simple values: that is the dictionary idea. A dictionary maps keys to values; a set stores unique items! The fox and the dog became friends in the end. Data science starts with clean data and clear questions.'

# Task 3: word frequency
import re


def word_freq(text):
    """Return a dictionary of lowercase word frequencies; punctuation is ignored."""
    words_found = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", str(text).lower())
    frequencies = {}
    for word in words_found:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def top_n(freq, n):
    """Return up to n (word, count) pairs, count descending and word ascending."""
    if n <= 0:
        return []
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


def longest_word(freq):
    """Return the longest word key; alphabetical order breaks length ties."""
    if not freq:
        return None
    return min(freq, key=lambda word: (-len(word), word))


freq = word_freq(text)
total_words = sum(freq.values())
print("Total words:", total_words)
print("Distinct words:", len(freq))
print("Top 10:", top_n(freq, 10))
print("Longest word:", longest_word(freq))
assert sum(freq.values()) == len(re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text.lower()))
assert top_n({"pear": 2, "apple": 2, "plum": 1}, 2) == [("apple", 2), ("pear", 2)]
assert longest_word({"cat": 3, "zebra": 1, "apple": 2}) == "apple"
assert longest_word({}) is None
print("Task 3 checks: PASS")


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    items = top_n(freq, 5)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar([x[0] for x in items], [x[1] for x in items])
    ax.set_title(f"Top 5 words (total words: {total_words})")
    ax.set_xlabel("Word")
    ax.set_ylabel("Frequency")
    fig.tight_layout()
    fig.savefig("task3_top5_words.png", dpi=160)
    plt.show()
