#numbers = range(1,11)
evens_squared = [number * number for number in range(1,11) if number % 2 == 0] 

'''
for num in numbers:
    if num % 2 == 0:
        evens_squared.append(num*num)
'''
#print(numbers)
print(evens_squared)

# Using single list comprehension, and the following list:
#part 1
ages = [5, 15, 64, 27, 84, 26]
# Return a list of only the odd ages.
odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)
#part 2
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a list with chickens whose name is more than 10 characters
long_chicken_names = [chicken for chicken in chicken_names if len(chicken)>10]
print(long_chicken_names)
# Return a list of chickens whose name starts with the letter H
chicken_names_starting_with_h = [chicken for chicken in chicken_names if chicken[0] == "H"]
print(chicken_names_starting_with_h)
#part 3
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Build a new list, with the first letter from each word
new_words = [word[0] for word in words]
print(new_words)
# Convert each letter to lower case
new_words_lowercase = [word[0].lower() for word in words]
print(new_words_lowercase)