class pair_to_number_conversion():
    """
    Purpose: This class contains the method to convert pair
            number to the color for a 25-pair color code.
            Example: MAJOR_COLOR = WHITE & MINOR_COLOR = BROWN
            PAIR NUMBER = 4
    """
    def __init__(self, MAJOR_COLORS, MINOR_COLORS) -> None:
        self.MAJOR_COLORS = MAJOR_COLORS
        self.MINOR_COLORS = MINOR_COLORS

    def test_pair_to_number(self, major_color, minor_color, expected_pair_number):
        pair_number = self.get_pair_number_from_color(major_color, minor_color)
        assert(pair_number == expected_pair_number)

    def get_pair_number_from_color(self, major_color, minor_color):
        try:
            major_index = self.MAJOR_COLORS.index(major_color)
        except ValueError:
            raise Exception('Major index out of range')
        try:
            minor_index = self.MINOR_COLORS.index(minor_color)
        except ValueError:
            raise Exception('Minor index out of range')
        return major_index * len(self.MINOR_COLORS) + minor_index + 1
