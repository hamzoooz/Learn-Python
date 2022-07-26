# ---------------------------
# String
# يمكن كتابة السلسلة في علامة تنصيص منفرده أو مزدوجة
# ويمكن كتابة جعلها على أكثر من سطر عن طريق الأقتباس المثلث مفرد أو مزدوج
#  يمكن إدخال علامات التنصيص في بعضها بدون إستخدام أدوت التخطي عت طريق عكسهن
# ---------------------------

# separate || separator
print("="*20) # ====================

singleString = 'This Is String'
doubleString = "This IS String"
print(singleString)
print(doubleString)

# We Can Use This Method Without Scape Sequences
stringinstring = ' "This Double Quotes" inside Single Quotes'
print(stringinstring)
print("="*35)

# When We need to print the string in more than one line we use treble 'single' || "duoble" Quotes
# we Can Use duoble or single inside each any one 
# like This 
mult_line_duoble = """First Line
Second Line & "Test duoble insid trible double quote" & 'Test Single insid trible double quote'
Third Line
"""
print(mult_line_duoble)

mult_line_single = '''First Line 
Second Line 'Test Single insid trible single quote'
Third Line & "Test Single insid trible double quote"
'''
print(mult_line_single)
