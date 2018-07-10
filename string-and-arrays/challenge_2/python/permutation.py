from collections import Counter, defaultdict

class Permutation():
  
  def _is_invalid_input(self, base_string, permutated):
    has_none = base_string is None or permutated is None
    has_empty = not base_string or not permutated
    if has_none or has_empty:
      return True
    return False

  def _has_lenght_notequal(self, base_string, permutated):
    return len(base_string) != len(permutated)
  # Implementacao com sorted 
  # Complexidade temporal O(n logn) por conta do sorte, em geral
  # Complexidade espacial O(n)
  def is_permutation_sorted(self, base_string, permutated):
    not_permutation = self._is_invalid_input(base_string, permutated) or self._has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False
    return sorted(base_string) == sorted(permutated)

  # Implementacao com Counter
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def is_permutation_counter(self, base_string, permutated):
    not_permutation = self._is_invalid_input(base_string, permutated) or self._has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False
    return Counter(base_string) == Counter(permutated)

  # Implementacao com defaultdict
  # Complexidade temporal O(n)
  # Complexidade espacial O(n)
  def is_permutation_dict(self, base_string, permutated):
    not_permutation = self._is_invalid_input(base_string, permutated) or self._has_lenght_notequal(base_string, permutated)
    if not_permutation:
      return False

    dict_base_string = defaultdict(int)
    dict_permutated = defaultdict(int)
    for char in base_string:
      dict_base_string[char] += 1
    for char in permutated:
      dict_permutated[char] += 1
    return dict_base_string == dict_permutated