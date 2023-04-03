"""
-------------------------------------------------------
Simple midterm function testing
-------------------------------------------------------
Author: Ali Ahmed
ID:     169038398
Email:  ahme8398@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_array import List
from Queue_array import Queue
from queue_functions import queue_rotate


# Constants
SEP = "-" * 60
SIZE = 6


def test_queue_rotate():
    print(SEP)
    print("Testing 'queue_rotate'")
    print()
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    values = list(range(SIZE))

    for case in CASES:
        source = Queue()

        for v in values:
            source.insert(v)
        queue_rotate(source, case)
        print(f"queue_rotate({values}, {case}): {source._values}")
    print()
    return


def test_rotate():
    print(SEP)
    print("Testing 'rotate'")
    print()
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    values = list(range(SIZE))

    for case in CASES:
        source = Queue()

        for v in values:
            source.insert(v)
        source.rotate(case)
        print(f"{values}: source.rotate({case}): {source._values}")
    print()
    return


def test_count_pairs():
    print(SEP)
    print("Testing 'count_pairs'")
    print()
    CASES = (
        [],
        [0, 1, 2, 3],
        [0, 0, 1, 1, 2, 2, 3, 3],
        [0, 0, 0, 1, 2, 3, 3, 3],
    )

    for values in CASES:
        source = List()

        for v in values:
            source.append(v)
        pairs = source.count_pairs()
        print(f"{values}: source.count_pairs(): {pairs}")
    print()
    return


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Midterm Testing")
    test_queue_rotate()
    test_rotate()
    test_count_pairs()
