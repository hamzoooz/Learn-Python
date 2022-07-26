# from cs50 import get_int

# def main():
#     i = get_positive_int()
#     print(i)

# def get_positive_int():
#     while True :
#         n = int(input("enter POsitive Integer: "))
#         if n > 0 :
#             break
#     return n
# main()

def main():
    i = get_positive_int()
    print( i )
    
def get_positive_int():
    while True :
        n = int(input("Enter Your Number : "))
        if n < 0:
            print(" This Negative Number ")
        elif n > 0:
            print("This positive Number : ")
        return n 
main()