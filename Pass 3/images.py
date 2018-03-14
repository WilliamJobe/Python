from PIL import Image #måste installera pillow
try:
    myimage = Image.open("Python.png")
except:
    print("Unable to load image")
myimage.load()
print(myimage.format, myimage.size, myimage.mode)
myimage.show()
