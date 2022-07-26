# =================================
#    Escape Sequences Characters     
# =================================
# 
# [01] \b   => Back Space [بتمسح العنصر القبلها]
# [02] \    => Escape New Line + Back Slash[\] + after .
# [03] \\   => Escape Back Slash
# [04] \'   => Escape Single Quotes
# [04] \"   => Escape Double Quotes
# [05] \n   => Make New Line
# [06] \r   => Carriage Return replace Before it By After it
# [07] \t   => Horizotal Tap. 
# [08] \xhh => Character Hex Value .

# For More Escape Sequences Characters Search in Google 
# ======================================================

# Back Space 
print("hamzooozz\bbanga") #Will Remve z print hamzooozbanga

# Escape New Line + \
print("Hello\
    Python\
") # Escape New Line & \ Print Hello Python Ijn One Line  print ->Hello    Python

# Escape Back Slash
print("I Like Back Slash'\\'") #Escape Back Slash print -> hamzoooz\banga

# Escape Single Quotes
print('hamzoooz\'banga\'') #Escape Single Quotes print -> hamzoooz'banga'

# Escape Double Quotes
print("hamzoooz\"banga\"") #Escape Double Quotes print -> hamzoooz"banga"

# Make New Line
print("hamzoooz\nbanga") #Make New Line 

# Carriage Return replace Before it By After it
print("123456\rABCD") #Carriage Return replace Before it By After it print ABCD56 

# Horizotal Tap. 
print("Hello\tPython") #Horizotal Tap print -> Hello    Python 

# Character Hex Value .
print("\x4F\x73") # print -> Os