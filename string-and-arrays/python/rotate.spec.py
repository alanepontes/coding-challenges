import unittest
from rotate import Rotate

class TestRotate(unittest.TestCase):
  def setUp(self):
    self.rotate = Rotate()

  def test_all_unique_chars(self): 
    self.assertEqual(self.rotate.is_rotate(None, None), False) # any input none
    self.assertEqual(self.rotate.is_rotate(None, ''), False) # any input none
    self.assertEqual(self.rotate.is_rotate('', ''), True)
    self.assertEqual(self.rotate.is_rotate('', 'alane'), False) # any string that differ in size
    self.assertEqual(self.rotate.is_rotate('alane', 'neaa'), False) # any string that differ in size
    self.assertEqual(self.rotate.is_rotate('alane', 'neala'), True) 

if __name__ == '__main__':
  unittest.main()
