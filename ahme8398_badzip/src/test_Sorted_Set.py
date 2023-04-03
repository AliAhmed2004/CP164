"""
-------------------------------------------------------
Simple Sorted_Set testing
-------------------------------------------------------
Author: Ali Ahmed
ID:     169038398
Email:  ahme8398@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Sorted_Set_array import Sorted_Set

# Constants
SEP = "-" * 60
VALUES = [4, 3, 5, 1, 2, 0]


def print_set(name, source):
    """
    Prints Sorted_Set formatted as 'name: {set contents}'
    """
    print(f"{name}: {{", end='')
    for v in source:
        print(f"{v}, ", end="")
    print("}")
    return


def fill_set(values):
    """
    Returns a Sorted_Set with contents of values
    """
    source = Sorted_Set()
    for v in values:
        source.add(v)
    return source


def test_is_empty():
    print()
    print(SEP)
    print("Empty Sorted_Set:")
    print()
    source = Sorted_Set()
    print_set("source", source)
    print(f"source.is_empty(): {source.is_empty()}")


def test_add():
    print()
    print(SEP)
    print("Test add()")
    print()
    source = Sorted_Set()
    print(f"Attempt to add {VALUES} to source again:")
    for v in VALUES:
        added = source.add(v)
        print(f"added {v}: {added}")
    print_set("source", source)
    print()
    print(f"source.is_empty(): {source.is_empty()}")
    print()
    print("Test add() with repeated values")
    print(f"Attempt to add {VALUES} to source again:")
    for v in VALUES:
        added = source.add(v)
        print(f"added {v}: {added}")
    print_set("source", source)


def test_contains():
    print()
    print(SEP)
    print("Test in (__contains__())")
    print()
    source = fill_set(VALUES)
    print_set("source", source)
    v = VALUES[2]
    found = v in source
    print(f"{v} in source: {found}")
    v = 99
    found = v in source
    print(f"{v} in source: {found}")


def test_equ():
    print()
    print(SEP)
    print("Test == (__eq__())")
    print()
    source = fill_set(VALUES)
    target = fill_set(VALUES)
    print_set("source", source)
    print_set("target", target)
    equals = source == target
    print(f"source == target: {equals}")


def test_discard():
    print()
    print(SEP)
    print("Test discard()")
    print()
    source = fill_set(VALUES)
    v = 99
    discarded = source.discard(v)
    print(f"source.discard({v}): {discarded}")
    print_set("source", source)
    v = VALUES[3]
    discarded = source.discard(v)
    print(f"source.discard({v}): {discarded}")
    print_set("source", source)
    print()
    print("Test == (__eq__()) - after successful discard")
    target = fill_set(VALUES)
    print_set("target", target)
    equals = source == target
    print(f"source == target: {equals}")


def test_issubset():
    print()
    print(SEP)
    print("Test issubset()")
    print()
    source = fill_set(VALUES)
    print_set("source", source)
    target = fill_set(VALUES[1:])
    print_set("target", target)
    subset = source.issubset(target)
    print(f"source.issubset(target): {subset}")
    subset = target.issubset(source)
    print(f"target.issubset(source): {subset}")


def test_isdisjoint():
    print()
    print(SEP)
    print("Test isdisjoint()")
    print("source:")
    source = fill_set(VALUES)
    print_set("source", source)
    target = fill_set(VALUES[1:])
    print_set("target", target)
    disjoint = source.isdisjoint(target)
    print(f"source.isdisjoint(target): {disjoint}")

    print_set("source", source)
    target = fill_set(list(range(7, 10)))
    print_set("target", target)
    disjoint = source.isdisjoint(target)
    print(f"source.isdisjoint(target): {disjoint}")


def test_intersection():
    print()
    print(SEP)
    print("Test intersection()")
    source1 = fill_set(list(range(4)))
    print_set("source1", source1)
    source2 = fill_set(list(range(3, 6)))
    target = source1.intersection(source2)
    print_set("source1", source1)
    print_set("source2", source2)
    print("target = source1.intersection(source2)")
    print_set("target", target)


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test Sorted_Set()")
    test_is_empty()
    test_add()
    test_contains()
    test_equ()
    test_discard()
    test_issubset()
    test_isdisjoint()
    test_intersection()
