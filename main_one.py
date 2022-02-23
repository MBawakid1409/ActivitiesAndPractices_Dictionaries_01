# Activities & Practices
# --------- [Dictionaries] ---------
print("--------- [Dictionaries] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
# Make a Dictionary
menu = {"avocado toast": 6, "carrot juice": 5, "bluberry muffin": 2}
print(menu) # {'avocado toast': 6, 'carrot juice': 5, 'bluberry muffin': 2}
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)
# {'von Trapp': ['Johannes', 'Rosmarie', 'Eleonore'], 'Corleone': ['Sonny', 'Fredo', 'Michael']}
print("----------------------------------")
# Practise 02
print("Practise #02")
# Add A Key
# menu = {"avocado toast": 6, "carrot juice": 5, "bluberry muffin": 2}
menu["cheesecake"] = 8
print(menu) 
# {'avocado toast': 6, 'carrot juice': 5, 'bluberry muffin': 2, 'cheesecake': 8}
print("----------------------------------")
# Practise 03
print("Practise #03")
# Add Multiple Keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print(sensors) # {'living room': 21, 'kitchen': 23, 'bedroom': 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors) # {'living room': 21, 'kitchen': 23, 'bedroom': 20, 'pantry': 22, 'guest room': 25, 'patio': 34}
print("----------------------------------")
# Practise 04
print("Practise #04")
# Overwrite Values
# {'avocado toast': 6, 'carrot juice': 5, 'bluberry muffin': 2, 'cheesecake': 8}
menu["avocado toast"] = 7
print(menu)
# {'avocado toast': 7, 'carrot juice': 5, 'bluberry muffin': 2, 'cheesecake': 8}
print("----------------------------------")
# Practise 05
print("Practise #05")
# Dict Comprehensions
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students) # {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print("----------------------------------")
# Practise 06
print("Practise #06")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks) # <zip object at 0x000001F11436E480>
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine) 
# {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}
print("----------------------------------")
# Practise 07
print("Practise #07")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "Imagine", "What's going on", "Respecet", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

# adding new entries
plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
# {'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 21, "What's going on": 89, 'Respecet': 5, 'Respect': 94, 'Purple Haze': 1}, 'Sunday Feelings': {}}
print("----------------------------------")
# Practise 08
print("Practise #08")
# Get A Key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights["Shanghai Tower"]) # 632
print("----------------------------------")
# Practise 09
print("Practise #09")
# Get an Invalid Key
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# print(building_heights["Landmark 81"]) # KeyError: 'Landmark 81'
# to avoid this error is to first check if the key exists in the dictionary:

# key_to_check = "Landmark 81"

# if key_to_check in building_heights:
#     print(building_heights["Landmark 81"])

# This will not throw an error, because [key_to_check in building_heights] will return [False], and so we never try to access the key.
print("----------------------------------")
# Practise 10
print("Practise #10")
# Try/Except to Get a Key
# We saw that we can avoid [keyError]s by checking by checking if a key is in a dictionary first. Another method we could use is a try/except:
key_to_check = "Landmark 81"
try:
    print(building_heights[key_to_check])
except KeyError:
    print("That key doesn't exist!") # That key doesn't exist!

# When we try to access a key that doesn't exist, the program will go into the [except] block and print "That key doesn't exist!"    
print("----------------------------------")
# Practise 11
print("Practise #11")
# Safely Get a Key
# Dictionaries have a [.get()] method to search for a value instead of the
# [my_dict[key]] notation we have been using. If the key you are trying to 
# [.get()] does not exist, it will return [None] by default:

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights.get("Shanghai Tower")) # 632
print(building_heights.get("My House")) # None
print(building_heights.get("My House", 0)) # Default Value : 0
print(building_heights.get("Al-Baik", 'No Value')) # Default Value : No Value
print("----------------------------------")
# Practise 12
print("Practise #12")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id) # 100019
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id) # 100000
print("-------------")
print(user_ids)
# {'teraCoder': 100019, 'pythonGuy': 182921, 'samTheJavaMaam': 123112, 'lyleLoop': 102931, 'keysmithKeith': 129384}
print("----------------------------------")
# Practise 13
print("Practise #13")
# Delete a Key
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize")) # "Gift Basket"
print(raffle)
# Output: {223842: 'Teddy Bear', 872921: 'Concert Tickets', 412123: 'Necklace', 298787: 'Pasta Maker'}
print(raffle.pop(100000, "No Prize")) # "No Prize"
print(raffle)
# Output: {223842: 'Teddy Bear', 872921: 'Concert Tickets', 412123: 'Necklace', 298787: 'Pasta Maker'}
print(raffle.pop(872921, "No Prize")) # "Concert Tickets"
print(raffle)
# Output: {223842: 'Teddy Bear', 412123: 'Necklace', 298787: 'Pasta Maker'}
print("----------------------------------")
# Practise 14
print("Practise #14")
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

