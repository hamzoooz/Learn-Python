# class type(o: object)
# class type(name: str, bases: Tuple[type, ...], dict: Dict[str, Any])
# type(object_or_name, bases, dict)
# type(object) -> the object's type
# type(name, bases, dict) -> a new type
# Full name: builtins.type
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str

# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.
# Full name: builtins.str

# a = "#001_Osama_Elzero"
# type(a)

# a = 10 
# b = 10 
a = input("inter one Value ")
b = input("inter tow Value ")
if  a < b  : 
    print(a , "is larg than ", b )
elif a == b  :
    print(a , "equal ", b )
else :
    print(a , "is larg than ", b )
