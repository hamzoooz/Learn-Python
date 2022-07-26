# # ===========================
# #       String Methods
# # ===========================
# #  Strip(char) => Defualt Char it space 
# # [01:1] strip(char)  => Return a copy of the string with leading and trailing whitespace removed.If chars is given and not None, remove characters in chars instead.
# # [01:2] rstrip(char) => Return a copy of the string with leading and trailing whitespace removed.If chars is given and not None, remove characters in chars instead.
# # [01:3] lstrip(char) => Return a copy of the string with leading and trailing whitespace removed.If chars is given and not None, remove characters in chars instead.
# # [02] Title() => Make All start character Capital untel After Number
# # [03] capitalize() => make All Char Start Capital except After Number
# # [04] zfill(int:width) => make all number has same width vai width you needed
# # [05] upper() => make All String Appuer Case
# # [06] lower() => make All String lower Case
# # [07:1] split(char , int:maxsplit) => return String list and asplited by parting char defualt char space
# # [07:2] rsplit(char , int:maxsplit) => return String list and asplited by parting char defualt char space but it Strat Form End String
# # [08] center(int:number , str:char) return String as list and asplited by parting char defualt char space
# #       => int:number => number of character we needed to return
# #       => str:char   => Charcter we needed to added To Strint
# # [09] count: Returns the number of times a specified value occurs in a tuple 
# #      count(x: str, __start, __end ) -> int

# a = "I love Python" 
# b = "  I love   Python  " # String With alought Spaces

# print(len(a)) # len() Function print length  Of String with Spacing
# # (function) len: (__obj: Sized) -> int
# # Return the number of items in a container.

# # Methods One srtip() => take charter  Form Both Side String
# # Methods One rsrtip() => take charter  Form Right String
# # Methods One lsrtip() => take charter  Form Left String
# #Syntax => function(name.strip(char==="space"))
# print(b)
# print(b.strip())  #take charter Form Both Side String
# print(b.rstrip())  #take charter  Form Right String
# print(b.lstrip())  #take charter  Form Left String
# print("="*20) 
# ============================================================
# a = "####I love Python####" 
# print(a)
# print(a.strip("#"))  #take charter Form Both Side String
# print(a.rstrip("#"))  #take charter  Form Right String
# print(a.lstrip("#"))  #take charter  Form Left String
# print("="*20) 
# ============================================================
# a = "#@#@#@#I love Python#@#@#@#@#@" 
# print(a)
# print(a.strip("#@"))  #take charter Form Both Side String
# print(a.rstrip("#@"))  #take charter  Form Right String
# print(a.lstrip("#@"))  #take charter  Form Left String
# print("="*20) 


# # ==============================================================
# # Method N.o Tow title()
# # make All Char Start Capital letter Untel After Number
# # Return a version of the string where each word is titlecased.
# # More specifically, words start with uppercased characters and all remaining cased characters have lower case.
# a = "i love 2d graphics and 4g Technolgy and pyhton"
# print(a.title())
# print("="*20) 

# # ==============================================================
# # Method N.o Tow capitalize()
# # make All Char Start Capital except After Number.
# # Return a capitalized version of the string.
# # More specifically, make the first character have upper case and the rest lower case.
# a = "i love 2d graphics and 4g Technolgy and pyhton"
# print(a.capitalize())
# print("="*20) 

# # ==============================================================
# # Method N.o Three zfill()
# #make all number has same width vai width you needed.
# # (method) zfill: (__width: SupportsIndex) -> str
# # Pad a numeric string with zeros on the left, to fill a field of the given width.
# # The string is never truncated.
# a ,b,c,d,f = "1", "10" , "111","1111","33333"
# print(a.zfill(5))
# print(b.zfill(5))
# print(c.zfill(5))
# print(f.zfill(5))
# print("="*20) 

