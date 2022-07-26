        # ===================================#
        # ===== String Indexing & Slincing ==#
        # ===================================#

#  [1] All Data In Python Is Object
#  [2] Object Contain Element
#  [3] Every Element Has Its Own Index
#  [4] Python Use Zero Based Indexing ( Index Start From Zero )
#  [5] Use Square Brackets To Access Element 
#  [6] Enable Accessing Parts Of String , Tupes or Lists
# ===================================

# Indexing ( Access Single Item )
# Syntax => function(name_string[N.o Index])

myString = "I Love Islam"

print(myString[0])  # Index 0 => I
print(myString[8])  # Index 8 => s
print(myString[-1]) # Index -1 => m First Character From End 
print(myString[-5]) # Index -5 => m 5th Character From End 

# ===================================

# Slicing ( Access Multiple Sequence Items)
# Syntax => [Start:End] or [Start:End:steps] End Note Included Accept int

print(myString[:6])       # Start is Note Here will Start from 0 => I Love
print(myString[2:])       # If Stat Is note here will go To End  => love Islam
print(myString[:])        # Full String Data
print(myString[2:6])      # slicing from 0 to 6th => "love"
print(myString[-10:-6])   # slicing from -10th to -6th => "love"

print(myString[::2])      # Skip one and the Next character 
print(myString[::3])      # Skip tow and the Next character 
