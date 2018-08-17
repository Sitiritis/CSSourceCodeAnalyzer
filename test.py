import UtilFunctions as uf
'''import re
import UtilFunctions as uf

test_str = "fdsgdfsgds\n/*\nfdsgfdsg\n*/\nhjgkhjgk\n/*hdfsgfdsg*/\n"

print(test_str)

test_str = re.sub(r"/\*\s*.*\s*\*/", "", test_str)
test_str = uf.remove_empty_lines(test_str)

print(test_str)
'''

'''
import Lookups as l

print("|".join(l.cs_keyword_operators))
'''

'''
line_of_code = "int a[3] = fgld() + ++mvkm(fdsl, 4) * dfkgjkf[456, fkg] + \"fgfd\""
#line_of_code = "a ^= b + a - c * 2 ?? d != 3 * 2"

print(uf.__parse_simple_operators(line_of_code))
print(uf.__parse_operands(line_of_code))
'''

d1 = {'1': 10, '2': 15}
d2 = {'2': 15, '3': 20}

result = uf.__merge_dictionaries(d1, d2)

print(d1)
print(d2)
print(result)
