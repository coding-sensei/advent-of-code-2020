from aoc.utilities import *
import mock


def test_convert_file_to_integar_list():
    mock_open = mock.mock_open(read_data="1\n2\n3")

    with mock.patch('builtins.open', mock_open):
        assert convert_file("foo.txt", int) == [1,2,3]

def test_convert_file_to_string_list():
    mock_open = mock.mock_open(read_data="foo\nbar")

    with mock.patch('builtins.open', mock_open):
        assert convert_file("foo.txt", str) == ["foo","bar"]

def test_read_numbers_returns_list_of_integars():
    mock_open = mock.mock_open(read_data="1\n2")

    with mock.patch('builtins.open', mock_open):
        assert read_numbers("foo.txt") == [1,2]
