# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

words = ['onset', 'lab', 'python', 'google', 'enlist', 'dusty', 'gogole', 'tinsel', 'notes', 'silent', 'dog', 'loop', 'stone', 'study', 'listen']
docs = {'D1': 'data science uses python and sets', 'D2': 'python is simple and fun', 'D3': 'a dictionary maps keys to values', 'D4': 'values may repeat but keys are unique', 'D5': 'simple data simple code', 'D6': 'python sets and dictionaries are fun'}

# Task 6: anagrams and a mini search engine
import re


def _word_key(word):
    """Normalize a word for anagram comparison."""
    return "".join(sorted(re.sub(r"[^a-z0-9]", "", str(word).lower())))


def anagram_groups(words):
    """Return groups of words sharing an anagram key; omit singleton groups."""
    groups = {}
    for word in words:
        key = _word_key(word)
        if key:
            groups.setdefault(key, []).append(word)
    return [group for group in groups.values() if len(group) > 1]


def inverted_index(docs):
    """Build {lowercase_word: set(document_ids)} from {document_id: text}."""
    index = {}
    for document_id, content in docs.items():
        for word in set(re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", str(content).lower())):
            index.setdefault(word, set()).add(document_id)
    return index


def search_and(index, w1, w2):
    """Return document IDs containing both terms."""
    return index.get(str(w1).lower(), set()) & index.get(str(w2).lower(), set())


def search_or(index, w1, w2):
    """Return document IDs containing either or both terms."""
    return index.get(str(w1).lower(), set()) | index.get(str(w2).lower(), set())


print("Anagram groups:", anagram_groups(words))
index = inverted_index(docs)
print("Indexed terms:", len(index))
print("Search AND ('python', 'sets'):", sorted(search_and(index, "python", "sets")))
print("Search OR ('python', 'sets'):", sorted(search_or(index, "python", "sets")))
assert all(len(group) >= 2 for group in anagram_groups(words))
assert search_and({"python": {"D1", "D2"}, "sets": {"D2", "D3"}}, "python", "sets") == {"D2"}
assert search_or({"python": {"D1", "D2"}, "sets": {"D2", "D3"}}, "python", "sets") == {"D1", "D2", "D3"}
assert inverted_index({"D1": "Python python sets!"}) == {"python": {"D1"}, "sets": {"D1"}}
print("Task 6 checks: PASS")
