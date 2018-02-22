#sneak in a little example of importing a library:)
import os

list2 = ["foo","man","chu","Elvis"]

#iterating through a list
for i in list2:
    print(i)

#iterating through a dictionary
for j, k in os.environ.items():
    print("%s=%s" % (j,k))

launch = 10
while launch > 0:
    print(launch)
    launch -= 1
print("Blastoff!")

for i in range(0,20,1):      #for(i=0;i<20;i=i+1)i++
    print(i)
