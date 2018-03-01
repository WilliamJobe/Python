class MyMath:
    myInt = 12345 #class variable the same for all instances
    
    def __init__(self, x, y):
        self.x = x #instance variables
        self.y = y

test1 = MyMath(3.14,2.718)
test2 = MyMath(42,1337)
print(test1.x,test1.y,test1.myInt)
print(test2.x,test2.y,test2.myInt)