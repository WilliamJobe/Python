class MyMath:
    myInt = 12345 #class variable the same for all instances
    """“Private” instance variables that cannot be accessed except from
    inside an object don’t exist in Python. However, there is a
    convention that is followed by most Python code: a name prefixed
    with an underscore (e.g. _spam) should be treated as a non-public
    part of the API (whether it is a function, a method or a data member).
    It should be considered an implementation detail and subject to change without notice. Since
    there is a valid use-case for class-private members (namely to avoid name clashes of names
    with names defined by subclasses), there is limited support for such a mechanism,
    called name mangling. Any identifier of the form __spam (at least two leading
    underscores, at most one trailing underscore) is textually replaced with
    _classname__spam, where classname is the current class name with leading
    underscore(s) stripped. This mangling is done without regard to the syntactic
    position of the identifier, as long as it occurs within the definition of a class."""

    __privateString = "Behandla som privat och blir manglad :)"

    def __init__(self, x, y):
        self.x = x #instance variables
        self.y = y
        print(self.__privateString)

test1 = MyMath(3.14,2.718)
test2 = MyMath(42,1337)
print(test1.x,test1.y,test1.myInt)
print(test2.x,test2.y,test2.myInt)
#print(test2.__privateString)