from aoc.utilities import *
from mock import patch, mock_open


@patch("builtins.open", new_callable=mock_open, read_data="1\n2\n3")
def test_convert_file_to_integar_list(mock_open):
    assert  read_numbers("foo.txt") == [1,2,3]
