"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def sortUSA():
    '''Return all the cities in the USA in alphabetical order'''
    a = list()
    for i in locations:
        for j in locations[i]:
            # print(locations[i])
            if j == 'USA':
                for k in locations[i][j]:
                # print(locations[i][j])
                    a.append(k)
    return sorted(a)
    # return sorted(a)


def alphaAsia():
    '''Return all the cities in Asia continent in alphabetical order'''
    a=list()
    for i in locations:
        if i == 'Asia':
            for j in locations[i]:
                for k in locations[i][j]:
                    a.append(k+" - "+j)
    return a

    
# Note: Check for test cases to understand the output format.
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# alphaAsia(locations)


