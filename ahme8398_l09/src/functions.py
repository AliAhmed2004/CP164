"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-03-20"
-------------------------------------------------------
"""
# Imports

# Constants

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for value in values:
        hash_val = hash(value)
        slot = hash_val % slots
        print(f"{hash_val:>20d} {slot:>4d}    {value}")
    return