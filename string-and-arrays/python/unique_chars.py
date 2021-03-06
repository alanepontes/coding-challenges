from util import Util
# if a string contains only unique characters

class UniqueChars():
  # Implementacao com set()
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def withSet(self, string):
    return not (string is None) and len(set(string)) == len(string)

  def _createHashMap(self, string):
    setChars = set()
    for char in string:
      if char not in setChars:
        setChars.add(char)
    return setChars
    
  # Implementacao com hashMap lookup
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def withHashMapLookup(self, string):
    return not Util.has_none(string) and len(self._createHashMap(string)) == len(string) 

  # Implementacao com bitwise operator AND
  # Complexidade temporal O(n)
  # Complexidade espacial O(1)
  def withBitAnd(self, string):
    if Util.has_none(string):
      return False
    
    accumulator = int(0)
    for char in string:
      val = int(2**(ord(char) - ord('A'))) 
      if accumulator & val == 0:
        accumulator += val
      else:
        return False
    return True 

  # Implementacao com aux array
  # Complexidade temporal O(n²)
  # Complexidade espacial O(1)
  def withAuxArr(self, string):
    if Util.has_none(string):
      return False
    
    for i in range(len(string)):
      for j in range(len(string) - 1 - i):
        if (string[i] == string[j + 1 + i]):
          return False;
    return True
    
    