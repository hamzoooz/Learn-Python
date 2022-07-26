
# =======================================
# print("If You Agree pres y or yes and Don't Agree Pres n or no "  )
# a = input("Do You Agree ?" )
# if a == "Y" or  a ==  "y" or  a == "Yes" or  a == "yes" or  a == "YES" :
#     print("Agreed.")
# elif a == "N" or  a == "n" or  a == "NO" or  a == "No" or  a == "no" or  a == "nO" :
#     print("Not Adreed.")
# else : # Make This Return Back If Not Recognize Input 
# print(f"\"{  a  }\" Not Recognize ")
# =======================================

# # Other Way
# print("If You Agree pres y or yes and Don't Agree Pres n or no "  )
# b = input("Do You Agree ?")
# if b in ["Y" ,"y" , "Yes","yes","YES"] :
#     print("You Agreed")
# elif b in ["N", "n", "NO", "No", "no", "nO"]:
#     print("You Not Agreed")
# else : # Make This Return Back If Not Recognize Input 
#     print(f"\"{  b  }\" Not Recognize ")
# =======================================

# Other Way

print("If You Agree pres y or yes and Don't Agree Pres n or no "  )
c = input("Do You Agree ?")
if c.lower() in ["y","yes"] :
    print("You Agreed")
elif c.lower() in ["n" , "no"]:
    print("You Not Agreed")
else : # Make This Return Back If Not Recognize Input 
    print(f"\"{  c  }\" Not Recognize ")
# =======================================

# (function) print: (*values: object, sep: str | None = ..., end: str | None = ..., file: SupportsWrite[str] | None = ..., flush: bool = ...) -> None



