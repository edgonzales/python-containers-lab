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