# # ==============================================================
# # Method N.o Foure Upper()
# # make All String Appuer Case.
# # (method) upper: () -> str
# # Return a copy of the string converted to uppercase.
# g = "Hamza Banga Hamza Ahmed"
# print(g.upper())
# print("="*20) 

# # ==============================================================
# # Method N.o Five Lower()
# # make All String Lower Case.
# # (method) lower: () -> str
# # Return a copy of the string converted to lowercase.
# h = "HMAZA Banga Hamza AHMED"
# print(h.lower()) # -> hamza banga hamza Ahmed
# print("="*20)  

# # ==============================================================
# # Method N.o Six split(str:char , int:maxwidth)
# # return String list and asplited by parting char defualt char space
# # its splite by Defualt Space & We Can pase other character
# # (method) split: (sep: str | None = ..., maxsplit: SupportsIndex = ...) -> list[str]
# # Return a list of the words in the string, using sep as the delimiter string.
# #   =>  sep
# #   The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result.
# #   => maxsplit
# #   Maximum number of splits to do. -1 (the default value) means no limit.
# h = "hamza banga hamza Ahmed"
# print(h.split())
# print("="*20) 

# h = "hamza-banga-hamza-Ahmed"
# print(h.split("-")) 
# print("="*20) 

# k = "hamza-banga-hamza-Ahmed-hamza-banga-hamza-Ahmed"
# print(k.split("-", 1)) 
# print("="*20) 
# # ==============================================================
# # Method N.o Six rsplit(str:char , int:maxwidth)
# # return String list and asplited by parting char defualt char space
# # its splite by Defualt Space & We Can pase other character
# # str:char      => character we needed to split from it 
# # int:maxwidth => length of item insid list we needed to return
# l = "hamza-banga-hamza-Ahmed-hamza-banga-hamza-Ahmed"
# print(l.rsplit("-", 2)) 
# print("="*20) 


# # ==============================================================
# # Method N.o seven center(int:number , str:char)
# # return String list and asplited by parting char defualt char space
# # its splite by Defualt Space & We Can pase other character
# # int:number => number of character we needed to return
# # str:char   => Charcter we needed to added To Strint
# m = "hamza"
# print(m.center(10)) # Add Spaces 
# print(m.center(10,"#")) # Add # => ##hamza## 
# print("="*20) 
# # ==============================================================

# # count: (x: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int
# # Returns the number of times a specified value occurs in a tuple
# # The letter of Word Case sensitive  
# #   => (x: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int
# # string S[start:end]. Optional arguments start and end are interpreted as in slice notation

# n = "I Love Pyhon And PHP But I love Pyhon More Than PHP Becouce The Pyhon it Better and Do Any Thing PYHON"
# print(n.count("Pyhon" , ))           # -> 3
# print(n.count("Pyhon" ,0 , 20 ))     # -> 1
# print("="*20) 
# # ==============================================================

# # (method) swapcase: () -> str
# # Convert uppercase characters to lowercase and lowercase characters to uppercase.
# o = "I lovE ISLam"
# p = "i lOVE iSLAM"
# print(o.swapcase())
# print(p.swapcase())
# print("="*20) 
# ==============================================================

# # (method) startswith: (__prefix: str | Tuple[str, ...], __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> bool
# # S.startswith(prefix[, start[, end]]) -> bool
# # Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
# r = "I Love Islam"
# print(r.startswith('I')) # -> True 
# print(r.startswith('I' , 2 , 5)) # -> False

# ==============================================================


# # (method) endswith: (__suffix: str | Tuple[str, ...], __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> bool
# # S.endswith(suffix[, start[, end]]) -> bool
# # Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.
# r = "I Love Islam"
# print(r.endswith('m')) # -> True

# print(r.endswith('e' , 2, 6)) # -> true
# u = "Hello, welcome to my world."
# y = u.endswith("my world.")
# print(y)
# ==============================================================
# (method) index: (__sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int
# S.index(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
# Raises ValueError when the substring is not found.

