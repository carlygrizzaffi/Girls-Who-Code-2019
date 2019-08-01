#import jsonToPython
#make an empty dictionary
#creat a survey to ask IN A LOOP (whole data data table)
    #create temporary empty dictionary (row in data table)
    #name
    #eye color
    #favorite ice cream flavor
    #birth birthmonth

    #with values form survey, create  (update orional dictoinary, i.e add the row to the data table)

    #store objects in dictionary form line 2
    #close LOOP

#convert to JSON


import json
pythondictionary={};
tempobject={};

while True:
    name = input('What is your name?')
    color = input('What is your eye color?')
    icecream = input('What is your favorite ice cream flavor?')
    birthmonth = input('In what month were you born?')

    tempobject = {
    name:{
    "color":color,
    "icecream":icecream,
    "birthmonth":birthmonth
        }
    }

    value = {color, icecream, birthmonth}

    pythondictionary.update({name:value})

    print(pythondictionary)

    pythondictionarytojson = json.dumps(tempobject)
