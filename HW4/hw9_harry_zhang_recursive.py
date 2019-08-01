# In all the exercises that follow, insert your code directly in this file
# where you find a comment saying "Answer to Question [...]"
#
# IMPORTANT NOTES: 
#
# 1) THIS IS A PROGRAMMING COURSE. :-) THIS MEANS THAT THE ANSWERS TO THESE QUESTIONS
# ARE MEANT TO BE DONE IN CODE AS MUCH AS POSSIBLE. E.G., WHEN A QUESTION SAYS "COUNT
# THE NUMBER OF TIMES THAT [...]" YOU SHOULD INTERPRET THIS AS "WRITE CODE THAT COUNTS
# THE NUMBER OF TIMES THAT [...]". USE YOUR BEST JUDGMENT AND YOU WILL DO FINE. :-)
#
# 2) WHEN A QUESTION PROVIDES A VALUE FOR YOU TO USE IN COMPUTATIONS, FIRST STORE IT IN
# A VARIABLE AND WRITE CODE THAT MAKES USE OF THAT VARIABLE.
#
# 3) WHENEVER A QUESTION DOES NOT SPECIFY A PARTICULAR WAY TO DO SOMETHING,
#    THEN YOU CAN DO IT *ANY* WAY. :-)

"""

Intro

In this assignment you will explore the Star Wars API. This is an 
open and free-to-use API that provides all information you could 
possibly need about... Star Wars!

You can read about the project on the page

http://swapi.co/about

and access the technical documentation for the API on the page

http://swapi.co/documentation

As mentioned in class this week, using an API requires that you get
the relevant information from its documentation. This API has great
documentation, so be sure to check it carefully. The documentation
contains all the details you need to answer the questions below.


Note 1: you are not meant to use the Python bindings provided on
the site. Instead, use the two modules we used in class (requests and
json) to answer all questions below.


Note 2: if at any point you get an error message ending with a line that reads

requests.exceptions.SSLError:  (...)

then pass the additional argument verify=False in _all_ calls to requests.get(), eg:
    
    r = requests.get(url, verify=False)

or if you want to pass the dictionary 'parameters' to the server:
    
    r = requests.get(url, params=parameters, verify=False)
    
"""

"""

Question 1


You can access information about 10 planets in Star Wars by sending a
get request to

http://swapi.co/api/planets/

1.1) Using a for loop, print out the names of all 10 planets returned
by that call.



1.2) Write a function called get_planet_population that takes as an
argument a string called 'planet_name'. Your function should then
return (note: *not* print):

   - the population of that planet *as a number*, if that planet is
   among the 10 planets listed in the data returned by an API call to
   http://swapi.co/api/planets/ and the API lists its population; or
   
   - the special Python value None, if that planet is among the 10
   planets listed in the data returned by an API call to
   http://swapi.co/api/planets/ and the API tells you the population
   is 'unknown'.
   
   - the string "unknown planet", if that planet is not among the 10
   planets listed in the data returned by an API call to
   http://swapi.co/api/planets/.

   
Notes for Question 1.2: 
    
    1) Your function should be case-insensitive in the way it handles
    planet_name and matches it against the planets available through
    that API call.
    
    2) The planet API supports a 'search' feature which you are not
    meant to use here. 
    
    3) Please note None (no quotes) is a special Python value and
    different from the string 'None'. In the second scenario described
    above, your function should return the special Python value.

    
1.3) Print the names of all planets, from among the 10 planets
obtained by sending a request to http://swapi.co/api/planets/, that
have a population less than or equal to 30,000,000 and whose climate
description includes the word 'temperate'.

Notes for Question 1.3:
    
    1) Please note that some planets have a population that is listed
    as 'unknown' and that string cannot be converted into a number. In
    your if statement you will have to handle that case (population ==
    'unknown') separately, otherwise you will get an error when you
    try to convert the population into a number. Obviously, planets
    with a 'unknown' population should not be listed by your code.
    
    2) Please note that the 'climate' for a planet often is a
    description containing multiple words. You merely have to check if
    'temperate' is found in that string.

"""

# Answer to Question 1.1
import requests
url = "https://swapi.co/api/planets/?format=json"
r = requests.get(url)
r_json = r.json()
results = r_json['results']
names = list()
for i in results:
    names.append(i['name'])
print(names)
# Answer to Question 1.2


