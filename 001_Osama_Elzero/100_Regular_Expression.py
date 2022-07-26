import re

# my_Search = re.search("[A-Z]", "OsamaElzero")
my_Search = re.search(r"[A-Z]{2}", "OOsamaElzero")
print(my_Search)
print(my_Search.span())
print(my_Search.string)
print(my_Search.group())
# print(dir(my_Search))
# print(dir(re))