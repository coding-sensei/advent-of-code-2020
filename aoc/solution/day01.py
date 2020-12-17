def part1(expenses):
    """
    Function to solve Day 01 Part 1.

    O(n^2) Time complexity: I think this could be reduced to O(n) with a dictionary
    O(n) Space complexity

    Args:
        expenses (list): The list of expenses in Integers.

    Returns:
        int: The multiplication of the two expenses that add up to 2020.

    """
    for expense in expenses:
        remainder = 2020 - expense
        if remainder in expenses:
            return remainder * expense
