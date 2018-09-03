# -*- coding: utf-8 -*-
"""
@author: kpandey
"""

import random

#s=read_words('cs_words.txt')
ALPHABET='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def read_words(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            splitLine = line.split('%')
            print(splitLine)
            result.append(splitLine)
            #newDict[splitLine[0]] = ",".join(splitLine[1:])
    return(result)


def set_to_string(sets):
    """
    This function takes a set as a parameter and returns the set as a string
    with the values in the set seperated by a space and capitalized.
    """
    result = '' #start with empty string
    for element in sets:
        result+=element + ' ' #adds spaces between results
    return result.upper() #makes result upper cased


def create_underlined_word(answer):
    """
    This function takes a parameter of a word and returns the word but without
    any letters which are instead placed with underlines. the number of 
    letters in the word dictate how many underlines will occur.
    """
    result='' #start with empty
    under_score= '_' #what each letter will become
    for letter in answer: #loops through answer
        result+=under_score #turns it into underline
    return result
    
    
def insert_letter(letter, word, guess_word):
    """
    This function takes a letter, a word, and the guess_word as a parameter
    and returns the new word with the letter being displayed in that word
    where a underscore was in the same index as in the guess_word. The returned
    value is a set containing those values.
    """
    new_word=list(word) #makes the word a list
    new_guess_word=list(guess_word) #makes the guess_word a list
    for i in range(len(new_guess_word)): 
        if letter==guess_word[i]: #if letter is in the correct word
            new_word.pop(i) #the new word gets that letter instead of _
            new_word.insert(i,letter) #actually changes _ to letter given
        else:
            new_word #nothing happens and continues in loop
    #answer=set_to_string(new_word)
    return new_word #returns list of new_word


def insert_letter_to_string(letter, word, guess_word):
    """
    This function is identical to the one above but instead returns a string
    of the new_word instead of a list. We implimented the above function in 
    our hangman function, but this function also works, and the output is 
    cleaner on its own.
    """
    new_word=list(word) #makes the word a list
    new_guess_word=list(guess_word) #makes the guess_word a list
    for i in range(len(new_guess_word)): 
        if letter==guess_word[i]: #if letter is in the correct word
            new_word.pop(i) #the new word gets that letter instead of _
            new_word.insert(i,letter) #actually changes _ to letter given
        else:
            new_word #nothing happens and continues in loop
    answer=set_to_string(new_word) #creates the string instead of list
    return answer #returns a string of new_word
    

def english_letter(guess):
    """
    This function takes a parameter of a letter and lets the user know if this 
    word is in the english alphabet. It utilizes a variable denoting alphabet
    which has all the letters in the alphabet both upper and lowercase.
    """
    if guess not in ALPHABET: #only prints if not in alphabet.
        print('This word is not in the English alphabet. Try Again.')
        

def bad_hangman(guesses_left, total):
    """
    this function takes two parameters and returns a picture representing
    how many guesses you have left in your hangman function. It only allows
    7 outputs and will show the entire picture once you have no guesses left.
    """
    if guesses_left == total:
        print('|------|')
    if guesses_left == total-1:
        print('|------|')
        print('|      O')
    if guesses_left == total-2:
        print('|------|')
        print('|      O')
        print('|    \ | /')
    if guesses_left == total-3:
        print('|------|')
        print('|      O')
        print('|    \ | /')
        print('|     \|/')
    if guesses_left == total-4:
        print('|------|')
        print('|      O')
        print('|    \ | /')
        print('|     \|/')
        print('|      |')
    if guesses_left == total-5:
        print('|------|')
        print('|      O')
        print('|    \ | /')
        print('|     \|/')
        print('|      |')
        print('|' + '     ' + '/' + str(' \\'))
    if guesses_left == total-6:
        print('|------|')
        print('|      O')
        print('|    \ | /')
        print('|     \|/')
        print('|      |')
        print('|' + '     ' + '/' + str(' \\'))
        print('|' + '    ' + '/' + str('   \\'))
    if guesses_left == total-7:
        print('|------|')
        print('|      O')
        print('|    \ | /')
        print('|     \|/')
        print('|      |')
        print('|' + '     ' + '/' + str(' \\'))
        print('|' + '    ' + '/' + str('   \\'))
        print('|____________')
        

def play_hangman(filename, total_guesses):
    """
    This function designs the game of hangman using python. It imports a random
    word from the cswords.txt and converts it into a list. It also, creates an 
    empty list of blank spaces that indicates the number of letters in the 
    correct word. Hence, this function works with list. If the letter is 
    guessed correctlyit adds the letter to the empty_word. Otherwise, it just 
    adds the guessed letter into the set of guessed letters and consequently 
    the game is over when the user has made 7 incorrect guesses. Otherwise, 
    the program congratulates the user for being able to guess the word. If the
    game is over, the program asks the user if they want to play again.
    """
    lists=read_words(filename) #creats a list form the file (using other fct)
    random_Q_A = random.choice(lists)
    question = random_Q_A[0]
    guess_word= random_Q_A[1]
    print(question)
    guessed_letters=set()               
    #Creates an empty set of the guessed letters so they can be added later 
    #and the order of the letters don't matter
    
    empty_word=create_underlined_word(guess_word)
    #creates new empty word with empty blanks to be filled with correct letters
    total_guesses=7
    #This defines the no of guesses allowed to the user to be 7
    print("number of guesses is "+str(total_guesses))
    count=0
    print("-"*17)
    print("Guessed letters:"+ set_to_string(guessed_letters))
    strings="*"*total_guesses
    print("Incorrect guesses left: "+ strings)
    while empty_word!= guess_word.lower():
        letter=input("Guess a letter:")
        print("-"*17)
        if letter.lower() in guessed_letters: #checks if letter already guessed
            print("You guessed this letter already. Try again!")
            letter=input("Guess a letter:")
            print(set_to_string(empty_word))           
        guessed_letters.add(letter)#Adds new letter to set of guessed letters
        print("Guessed letters:"+ set_to_string(guessed_letters))
        strings="*"*total_guesses
        print("Incorrect guesses left: "+ strings)
        if letter.lower() in guess_word:
            empty_word=insert_letter(letter, empty_word,guess_word)
            #inserts the correct guessed letter in the word with the blanks
            set_to_string(empty_word)
            print(set_to_string(empty_word))
        else:
            print(set_to_string(empty_word))           
            count+=1
            total_guesses=total_guesses-1
    #This decreases the total no of guesses every time a wrong guess is made
            if count>=7: #i.e. if count equals to the number of guesses allowed
                print('-'*18)
                print("GUESSED LETTERS:" + set_to_string(guessed_letters))            
                print("The word was: "+ guess_word)#This prints the correct word
                print("Better Luck next time!")
                print("sorry, no more guesses.")
                break #This breaks the loop
        
    if total_guesses>0:#This means the person was able to guess the word     
        print("Congratulations, you only made "+str(total_guesses)+ \
        " mistakes in finding the correct word.")
    elif total_guesses==0:
        play_again=input("DO you want to play again?")
        #This makes it interactive by asking the user if they want to try again
        if play_again.lower()=="yes":
            play_hangman(filename, total_guesses)

play_hangman('testdic.txt', 7)