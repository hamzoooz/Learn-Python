import pyfiglet 
import termcolor
# help(pyfiglet)
def myDecorator(func) :
    def nestedFunc():
        print("######################## ")
        print( termcolor.colored( pyfiglet.figlet_format(func()) ,color="blue"))
        # print("#######", termcolor.colored( pyfiglet.figlet_format(func()) ,color="blue") , "######")
        print("######################## ")
    return nestedFunc()

# @myDecorator
# def sendNote() : 
#     print(termcolor.colored("########   Note    #########" ,color="blue"))

@myDecorator
def sayHow() : 
    # print(termcolor.colored("########   Note    #########" ,color="blue"))
    # print("How Are You")
    return "How Are You "

# sendNote()
sayHow()