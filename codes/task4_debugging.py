# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

import copy

# Task 4: corrected functions for the four identified bugs

def merge_inventories(a, b):
    """Merge two {item: qty} dictionaries, return a new dict, and do not mutate inputs."""
    result = a.copy()
    for item, quantity in b.items():
        result[item] = result.get(item, 0) + quantity
    return result


def unique_tags(records):
    """Return the set of all distinct tags in records."""
    tags = set()
    for record in records:
        for tag in record.get("tags", []):
            tags.add(tag)
    return tags


def remove_empty(d):
    """Remove in place every key whose value equals zero, then return d."""
    for key in list(d):
        if d[key] == 0:
            del d[key]
    return d


_inventory_a = {"pen": 10, "book": 4}
_inventory_b = {"pen": 3, "pencil": 8}
_merged = merge_inventories(_inventory_a, _inventory_b)
_records = [{"tags": ["python", "beginner"]}, {"tags": ["python", "data"]}]
_tag_set = unique_tags(_records)
_stock = {"pen": 10, "book": 0, "eraser": 0, "pencil": 5}
_removed = remove_empty(_stock)
print("Merged inventory:", _merged)
print("Input A unchanged:", _inventory_a)
print("Input B unchanged:", _inventory_b)
print("Unique tags:", sorted(_tag_set))
print("After removing zero quantities:", _removed)
assert _merged == {"pen": 13, "book": 4, "pencil": 8}
assert _inventory_a == {"pen": 10, "book": 4}
assert _inventory_b == {"pen": 3, "pencil": 8}
assert _tag_set == {"python", "beginner", "data"}
assert _removed == {"pen": 10, "pencil": 5}
print("Task 4 checks: PASS")
