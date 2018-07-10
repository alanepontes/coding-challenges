from util import Util
# Determine if a string s1 is a rotation of another string s2, 
# by calling (only once) a function is_substring

class Rotate():

  def is_substring(self, string, stringconcat):
    return string in stringconcat

  # Implementacao com in operator 
  # https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def is_rotate(self, s1, s2):
    if Util.has_none(s1, s2) or Util.has_lenght_notequal(s1, s2):
      return False
    return self.is_substring(s1, s2 + s2)