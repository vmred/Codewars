# You might know some pretty large perfect squares.
# But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

# Examples:

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect
from asserts.Asserts import assert_true


def find_next_square(sq):
    s = sq ** 0.5

    if s.__divmod__(1.)[1] != 0.0:
        return -1

    return (int(s) + 1) ** 2


assert_true(find_next_square(114), -1)
assert_true(find_next_square(121), 144)
