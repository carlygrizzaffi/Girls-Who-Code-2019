import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.random import RandomState
import aids
from colors import rgb, hsv, hex, random
subjectivity = np.random.randn(1000)

plt.hist(subjectivity, bins = 30, color = "blue")
plt.title("Aids")
#Set the x and y labels.
plt.xlabel("Value")
plt.ylabel("Frequency")
#Show your plot.

plt.close()
aids_data_country = []
list_of_all_aids = aids.get_reports()
# Data for pie chart
labels = []
sizes = len(list_of_all_aids)
delete_repeats = []
colors = []
print(colors)
for data in list_of_all_aids:
    aids_data_country.append(data["Country"])
occurences_country = []
# Plot
for country in aids_data_country:
    if country not in delete_repeats:
        occurences_country.append(aids_data_country.count(country))
        delete_repeats.append(country)
    if country not in labels:
        color_string = "%s" % random().rgb

        colors.append(color_string)
        labels.append(country)
print(occurences_country)
print(labels)
plt.pie(occurences_country, labels=labels)

plt.axis('equal')
plt.show()
plt.close()
