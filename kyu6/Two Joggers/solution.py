# Bob and Charles are meeting for their weekly jogging tour.
# They both start at the same spot called "Start"
# and they each run a different lap, which may (or may not) vary in length.
# Since they know each other for a long time already, they both run at the exact same speed.


# Task
# Your job is to complete the function nbrOfLaps(x, y) that, given the length of the laps for Bob and Charles,
# finds the number of laps that each jogger has to complete before they meet each other again,
# at the same time, at the start.

# The function takes two arguments:
# The length of Bob's lap (larger than 0)
# The length of Charles' lap (larger than 0)

# The function should return an array (Tuple<int, int> in C#) containing exactly two numbers:

# The first number is the number of laps that Bob has to run
# The second number is the number of laps that Charles has to run

# Examples:
# nbr_of_laps(5, 3) # returns (3, 5)
# nbr_of_laps(4, 6); # returns (3, 2)


def nbr_of_laps(x, y):
    x_laps, y_laps = 1, 1
    x_lap = x
    y_lap = y
    while x != y:
        if x < y:
            x += x_lap
            x_laps += 1
        else:
            y += y_lap
            y_laps += 1

    return x_laps, y_laps
    # from math import gcd
    # return y / gcd(x, y), x / gcd(x, y)