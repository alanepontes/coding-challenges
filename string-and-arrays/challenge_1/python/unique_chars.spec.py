import unittest
from unique_chars import UniqueChars

class TestUniqueChars(unittest.TestCase):
  def setUp(self):
    self.uniqueChars = UniqueChars()

  def test_all_unique_chars(self):
    self.assertEqual(self.uniqueChars.withSet(None), False)
    self.assertEqual(self.uniqueChars.withSet(''), True)
    self.assertEqual(self.uniqueChars.withSet('alane'), False)
    self.assertEqual(self.uniqueChars.withSet('alne'), True)
    self.assertEqual(self.uniqueChars.withSet('alneCC'), False)

    self.assertEqual(self.uniqueChars.withHashMapLookup(None), False)
    self.assertEqual(self.uniqueChars.withHashMapLookup(''), True)
    self.assertEqual(self.uniqueChars.withHashMapLookup('alane'), False)
    self.assertEqual(self.uniqueChars.withHashMapLookup('alne'), True)
    self.assertEqual(self.uniqueChars.withHashMapLookup('alneCC'), False)

    self.assertEqual(self.uniqueChars.withBitAnd(None), False)
    self.assertEqual(self.uniqueChars.withBitAnd(''), True)
    self.assertEqual(self.uniqueChars.withBitAnd('alane'), False)
    self.assertEqual(self.uniqueChars.withBitAnd('alne'), True)
    self.assertEqual(self.uniqueChars.withBitAnd('alneçç'), False)
    self.assertEqual(self.uniqueChars.withBitAnd('ààlne'), False)
       

if __name__ == '__main__':
  unittest.main()