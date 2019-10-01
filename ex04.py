# total number of cars
cars = 100
# total space in each car
space_in_a_car = 4
# total number of drivers
drivers = 30
# total number of passengers
passengers = 90
# total number of cars that aren't driven
cars_not_driven = cars - drivers
# total number of cars that are driven
cars_driven = drivers
# total number of passengers that all the available cars can transport
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers that can fit into available cars
average_passengers_per_car = passengers / cars_driven

print('There are ', cars, ' cars available.')
print('There are only ',drivers,' drivers available.')
print('There will be ', cars_not_driven, ' empty cars today.')
print('We can transport ', carpool_capacity, ' people today.')
print('We have ', passengers, ' to carpool today.')
print('We need to put about ', average_passengers_per_car, ' in each car.')
