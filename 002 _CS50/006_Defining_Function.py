# # Creat For Loop By Using Built-in Function 
# for i in range(8): # repeat 8th once
#     print("Python it Awesome")
# =====================================

# # # Creat For Loop By Using Helper Function 
# def awesome(): 
#     print("Python it Awesome")
#     # print("Python it Awesome" , end = " || ")
# for i in range(3):
#     awesome()
# =====================================

# # Creat For Loop By Using Helper Function  To Ignoer Order between Functions
# def main():
#     for i in range(8):
#         awesome()

# def awesome():
#     print("Python it Awesome")
# main()
# =====================================
 
 # Error Need Fix
# To More Flexable In Function use  Arg
a = int(input("Enter Number you wante To Repeat? "))
def awesome( b ):
    i = 1
    for i in range(a):
        print(i , end="");print(" => Python it Awesome")
        i += 1
## main(a)
awesome(a)
# # =====================================
