#First create a list of the whole alphabet
#Pick a random word
#Prompt user to choose a letter. Success or fail
#If success, ask again until the word is spelled


import string
import random



#alphabet
alphabet = list(string.ascii_uppercase)

#number of tries
attempts = 10

#generate list
def create_list_words(file):
    f = open(file, "r" )
    word_list = []
    for line in f:
        for word in line.split():
            word_list.append(word)
    return word_list


#generate random word
def word_random(word_list):
    random_word = random.choice(word_list)
    return random_word


def check_letter(random_word):
    print("Choose a letter from the alphabet -->  " + str(random_word))
    letter_choice = input().lower()

    if letter_choice in random_word:
        return (True, letter_choice)
    else:
        return (False, letter_choice)

        # print "Nice job!"

#underscore_string = "---------------"
#play the game




def replace_underscores(random_word):
    underscore_string = []
    for letter in range(len(random_word)):
        underscore_string += "_"
    return (underscore_string)

def create_dict(random_word):
    word_dict = {}
    for index in range(len(random_word)):
        if random_word[index] in word_dict:
            word_dict[random_word[index]].append(index)
        else:
            word_dict[random_word[index]] = [index]
    return word_dict


def play_game(random_word):
    underscore_string = replace_underscores(random_word)
    #cast as list for removal
    random_word = list(random_word)
    deep_copy_random_word = random_word[:]
    word_dict = create_dict(random_word)
    # print (word_dict)

    print("Welcome to Hangman. You have " + str(attempts) + " attempts")

    attempts_count = 0

    while attempts_count < attempts:
        choice_status = check_letter(random_word)
        # print("status" + underscore_string)
        #want to check if the length of the random word is 0
        if choice_status[0]: #either true or false
            print("Nice job!")

            #deep Copy
            # index_letter = deep_copy_random_word.index(choice_status[1])
            # index_letter = original_length - len(random_word) + random_word.index(choice_status[1])
            # print ("the index is: " + str(index_letter))
            # print (deep_copy_random_word)
            #random word
            random_word.remove(choice_status[1])#remove the letter chosen when it is correct
            #show the status in the underscore
            index_letter = word_dict[choice_status[1]][0]
            word_dict[choice_status[1]].remove(index_letter)
            underscore_string[index_letter] = choice_status[1]
            print (underscore_string)
            print("the word is now: " + str(random_word))
            if len(random_word) == 0:
                print("You have won")
                return
        else:
            print("Sorry, try again.")
            attempts_count += 1
            print("You have %s attemps left" %(attempts - attempts_count))

    print("You have no more attempts. You lose.")

word_list = create_list_words('words.txt')
random_word = word_random(word_list)
play_game(random_word)
# word_dict = create_dict("wwordw")
# print (word_dict)

# replace_underscores("word")
