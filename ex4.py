# Created by Ibrahim Elsakka on 4/7/2017

# we have 100 cars
cars = 100
#we have 4 spaces per car
space_in_a_car = 4.0
# we have 30 drivers
drivers = 30
#we jave 90 passengers
passengers = 90
# we have 100 - 30 = 70 cars not driven
cars_not_driven = cars - drivers
# we have 30 cars driven
cars_driven = drivers
# we have 30 * 4.0 = 120.0 carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# we have 90 / 30 = 3 average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only,", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."