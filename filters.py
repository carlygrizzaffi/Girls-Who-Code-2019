
# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.

darkBlue = (0, 51, 76)
yellow = (252, 227, 166)
red = (217, 26, 33)
lightblue = (112, 150, 158)
width = 1800
height = 1200
im = Image.open("wombat2.jpg")
pixels = im.getdata()
print("Image loaded")
width,height = im.size


newImage = []


for elem in pixels:
    x = elem[0] + elem[1] + elem[2]
    if x < 182:
        newImage.append(darkBlue)
    elif 182 < x < 364:
        newImage.append(red)
    elif 364 < x < 546:
        newImage.append(lightblue)
    else:
        newImage.append(yellow)

colorimage = Image.new("RGB",(width,height),"white")
colorimage.putdata(newImage)
colorimage.show()