# w = "I Love Islam"
# print(w.index("L")) #  -> 2
# # print(w.index("M")) #  -> Error
# print(w.index("I" , 1, 10 )) # -> 7
# # print(w.index("I" , 1, 6 )) # -> Error
# ==============================================================
# (method) find: (__sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int
# S.find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
# Return -1 on failure.

# x = "I Love Islam"
# print(x.find("L")) #    ->  2 
# print(x.find("M")) #    -> -1
# print(x.find("o",1 , 4)) # -> 3
# ==============================================================
# (method) rjust: (__width: SupportsIndex, __fillchar: str = ...) -> str
# Return a right-justified string of length width.
# Padding is done using the specified fill character (default is a space).

# y = " Islam "
# print(y.rjust(10,"@"))
# y = " Islam "
# print(y.ljust(16,"#"))
# ==============================================================
# (method) splitlines: (keepends: bool = ...) -> list[str]
# Return a list of the lines in the string, breaking at line boundaries.
# Line breaks are not included in the resulting list unless keepends is given and true.

# z = """Firs Line
#     Second Line
#     Third Line
#     """
# print(z.splitlines())  #  -> ['Firs Line', 'Second Line', 'Third Line']
# z = """Firs Line\nSecond Line\nThird Line"""
# print(z.splitlines())  #  -> ['Firs Line', 'Second Line', 'Third Line']
# ==============================================================
# (method) expandtabs: (tabsize: SupportsIndex = ...) -> str
# Return a copy where all tab characters are expanded using spaces.
# If tabsize is not given, a tab size of 8 characters is assumed.

# a = "I\tLov\tIslam\t."
# print(a) # -> I       Lov     Islam   .
# print(a.expandtabs(3)) #  ->  I  Lov   Islam .
# ==============================================================
# (method) istitle: () -> bool
# Return True if the string is a title-cased string, False otherwise.
# In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

# b = "I Love Islam And 3G"
# c = "I Love Islam And 3g"
# print(b.istitle())  # -> True
# print(c.istitle())  # -> False
# ==============================================================
# (method) isspace: () -> bool
# Return True if the string is a whitespace string, False otherwise.
# A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

# d = "  "
# e = ""
# print(d.isspace())  #  -> True
# print(e.isspace())  #  -> False
# ==============================================================
# (method) islower: () -> bool
# Return True if the string is a lowercase string, False otherwise.
# A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.
# f = "i love lslam"
# g = "I Love Islam"
# print(f.islower())  # --> True
# print(g.islower())  # --> False
# ==============================================================
# h = "I LOVE ISLAM"
# j = "I Love Islam"
# print(h.isupper())  #  -> True
# print(j.isupper())  #  -> False
# ==============================================================
# k = "Islam"
# l = "Islam2021"
# m = "20Islam"
# n = "I Love Islam"
# print(k.isidentifier())  #  -> True
# print(l.isidentifier())  #  -> True
# print(m.isidentifier())  #  -> False
# print(n.isidentifier())  #  -> False
# ==============================================================
# o ="AGDSFytfuytyjy"
# p ="AGDSFytfuytyjy675554498645"
# print(o.isalpha())   #   ->  True 
# print(p.isalpha())   #   ->  False
# ==============================================================
# (method) isnumeric: () -> bool
# Return True if the string is a numeric string, False otherwise.
# A string is numeric if all characters in the string are numeric and there is at least one character in the string.

# r ="888"
# s ="Islam2021"
# u ="2021Islam2021"
# print(r.isnumeric())   #   ->  True 
# print(s.isnumeric())   #   ->  False
# print(u.isnumeric())   #   ->  False
# ==============================================================
# (method) isalnum: () -> bool
# Return True if the string is an alpha-numeric string, False otherwise.
# A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

# w = "Islam"
# x = "Islam2021"
# print(w.isalnum())   # -> True
# print(x.isalnum())   # -> True
# ==============================================================
