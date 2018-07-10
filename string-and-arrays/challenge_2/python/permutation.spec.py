import unittest
from permutation import Permutation

# Questions
# Can we assume the string is ASCII?
# - Yes
# Is whitespace important?
# - Yes
# Is this case sensitive? 'Cat', 'cat' is not a match?
# - Yes
# Can we use additional data structures?
# - Yes
# Can we assume this fits in memory?
# - Yes


# Test case
# 
class TestPermutation(unittest.TestCase):

  def setUp(self):
    self.permutation = Permutation()

  def test_permitation(self):
    self.assertEqual(self.permutation.is_permutation_sorted("", ""), False)
    self.assertEqual(self.permutation.is_permutation_sorted("", "alane"), False)
    self.assertEqual(self.permutation.is_permutation_sorted("alane", ""), False)
    self.assertEqual(self.permutation.is_permutation_sorted(None, None), False)
    self.assertEqual(self.permutation.is_permutation_sorted(None, "alane"), False)
    self.assertEqual(self.permutation.is_permutation_sorted("alane", None), False)
    self.assertEqual(self.permutation.is_permutation_sorted("Cat", "cta"), False)
    self.assertEqual(self.permutation.is_permutation_sorted("enala", "alane"), True)
    self.assertEqual(self.permutation.is_permutation_sorted("C at", "a Ct"), True)
    self.assertEqual(self.permutation.is_permutation_sorted("cat", "tac"), True)

    self.assertEqual(self.permutation.is_permutation_counter("", ""), False)
    self.assertEqual(self.permutation.is_permutation_counter("", "alane"), False)
    self.assertEqual(self.permutation.is_permutation_counter("alane", ""), False)
    self.assertEqual(self.permutation.is_permutation_counter(None, None), False)
    self.assertEqual(self.permutation.is_permutation_counter(None, "alane"), False)
    self.assertEqual(self.permutation.is_permutation_counter("alane", None), False)
    self.assertEqual(self.permutation.is_permutation_counter("Cat", "cta"), False)
    self.assertEqual(self.permutation.is_permutation_counter("enala", "alane"), True)
    self.assertEqual(self.permutation.is_permutation_counter("C at", "a Ct"), True)
    self.assertEqual(self.permutation.is_permutation_counter("cat", "tac"), True)


    self.assertEqual(self.permutation.is_permutation_dict("", ""), False)
    self.assertEqual(self.permutation.is_permutation_dict("", "alane"), False)
    self.assertEqual(self.permutation.is_permutation_dict("alane", ""), False)
    self.assertEqual(self.permutation.is_permutation_dict(None, None), False)
    self.assertEqual(self.permutation.is_permutation_dict(None, "alane"), False)
    self.assertEqual(self.permutation.is_permutation_dict("alane", None), False)
    self.assertEqual(self.permutation.is_permutation_dict("Cat", "cta"), False)
    self.assertEqual(self.permutation.is_permutation_dict("enala", "alane"), True)
    self.assertEqual(self.permutation.is_permutation_dict("C at", "a Ct"), True)
    self.assertEqual(self.permutation.is_permutation_dict("cat", "tac"), True)

if __name__ == '__main__':
  unittest.main()
