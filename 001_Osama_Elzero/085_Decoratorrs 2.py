def myDecorator(func) :
    def nestedFunc(*number):
    # def nestedFunc( n1 , n2 , n3 ):
        for num in number:
            if num < 0:
                print("Be Ware Ther One Nuber Less Than Zero !  ") 
        func( *number)
        # func( n1 , n2 , n3 )
    return nestedFunc()

@myDecorator
def calce(n1 , n2 , n3 ): 
    print(n1 + n2 + n3 )
    # return 
calce(-1 , 5 , 6 )

