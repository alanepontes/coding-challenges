class UniqueChars {
  static withSet(string) {
    return Boolean(string) && ((new Set(string)).size === (String(string).length));
  } 
}

module.exports = UniqueChars;