print(health_points) # 20
health_points += available_items.pop("stamina grains", 0)
print(health_points) # 35
health_points += available_items.pop("power stew", 0)
print(health_points) # 65
health_points += available_items.pop("mystic bread", 0)
print(health_points) # 65

print(available_items)
# {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}

health_points += available_items.pop("Homba Gomba", 10)
print(health_points) # 75

print(available_items)
# {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}
print("----------------------------------")
# Practise 15
print("Practise #15")
# Get All Keys
# Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:
print(list(test_scores)) 
# Output: ['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Dina']

# Dictionaries also have a [.keys()] method that returns a [dict_keys] object. A [dict_keys] object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. The dict_keys object returned by [.keys()] is a set of the keys in the dictionary. You cannot add or remove elements from a [dict_keys] object, but it can be used in the place of a list for iteration:

for student in test_scores.keys():
    print(student) 
# Output:
# Grace
# Jeffrey
# Sylvia
# Pedro
# Martin
# Dina

print("----------------------------------")
# Practise 16
print("Practise #16")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
print(users)
# dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])

lessons = num_exercises.keys()
print(lessons)
# dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])

print("----------------------------------")
# Practise 17
print("Practise #17")
# Get All Values

# Dictionaries have a [.values()] method that returns a [dict_values] object (just like a [dict_keys] object but for values!) with all of the values in the dictionary. It can be used in the place of a list for iteration:

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
    print(score_list)
# Output:
# [80, 72, 90]
# [88, 68, 81]
# [80, 82, 84]
# [98, 96, 95]
# [78, 80, 78]
# [64, 60, 75]
print("-----------------")
# There is no built-in function to get all of the values as a list, but if you really want to, you can use:

print(list(test_scores.values()))
# Output: [[80, 72, 90], [88, 68, 81], [80, 82, 84], [98, 96, 95], [78, 80, 78], [64, 60, 75]]

print("----------------------------------")
# Practise 18
print("Practise #18")

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
    total_exercises += exercises

print(total_exercises) # 115

print("----------------------------------")
# Practise 19
print("Practise #19")
# Get All Items

#    You can get both the keys and the values with the [.items()] method. like [.keys()] and [.values()], it returns a [dict_list] object. Each element of the [dict_list] returned by [.items()] is a tuple consisting of: # (key, value) 

# so to iterate through, you can use this syntax:

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")

# Output:
# Apple has a value of 184 billion dollars.
# Google has a value of 141.7 billion dollars.
# Microsoft has a value of 80 billion dollars.
# Coca-Cola has a value of 69.7 billion dollars.
# Amazon has a value of 64.8 billion dollars.

print("----------------------------------")
# Practise 20
print("Practise #20")

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20}

inventory["invisible knife"] = 40
inventory["mithril shield"] = 25

print(inventory)
# {'iron spear': 12, 'invisible knife': 40, 'needle of ambition': 10, 'stone glove': 20, 'mithril shield': 25}

print("----------------------------------")
# Practise 21
print("Practise #21")

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}

print(combo_meals[2]) # ['hamburger', 'fries', 'soda']

print("----------------------------------")
# Practise 22
print("Practise #22")

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
 
for element in oscars:
  print(element)

# Output:
# Best Picture
# Best Actor
# Best Actress
# Animated Feature

print("----------------------------------")
# Practise 23
print("Practise #23")

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(inventory.get("stone glove", 30)) # 20
print(inventory.get("Homba Gomba", 70)) # 70

