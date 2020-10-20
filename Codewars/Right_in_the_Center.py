# Given a sequence of characters, does "abc" appear in the CENTER of the sequence?
# The sequence of characters could contain more than one "abc".
# To define CENTER, the number of characters in the sequence to the
# left and right of the "abc" (which is in the middle) must differ by at most one.
# If it is in the CENTER, return True. Otherwise, return False.
# Write a function as the solution for this problem. This kata looks simple,
# but it might not be easy.

# is_in_middle("AAabcBB")  ->  True
# is_in_middle("AabcBB")   ->  True
# is_in_middle("AabcBBB")  ->  False



# def is_in_middle(sequence):
#     n = len(sequence)
#     i = (n - 3) // 2
#     return sequence[i:i+3] == 'abc' or (n % 2 == 0 and sequence[i+1:i+4] == 'abc')

# def is_in_middle(sequence):
#     while len(sequence) >= 3:
#         if sequence == 'abc' or sequence[1:] == 'abc' or sequence[:-1] == 'abc':
#             return True
#         sequence = sequence[1:-1]
#     return False

def is_in_middle(s):
    while len(s) > 4:
        s = s[1:-1]

    if 'abc' in s:
        return True
    return False

print(is_in_middle("AAabcBB"))
print(is_in_middle("AabcBB"))
print(is_in_middle("AabcBBB"))