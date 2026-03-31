import random
 
print("Welcome")
print("Choose a story template:")
print("1 - Hospital Stay")
print("2 - Camping Trip")
print("3 - Enchanted Castle")
 
choice = input("Enter 1, 2 or 3: ")
 
while choice not in ("1", "2", "3"):
    print("Please enter 1, 2 or 3")
    choice = input("Enter 1, 2 or 3: ")
    
    #template one
 
if choice == "1":
    print("\nOk! Let's do the Hospital story.")
    print("Hi, I will ask you for some words, just type them and press enter.\n")
 
    number = input("Type a number: ")
    time_measure = input("Type a measure of time (example: days, weeks): ")
    transport = input("Type a mode of transportation (example: taxi, bike): ")
    adjective = input("Type an adjective (example: weird, huge): ")
    adjective2 = input("Type another adjective: ")
    noun = input("Type a noun (example: table, cloud): ")
    color = input("Type a color: ")
    body_part = input("Type a part of the body: ")
    verb = input("Type a verb (example: run, sing): ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type one more noun: ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type a food (example: pizza, soup): ")
    adjective3 = input("Type one more adjective: ")
    silly_word = input("Type a silly made-up word (example: flurp, snazzle): ")
 
    ending = random.choice(["Woww, What a story!"])
 
    print("\n--- YOUR STORY ---\n")
    print("It was about " + number + " " + time_measure + " ago when I arrived at the hospital in a " + transport + ".")
    print("The hospital is a/an " + adjective + " place, there are a lot of " + adjective2 + " " + noun + " here.")
    print("There are nurses here who have " + color + " " + body_part + ".")
    print("If someone wants to come into my room I told them that they have to " + verb + " first.")
    print("I've decorated my room with " + number2 + " " + noun2 + ".")
    print("Today I talked to a doctor and they were wearing a " + noun3 + " on their " + body_part2 + ".")
    print("I heard that all doctors " + verb2 + " " + noun4 + " every day for breakfast.")
    print("The most " + adjective3 + " thing about being in the hospital is the " + silly_word + " " + noun + "!")
    print("\n" + ending)
    
    
    #template two
elif choice == "2":
    print("\nLet's do the Camping story.")
    print("I will ask you for some words, just type them and press enter.\n")
 
    name = input("Type a person's name: ")
    noun = input("Type a noun (example: guitar, rope): ")
    feeling = input("Type an adjective/feeling (example: excited, nervous): ")
    verb = input("Type a verb (example: dance, sleep): ")
    feeling2 = input("Type another feeling (example: scared, happy): ")
    animal = input("Type an animal: ")
    verb2 = input("Type another verb (example: swim, climb): ")
    color = input("Type a color: ")
    verb_ing = input("Type a verb ending in -ing (example: fishing, running): ")
    adverb = input("Type an adverb ending in -ly (example: slowly, loudly): ")
    number = input("Type a number: ")
    time_measure = input("Type a measure of time (example: hours, days): ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    number2 = input("Type another number: ")
    silly_word = input("Type a silly made-up word: ")
    noun2 = input("Type a food to roast (example: marshmallows, hot dogs): ")
 
    ending = random.choice(["Amazing!!"])
 
    print("\n--- YOUR STORY ---\n")
    print("This weekend I am going camping with " + name + ".")
    print("I packed my lantern, sleeping bag, and " + noun + ".")
    print("I am so " + feeling + " to " + verb + " in a tent.")
    print("I am " + feeling2 + " we might see a(n) " + animal + ", I hear they're kind of dangerous.")
    print("While we're camping, we are going to hike, fish, and " + verb2 + ".")
    print("I have heard that the " + color + " lake is great for " + verb_ing + ".")
    print("Then we will " + adverb + " hike through the forest for " + number + " " + time_measure + ".")
    print("If I see a " + color2 + " " + animal2 + " while hiking, I am going to bring it home as a pet!")
    print("At night we will tell " + number2 + " " + silly_word + " stories and roast " + noun2 + " around the campfire!!")
    print("\n" + ending)
 
 
#last template
 
elif choice == "3":
    print("\nGreat! Let's do the Enchanted Castle story.")
    print("I will ask you for some words, just type them and press enter.\n")
 
    name = input("Type a person's name: ")
    adjective = input("Type an adjective (example: dark, mysterious): ")
    color = input("Type a color: ")
    animal = input("Type an animal: ")
    place = input("Type a place (example: Paris, the mountains): ")
    adjective2 = input("Type another adjective: ")
    creature = input("Type a magical creature, plural (example: dragons, elves): ")
    adjective3 = input("Type one more adjective: ")
    creature2 = input("Type another magical creature, plural (example: fairies, trolls): ")
    room = input("Type a room in a house (example: kitchen, basement): ")
    noun = input("Type a noun (example: glitter, water): ")
    noun2 = input("Type another noun (example: cloud, stone): ")
    noun3 = input("Type a noun, plural (example: rose petals, feathers): ")
    adjective4 = input("Type another adjective: ")
    noun4 = input("Type a noun, plural (example: adventures, stars): ")
    number = input("Type a number: ")
    time_measure = input("Type a measure of time (example: years, centuries): ")
    verb_ing = input("Type a verb ending in -ing (example: flying, riding): ")
    adjective5 = input("Type one last adjective: ")
    noun5 = input("Type a noun (example: broomstick, carpet): ")
 
    ending = random.choice(["Until we meet again!"])
 
    print("\n--- YOUR STORY ---\n")
    print("Dear " + name + ",")
    print("I am writing to you from a " + adjective + " castle in an enchanted forest.")
    print("I found myself here one day after going for a ride on a " + color + " " + animal + " in " + place + ".")
    print("There are " + adjective2 + " " + creature + " and " + adjective3 + " " + creature2 + " here!")
    print("In the " + room + " there is a pool full of " + noun + ".")
    print("I fall asleep each night on a " + noun2 + " of " + noun3 + " and dream of " + adjective4 + " " + noun4 + ".")
    print("It feels as though I have lived here for " + number + " " + time_measure + ".")
    print("I hope one day you can visit, although the only way to get here now is " + verb_ing + " on a " + adjective5 + " " + noun5 + "!!")
    print("\n" + ending)
 
