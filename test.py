import re

my_re = re.compile(r"of (.*) experience")
text = 'How many years of Android development experience do you have?'

print(my_re.search(text).group(1))