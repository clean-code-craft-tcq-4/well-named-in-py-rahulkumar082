from conversions import number_to_pair_conversion as num_to_pair
from conversions import pair_to_number_conversion as pair_to_num
from new_feature import reference_manual as ref_manual

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

if __name__ == '__main__':
  num_to_pair = num_to_pair.number_to_pair_conversion(MAJOR_COLORS, MINOR_COLORS)
  pair_to_num = pair_to_num.pair_to_number_conversion(MAJOR_COLORS, MINOR_COLORS)
  ref_man = ref_manual.reference_manual(MAJOR_COLORS, MINOR_COLORS)
  num_to_pair.test_number_to_pair(4, 'White', 'Brown')
  num_to_pair.test_number_to_pair(5, 'White', 'Slate')
  pair_to_num.test_pair_to_number('Black', 'Orange', 12)
  pair_to_num.test_pair_to_number('Violet', 'Slate', 25)
  pair_to_num.test_pair_to_number('Red', 'Orange', 7)
  ref_man.print_manual()
  print('Done :)')
