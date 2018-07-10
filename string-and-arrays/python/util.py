class Util:
  
  @staticmethod
  def has_none(*args):
    for element in args:
      if (element is None):
        return True
    return False

  def has_empty_string(*args):
    for element in args:
      if not element:
        return True
    return False

  @staticmethod
  def has_lenght_notequal(base, target):
    return len(base) != len(target)