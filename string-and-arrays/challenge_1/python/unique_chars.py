# Determine if a string contains only unique characters

class UniqueChars():
  # Implementação com set()
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def withSet(string):
    if string is None:
      return False
    return len(set(string)) == len(string)
