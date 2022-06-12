class number_to_pair_conversion:
    """
    Purpose: This class contains the method to convert pair
            number to the color for a 25-pair color code.
            Example: PAIR NUMBER = 4
            MAJOR_COLOR = WHITE & MINOR_COLOR = BROWN
    """
    def __init__(self, MAJOR_COLORS, MINOR_COLORS) -> None:
        self.MAJOR_COLORS = MAJOR_COLORS
        self.MINOR_COLORS = MINOR_COLORS

    def get_color_from_pair_number(self, pair_number):
        zero_based_pair_number = pair_number - 1
        major_index = zero_based_pair_number // len(self.MINOR_COLORS)
        if major_index >= len(self.MAJOR_COLORS):
            raise Exception('Major index out of range')
        minor_index = zero_based_pair_number % len(self.MINOR_COLORS)
        if minor_index >= len(self.MINOR_COLORS):
            raise Exception('Minor index out of range')
        return (self.MAJOR_COLORS[major_index], self.MINOR_COLORS[minor_index])

    def test_number_to_pair(self, pair_number, expected_major_color, expected_minor_color):
        [major_color, minor_color] = self.get_color_from_pair_number(pair_number)
        assert(major_color == expected_major_color)
        assert(minor_color == expected_minor_color)