print(inventory) 
# {'iron spear': 12, 'invisible knife': 30, 'needle of ambition': 10, 'stone glove': 20, 'the peacemaker': 65, 'demonslayer': 50}

print("----------------------------------")
# Practise 24
print("Practise #24")

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}

# print(combo_meals[3]) # KeyError

print("----------------------------------")
# Practise 25
print("Practise #25")

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
 
print(12 in inventory) # False
# This code checks for the existence of 12 as a key in the dictionary. Although it is a value in the dictionary, it is not a key.

print("----------------------------------")
# Practise 26
print("Practise #26")

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}

print(combo_meals.get(3, ["hamburger", "fries"])) # ['hamburger', 'fries']

print(combo_meals)
# {1: ['hamburger', 'fries'], 2: ['hamburger', 'fries', 'soda'], 4: ['veggie burger', 'salad', 'soda'], 6: ['hot dog', 'apple slices', 'orange juice']}
# There is no key 3 in this dictionary, so the default provided to the .get() function, ["hamburger", "fries"], will be printed.

print("----------------------------------")
# Practise 27
print("Practise #27")

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
 
print("the peacemaker" in inventory) # True
# This code checks for the existence of "the peacemaker" as a key in the dictionary.

print("----------------------------------")
# Practise 28
print("Practise #28")

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
 
raffle.pop(561721, "No Value")
print(raffle) # No Value
# {223842: 'Teddy Bear', 872921: 'Concert Tickets', 320291: 'Gift Basket', 412123: 'Necklace', 298787: 'Pasta Maker'}
# The command .pop() will try to remove the nonexistent key 561721 from the dictionary, so raffle will remain unchanged.

print("----------------------------------")
# Practise 29
print("Practise #29")

print("----------[Mini Project - Scrabble]----------")
# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

# Build your Point Dictionary

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points *= 2

letter_to_points = {letter:playcount for letter, playcount in zip(letters, points)}

letter_to_points[" "] = 0

# test print
print(letter_to_points)
# Output:
# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}

# Score a Word

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total  

brownie_points = 'BROWNIE'
print(score_word(brownie_points))  # 15

# Score a Game

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points    

update_point_totals()
print(player_to_points) 
# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# Ideas for Further Practice!

def play_word(player, word):
    player_to_words[player].append(word)
    print(update_point_totals())

play_word("player1", "CODE") # None


print(player_to_words)
# {'player1': ['BLUE', 'TENNIS', 'EXIT', 'CODE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

print("----------------------------------")
# Practise 30
print("Practise #30")

# Write a function named [sum_values] that takes a dictionary named [my_dictionary] as a parameter. The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  values_points = 0
  for value in my_dictionary.values():
    values_points += value
  return values_points

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

print("----------------------------------")
# Practise 31
print("Practise #31")

# Create a function called [sum_even_keys] that takes a dictionary named [my_dictionary], with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]           
    return total        

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

print("----------------------------------")
# Practise 32
print("Practise #32")

# Create a function named [add_ten] that takes a dictionary with integer values named [my_dictionary] as a parameter. The function should add 10 to every value in [my_dictionary] and return [my_dictionary]

def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary 


print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

print("----------------------------------")
# Practise 33
print("Practise #33")

# Create a function named [values_that_are_keys] that takes a dictionary named [my_dictionary] as a parameter. This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
    list_sum = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            list_sum.append(value)
    return list_sum        


print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

print("----------------------------------")
# Practise 34
print("Practise #34")

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  largest_key = 0
  largest_value = 0
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

print("----------------------------------")
# Practise 35
print("Practise #35")

# Write a function named [word_length_dictionary] that takes a list of strings named [words] as a parameter. The function should return a dictionary of key/value pairs where every key is a word in [words] and every value is the length of that word.

def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths    
        
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

print("----------------------------------")
# Practise 36
print("Practise #36")

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs        


print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

print("----------------------------------")
# Practise 37
print("Practise #37")

# Create a function named [unique_values] that takes a dictionary named [my_dictionary] as a parameter. The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)



print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

print("----------------------------------")
# Practise 38
print("Practise #38")

# Create a function named [count_first_letter] that takes a dictionary named [names] as a parameter. [names] should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

# So in example above, the function would return:
# {"S" : 4, "L": 3}

def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters



print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

