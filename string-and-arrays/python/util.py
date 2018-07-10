class Util:
  
  @staticmethod
  def is_invalid_input(*args):
    for element in args:
      if (element is None) or not element:
        return True
    return False

  @staticmethod
  def has_lenght_notequal(base, target):
    return len(base) != len(target)