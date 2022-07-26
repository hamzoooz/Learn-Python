# Python      => Loosely Type Lannguage (|No Need To Declaration Var)
# Data Type   => Data Types (List - set - tuple - range - dict)
# All Thing In Python Via Object
#

# Data Type
# Can Classify Data Type By 

# [01] Numeric =>

    #[01] => int                    -> a = 123
    #[02] => float                  -> a = 1.5
    #[03] => Complex                -> a = 5j

# [02] Mapping  => [04] => Dict     -> a = {"Name" : "hamzooz" , "Age" : 23}

# [03] Boolean  => [05] => Bool     -> a = True || False

# [04] Set      => [06] => set      -> a = {"Name" , "hamzooz" , "Age" , 23}

# [05] Sequence => 
    #[01] => Text Type 
        # [07] str                  -> a = "Python"
    #[02] => Number                 
        # [08] Set     -> a = {1 , 2 ,3 ,4}  like Array & Can Edit Size & unordered  & unIndexed Ietm & immutable & unChangeable but can add || remove & Do not Allows Duplicate Vlalue 
        # [09] Tuple   -> a = (1 , 2 ,3 ,4)  like Array & Can Edit Size & ordered  & Indexed Ietm & Immutable & unChangeable & Allows Duplicate Vlalue 
        # [10] Range   -> a = range(5)
        # [11] List    -> a = [1 , 2 ,3 ,4]  & Can Edit Items  & ordered  & Indexed Ietm & Mutable & Changeable & Allows Duplicate Vlalue 

# built-in Python 
# Bool  => [True || False]
# Float => [1.2345]
# int   => [123]
# str   => ["Hello Python"]
# range =>  Sequence Of Numbers 
# list  =>  Sequence Of mutable
# tuple =>  Sequence Of immutable
# dict  =>  Collection Of Key-Value Paires
# set   =>  Collection Of unique Value


a = {"Name" : "hamzooz" , "Age" : 23}
b = {"Name" , "hamzooz" , "Age" , 23}
c = (1 , 2 ,3 ,4)
d = [1 , 2 ,3 ,4]
print(type(a))
print(type(b))
print(type(c))
print(type(d))