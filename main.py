from new_feature import reference_manual as ref_manual
from test_conversion.test_features import test_features

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

if __name__ == '__main__':
  ref_man = ref_manual.reference_manual(MAJOR_COLORS, MINOR_COLORS)
  test_object = test_features(MAJOR_COLORS, MINOR_COLORS)
  test_object.test_number_to_pair(4, 'White', 'Brown')
  test_object.test_number_to_pair(5, 'White', 'Slate')
  test_object.test_pair_to_number('Black', 'Orange', 12)
  test_object.test_pair_to_number('Violet', 'Slate', 25)
  test_object.test_pair_to_number('Red', 'Orange', 7)
  ref_man.print_manual()
  print('Done :)')
