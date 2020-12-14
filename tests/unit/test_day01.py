from aoc.solution import day01


def test_part1_list_of_two_values():
    expenses = [1, 2019]

    answer = day01.part1(expenses)

    assert answer == 2019


def test_part1_list_of_many_values():
    expenses = [2, 1, 3, 2018]

    answer = day01.part1(expenses)

    assert answer == 4036


def test_part1_use_expense_list_from_problem_example():
    expenses = [1721, 979, 366, 299, 675, 1456]

    answer = day01.part1(expenses)

    assert answer == 514579
