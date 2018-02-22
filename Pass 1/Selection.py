import random
random_number = random.randrange(1,100)

if random_number < 50:
    print("The %d < 50" % random_number)
elif random_number == 50:
   print("The %d = 50" % random_number) 
else:
    print("The %d > 50 " % random_number)

#ta upp logiska operationer här