import re

try1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
str = try1.search('my number is 667-212-6903')
print str.group()

try2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
str2 = try2.search('my number is 667-212-6903')
print str2.group(1)
