# It's the academic year's end, fateful moment of your school report. The averages must be calculated.
# All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.

def get_average(marks):
    x = len(marks)
    y = sum(marks)
    average = y // x
    return average
    raise NotImplementedError("TODO: get_average")

print(get_average([2, 2, 2, 2]))
print(get_average([1, 5, 87, 45, 8, 8]))