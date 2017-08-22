import re
try = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
str = try.search('my number is 667-212-6903')
