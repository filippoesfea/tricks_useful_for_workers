# GET FROM ANY FILE MOST COMMON WORD/NUMBER USED

import collections
# import json (optional)
# import re (optional)

# open file (if directory is not specified in path file, insert complete path in directory)
# es. example_mongo --> AAA --> 'Desktop\.....
file = open('yourfilename.json', 'rt')
data = file.read()
# splitting each content in file
words = data.split()
# collections
# most common --> select how much words get
most_common = collections.Counter(words).most_common(3)
print(most_common)
