# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
# Prompts the user for a word
s1 = input("Please enter a word: ")

# Prompts the user for how many times they'd like that word repeated
s2 = int(input("How many times would you like to repeat that word? "))

# Print the word repeated the specified number of times
result = s1 * s2
print(result)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
# Prompt the user for their name
s1 = input("Please enter your name: ")

# Prompt the user for their age
s2 = int(input("Please enter your age: "))

# Calculate the age next year
age_next_year = s2 + 1

# Print the greeting message using string concatenation
message = "Hello, " + s1 + "! You are " + str(s2) + " years old. Next year, you will be " + str(age_next_year) + " years old."
print(message)

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
# Prompt the user for a sentence
s1 = input("Please enter a sentence: ")

# Prompt the user for a word to find in that sentence
s2 = input("Please enter a word to find in the sentence: ")

# Check if the word is in the sentence
word_found = s2 in s1

# Print whether the word was found in the sentence
print(word_found)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
# Prompt the user for a word
s1 = input("Please enter a word: ")

# Prompt the user for a first index and convert it to an integer
first_index = int(input("Please enter the first index: "))

# Prompt the user for a last index and convert it to an integer
last_index = int(input("Please enter the last index: "))

# Slice the word at the indexes provided by the user
sliced_word = s1[first_index:last_index]

# Print the sliced word to the screen
print("Sliced word:", sliced_word)

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
# Define the words
s1 = "apple"
s2 = "banana"
s3 = "cherry"

# Print the words with a pipe character in between
print(s1, s2, s3, sep=' | ')
