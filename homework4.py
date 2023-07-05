# Write a Python program that takes a string as input and counts the frequency of each word in the string. The program should store the word frequencies in a dictionary and display the result.
# Here are the steps to follow:
# Prompt the user to enter a sentence or a paragraph.
# Remove any punctuation marks from the input string (e.g., commas, periods, exclamation marks).
# Convert the string to lowercase to make the word frequency case-insensitive.
# Split the string into a list of words using the split() method.
# Create an empty dictionary to store the word frequencies.
# Iterate over the list of words and update the dictionary with the frequency of each word. If a word is already in the dictionary, increment its count by 1. If it’s not in the dictionary, add it as a new key with a value of 1.
# Display the word frequencies in alphabetical order, along with their corresponding counts.




import string
sentence = input("Enter a sentence or paragraph: ")
sentence = sentence.translate(str.maketrans("","",string.punctuation))
sentence = sentence.lower()
words = sentence.split()
word_frequencies = {}
for word in words:
	if word in word_frequencies:
		word_frequencies[word] += 1
	else:
		word_frequencies[word] = 1
sorted_words = sorted(word_frequencies.keys())
for word in sorted_words:
	print(f"{word}: {word_frequencies[word]}")





# Create a phone book program that allows users to store and retrieve contact information. The program should use dictionaries and lists to store the data.
# Implement a menu-based system that provides the following options:
# Add a new contact: Prompt the user to enter a name and phone number, and add them to the phone book dictionary as a key-value pair.
# Search for a contact: Prompt the user to enter a name, and display the corresponding phone number from the phone book dictionary.
# List all contacts: Display all the contacts in the phone book, showing both the names and phone numbers.
# Exit the program: Terminate the program.
# Continuously prompt the user for their choice until they choose to exit the program.





def print_menu():
    print('1. Add a new contact')
    print('2. Search for a contact')
    print('3. List all contacts')
    print('4. Exit')
    print()
phone_book = {}

while True:
    print_menu()
    menu_choice = int(input("Enter your choice (1-4):"))


    if menu_choice == 1:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        phone_book[name] = phone
        print("Contact added successfully.\n")
    elif menu_choice == 2:
    	name = input("Enter the name to search: ")
    	if name in phone_book:
    		print("Phone number:",phone_book[name])
    	else:
    		print("Contact not found.\n")
    elif menu_choice == 3:
        if not phone_book:
        	print("Phone book is empty.\n")
        else:
        	print("Contacts:")
        	for name,number in phone_book.items():
        		print(name,":",number)
        	print()
    elif menu_choice == 4:
        print("Exit program")
        break
    else:
    	print("Please try again.\n")