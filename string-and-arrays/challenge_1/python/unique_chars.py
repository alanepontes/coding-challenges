# Determine if a string contains only unique characters

class UniqueChars():
  # Implementacao com set()
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def withSet(self, string):
    if string is None:
      return False
    return len(set(string)) == len(string)

  def _createHashMap(self, string):
    setChars = set()
    for char in string:
      if char not in setChars:
        setChars.add(char)
    return setChars
    
  # Implementacao com hashMap()
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def withHashMapLookup(self, string):
    if string is None:
      return False
    return len(self._createHashMap(string)) == len(string) 
    
    