# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['Tim', 'Arnoldo', 'Lalo']
print(students[1])
print(students[2])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as 
# there are names in the students list. Use a for loop to print out the string 
# "[food goes here] is a good food".
foods = ('Cauliflower', 'Green Beans', 'Orange')
for food in foods:
    print (f"{food} is good for you")

#Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods
lastTwo = []
for food in foods:
    lastTwo = foods[1:3]
    if food in lastTwo:
        print(food)

#Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
    'city': 'El Centro',
    'state': 'California',
    'population': '44,158'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")