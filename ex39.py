# Created by Ibrahim Elsakka on 4/29/2017

# create a mapping of state to abbreviation

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'Michigan': 'MI',
}

# create a basic set of states and some cities in them

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
