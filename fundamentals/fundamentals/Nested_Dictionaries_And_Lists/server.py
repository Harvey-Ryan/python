#################################################
## 1 - Update Values in Dictionaries and Lists ##
#################################################

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#############################################################################################
## Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].##
x[1][0] = 15
#print(x)

#########################################################################
## Change the last_name of the first student from 'Jordan' to 'Bryant' ##
students[0]["last_name"] = "Bryant"
#print(students[0]["last_name"])

#########################################################
## In the sports_directory, change 'Messi' to 'Andres' ##
sports_directory["soccer"][0] = "Andres"
#print(sports_directory["soccer"][0])

####################################
## Change the value 20 in z to 30 ##
z[0]['y'] = 30
#print(z[0]['y'])

############################################
## Iterate Through a List of Dictionaries ##
############################################

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for dictionary in students: ##Create variable (dictionary) inside of for loop
        first_name = dictionary['first_name']  ##assign first_name variable by calling loop variable (dictionary) then pull key inside []
        last_name = dictionary['last_name']
        print(f"first_name - {first_name}, last_name - {last_name}")
iterateDictionary(students) 

## should output: (it's okay if each key-value pair ends up on 2 separate lines;
## bonus to get them to appear exactly as below!)
## first_name - Michael, last_name - Jordan
## first_name - John, last_name - Rosales
## first_name - Mark, last_name - Guillen
## first_name - KB, last_name - Tonel

############################################
## Get Values From a List of Dictionaries ##
############################################

first_name = 'first_name'
last_name = 'last_name'
def iterateDictionary2(key, students):
    for dictionary in students: ##Create variable (dictionary) inside of for loop
        key_value = dictionary[key]  ##assign key_value variable by calling loop variable (dictionary) then pull key defined by function call parameter
        print(key_value)
iterateDictionary2(first_name, students)
iterateDictionary2(last_name, students)

###################################################
## Iterate Through a Dictionary with List Values ##
###################################################

## Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
## prints the name of each key along with the size of its list,
## and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, value in dojo.items():
        print(f"{len(value)} - {key.upper()} ") #Print locations led by "# LOCATIONS" followed by city names  and do the same for instructors.
        for item in value:
            print(item)
        print("\n")
printInfo(dojo)