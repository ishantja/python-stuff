# dictionaries are special structure which store information in key value pairs
# you can access by refering to its key
# compare to normal dictionary
#word is a key and value is the actual definition

#program to convert three digit month name to the full month

monthConversions = { #[] list () tuple {} dictionary
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    0: "April",
    1: "May",
    #"Jan": "April" #not allowed as keys need to to unique
}

print(monthConversions["Mar"]) #this is one way to access dictionary . Refering to key gives the value associated with it.
print(monthConversions.get("Dec","Not a valid key")) #gives none if not available instead of program exiting with code 1
#we can also setup the default value that is returned
print(monthConversions.get(0))

#