# This function gives the population of the planet
# @param:   planet_name A String specifying the name of the planet
# @return:  if 'unknown',return None
#           if not in the 10 planets returned by the API, return "unknown planet"
#           else, return the integer value of the population.   
def get_planet_population(planet_name):
    for j in results:
        if j['name'].upper() == planet_name.upper():
            if j['population'] == 'unknown':
                return None
            else:
                return int(j['population'])
    return "unknown planet"
#print(get_planet_population('hoth'))
#print(get_planet_population('naboo'))
    

# Answer to Question 1.3
    

# This function gives the list of names of planets of population under a certain amount
# @param:   bound The amount under which the population of the planet must be
#           climate The String that the climate of the planet must include
# @return:  list of names of accepted planets
    
def printPlanet(climate,bound):
    output = list()
    for j in results:
        if type(get_planet_population(j['name'])) == int :
            if climate in j['climate'] and get_planet_population(j['name']) <= bound:
                output.append(j['name'])
        else:
            continue
    return output

print(printPlanet('temperate',30000000))
"""

Question 2

In the previous question, you were only asked to use the 10 planets
returned by a first call to the API at http://swapi.co/api/planets/.
However, this API lists information about many more planets. What
happened was that SWAPI (both for planets as well as for any other
type of information) only serves 10 results at a time and then expects
your code to send additional requests for the rest of the data, which
will be served in "batches" of 10 results at a time. This is very
common behavior "in the real world", since it avoids needlessly
wasting bandwidth.

In this question you will use a while loop to issue requests for
information about all starships in Star Wars. The API to use is
located at

http://swapi.co/api/starships/

Note that the data you get back is a dictionary that contains a
key called 'next'. The value for that key is the URL to which you
should send the next request using requests.get() to fetch the
additional batch of information about the following 10 starships. 

2.1) Retrieve information about *all* starships available via this API
and store it in a list called 'starships'.

Hint: As mentioned above, the typical way to fetch all results from an
API is to use a while loop that will retrieve a batch of 10 results,
add them to a list (or similar data structure) and then send another
request for more results *if the value for the key 'next' in the
dictionary in the previous response contained a URL*. When you
retrieve the final batch of results and no more results are available,
the server will send you a dictionary that will probably still contain
results you need to add to the list but the value for key 'next' will
be None (rather than a URL). Therefore, one common strategy is to have
your while loop end when the value for key 'next' == None.



2.2) Print out the name of the fastest starship Star Wars. As
indicated in the documentation, speed is given by the MGLT (Maximum
number of Megalights) attribute of a starship.  

"""

# Answer to Question 2.1
import requests
# Answer to Question 1.2



# This function gives the dictionary fo all starship information
# @param: 
# @return:  dictionary containing all starship information.
#           The keys are ships' names and the values are all its information,excluding the name
def get_starships():
    url = "https://swapi.co/api/starships/?format=json"
    starships = dict()
    while url != None:
        r = requests.get(url)
        r_json = r.json()
        results = r_json['results']
        for i in results:
            name = i['name']
            del i['name']
            starships[name] = i 
        url = r_json['next']     
    return starships


# This function shows the starship information
# @param:
# @return:
def seeShipNames():    
    print(list(get_starships().keys()))
seeShipNames() 


# Answer to Question 2.2


# This function gets the dictionary of all speeds and their corresponding names
# @param:
# @return: dictionary of all speeds and their corresponding starship names
def getShipBySpeed():
    starships = get_starships()
    starships_by_speed = dict()
    for i in starships.keys():
        speed = starships[i]['MGLT']
        try:
            speed = int(speed)
        except:
            continue
        if speed not in starships_by_speed.keys():
            starships_by_speed[speed] = [i]
        else:
            starships_by_speed[speed].append(i)
    return starships_by_speed


def recursiveFindFastest(listOfSpeed):
    if len(listOfSpeed) == 1:
        return listOfSpeed[0]
    else:
        halfLength = int(len(listOfSpeed)/2)
        lower = recursiveFindFastest(listOfSpeed[:halfLength])
        upper = recursiveFindFastest(listOfSpeed[halfLength:])
        if lower < upper:
            return upper
        else:
            return lower


speed = getShipBySpeed()
fastest = speed[recursiveFindFastest(list(speed.keys()))]
fastestString = ''
for i in fastest:
    fastestString += i
    fastestString += ";"
print("Fastest ship is:",fastestString,sep = ' ')

