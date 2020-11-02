# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

word = input("Please enter a word or phrase: ")

i = 0

while i < 5:
    if word != 'quit':
        length_word = len(word)
        print(f"What you entered is {length_word} characters long")
        word = input("Please enter a word or phrase: ")
    else:
        break