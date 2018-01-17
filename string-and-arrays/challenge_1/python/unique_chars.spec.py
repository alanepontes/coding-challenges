import unittest
from unique_chars import UniqueChars

class TestUniqueChars(unittest.TestCase):
  def setUp(self):
    self.func = UniqueChars.withSet

  def test_all_unique_chars(self):
    self.assertEqual(self.func(None), False)
    self.assertEqual(self.func(''), True)
    self.assertEqual(self.func('alane'), False)
    self.assertEqual(self.func('alne'), True)
       

if __name__ == '__main__':
  unittest.main()