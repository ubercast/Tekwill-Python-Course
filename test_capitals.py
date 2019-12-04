from capitals import count_letters

assert count_letters('nfWEHI') == (4, 2), 'should be 4 uppercase letter and 2 lower case'
assert count_letters('WOIJgeiegrh') == (4, 7), 'should be 4 uppercase letter and 7 lower case'
assert count_letters('gh89FJKB') != (0, 0), 'should be wrong'