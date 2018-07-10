const UniqueChars = require('./uniqueChars.js');
describe('Test unique chars', () => {
  
  it('withSet()', () => {
    expect(UniqueChars.withSet('')).toEqual(false);
    expect(UniqueChars.withSet(null)).toEqual(false);
    expect(UniqueChars.withSet(undefined)).toEqual(false);
    expect(UniqueChars.withSet('alane')).toEqual(false);
    expect(UniqueChars.withSet('alne')).toEqual(true);
  })
});