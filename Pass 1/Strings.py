my_string = "Hello Python!"
print(my_string)

for i in my_string:
    print(i)

#strings are immutable i.e. can't change them but you can replace them
#code below causes error
#my_string[5] = "z"
my_string = "Whole new string"
print(my_string)

string1 ="Howdy"
string2 ="Python!!"
print("något annat", string1 + string2+"asdfasdf"+"asdfasfdsaf")
print('String1 * 5 =', string1 * 5)

string3="GoSa WiTh PyThOn!"
bacon_ipsum="Bacon ipsum dolor amet prosciutto rump short ribs pork chop venison sausage"
print(string3.upper())
print(string3.lower())
print(bacon_ipsum.split())
print(" ".join(['Bacon', 'ipsum', 'dolor', 'amet', 'prosciutto', 'rump', 'short', 'ribs', 'pork', 'chop', 'venison', 'sausage']))
print(bacon_ipsum.find("venison"))
print(bacon_ipsum.replace("Bacon","Python"))
