from conversions.number_to_pair_conversion import number_to_pair_conversion
from conversions.pair_to_number_conversion import pair_to_number_conversion


class test_features():
    """
    Purpose: This is a test class, which enables us to call functions to
    test number to pair and vice-versa functionality.
    """
    def __init__(self, MAJOR_COLORS, MINOR_COLORS) -> None:
        self.MAJOR_COLORS = MAJOR_COLORS
        self.MINOR_COLORS = MINOR_COLORS
        
    def test_pair_to_number(self, major_color, minor_color, expected_pair_number):
        pair_to_num_object = pair_to_number_conversion(self.MAJOR_COLORS, self.MINOR_COLORS)
        pair_number = pair_to_num_object.get_pair_number_from_color(major_color, minor_color)
        assert(pair_number == expected_pair_number)
    
    def test_number_to_pair(self, pair_number, expected_major_color, expected_minor_color):
        
        num_to_pair_object = number_to_pair_conversion(self.MAJOR_COLORS, self.MINOR_COLORS)
        [major_color, minor_color] = num_to_pair_object.get_color_from_pair_number(pair_number)
        assert(major_color == expected_major_color)
        assert(minor_color == expected_minor_color)
