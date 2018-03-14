
file = open("log.txt","w") 
 
file.write("Hej världen!!\n") 
file.write("Lite mer text") 
 
file.close() 

file = open("log.txt","r") 
print(file.read())

#with open("log.txt") as file:  
#data = file.read() 
#do something with data 