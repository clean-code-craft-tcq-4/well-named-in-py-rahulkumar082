import conversions.number_to_pair_conversion as num_to_pair

class reference_manual:
    """
    Purpose: This class will print out the complete reference
            manual with color name and MAJOR and MINOR COLOR.
    """
    def __init__(self, MAJOR_COLORS, MINOR_COLORS):
        self.MAJOR_COLORS = MAJOR_COLORS
        self.MINOR_COLORS = MINOR_COLORS

    def print_manual(self):
        for pair_number in range(1, 26):
            ref_obj = num_to_pair.number_to_pair_conversion(self.MAJOR_COLORS, self.MINOR_COLORS)
            major_color, minor_color = ref_obj.get_color_from_pair_number(pair_number)
            print(color_pair_to_string(pair_number, major_color, minor_color))

def color_pair_to_string(pair_number, major_color, minor_color):
  return f'{pair_number} -> {major_color} + {minor_color}'