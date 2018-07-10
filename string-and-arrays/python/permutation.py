from collections import Counter, defaultdict
from util import Util

class Permutation():
  
  # Implementacao com sorted 
  # Complexidade temporal O(n logn) por conta do sorte, em geral
  # Complexidade espacial O(n)
  def is_permutation_sorted(self, base_string, permutated):
    not_permutation = Util.has_none(base_string, permutated) or Util.has_empty_string(base_string, permutated) or Util.has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False
    return sorted(base_string) == sorted(permutated)

  # Implementacao com Counter
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def is_permutation_counter(self, base_string, permutated):
    not_permutation = Util.has_none(base_string, permutated) or Util.has_empty_string(base_string, permutated) or Util.has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False
    return Counter(base_string) == Counter(permutated)

  # Implementacao com defaultdict
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def is_permutation_dict(self, base_string, permutated):
    not_permutation = Util.has_none(base_string, permutated) or Util.has_empty_string(base_string, permutated) or Util.has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False

    dict_base_string = defaultdict(int)
    dict_permutated = defaultdict(int)
    for char in base_string:
      dict_base_string[char] += 1
    for char in permutated:
      dict_permutated[char] += 1
    return dict_base_string == dict_permutated