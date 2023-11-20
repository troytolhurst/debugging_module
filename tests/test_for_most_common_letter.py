from lib.get_most_common_letter import *

def tests_for_most_common_letter():
    result = get_most_common_letter("oneee two three four")
    assert result == "e"