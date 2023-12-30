# import the additional module
import re

# define list of places
listOfPlaces = ["Bayswater", "Table Bay", "Bejing", "Bombay"]

# define search string
pattern = re.compile("[Bb]ay")

for place in listOfPlaces:
    if pattern.search(place):
        print("%s matches the search pattern" % place)

