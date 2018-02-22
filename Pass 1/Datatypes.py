#Python is a dynamically typed language. Python uses values not variables :)
#Naming conventions Pascal - fix!!
a = 100
b = "foo"
c = True
d = 10.95
e = "bar"
# b is changed from string to integer dynamically
b = 4

print(a)
print(b)
print(c)
print(d)
print(a+d)

#bunch of different ways to concatenate different datatypes, format is recommended I believe
print(str(a)+e)
print(a,e)
print("Concatenate: {} {}".format(a,e))
print("Concatenate: {} {}".format(a+d,c))
print("Concatenate: %d %s " % (a,e))

#ta upp id() och minneshantering, garbage collector