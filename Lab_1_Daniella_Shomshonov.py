#!/usr/bin/env python
# coding: utf-8

# In[120]:


#1. See the list below. Please write a program that will tell you what the longest word is in the list. Package your program inside of a function.  
list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
lengthlist = []
def longest_word(list):
    for word in list:
        count = 0
        for i in word:
            count+=1
        lengthlist.append(count)
    print("The longest word in the list is " + list[(lengthlist.index(max(lengthlist)))])
        
                
longest_word(list)


            


# In[121]:


#Now that you have built the program above, in a new cell, edit your program: import a .txt file of a list of words and have your program randomly choose 7 words from the file to add to a list, and then have the program determine the longest word as you did above.
import random
wordlist = "words.txt"

def longestword():
    list=[]
    lengthlist=[]
    filename = wordlist
    f = open(filename, "r", encoding="utf8")
    words=f.readlines()
    f.close
    count=1
    while (count<8):
        list.append(random.choice(words).strip())
        count+=1
    print("This is the list of words " + str(list))
    for word in list:
        count = 0
        for i in word:
            count+=1
        lengthlist.append(count)
    print("The longest word in the list is " + list[(lengthlist.index(max(lengthlist)))])

longestword()


# In[122]:


#Pretend that you're going to be leading a review session on dictionaries. Build a program that uses dictionaries and incorporates at least 4 built-in methods. [See full list on W3Schools](https://www.w3schools.com/python/python_ref_dictionary.asp)
capital_city = {"Thailand": "Bangkok", "Italy": "Rome", "England": "London", "Chile":"Santiago", "Bolivia": "Sucre"}

# prints list  of ditcionary keys(countries)
print(capital_city.keys())

#inserts a key "Canada" with value "Ottawa"
capital_city.update({"Canada": "Ottawa"})
print(capital_city)

#removes the last inserted key-value pair "Canada": "Ottawa"
capital_city.popitem()
print(capital_city)

#copies the dictionary
world_capitals = capital_city.copy()
print(world_capitals)


# In[126]:


#created a class that has english and italian attributes and assigned them to parameters
class flashcards:
    def __init__(self, english, italian):
        self.english = english
        self.italian = italian
        
    def __str__(self):    ## this instance method returns the english and italian parameters as a string which I thought would be a nice way to display the flashcards"
        return self.english + ' - ' + self.italian
    
flashcard=[]
user_continue = True
    
## Created a while loop that asks the user for what word they want and the translation. I decided to use a variable called user_continue as the condition for the loop, which turns false if the user says they do not want to continue
while(user_continue == True):
    english = input("What word would you like to make a flashcard of? ")
    italian = input("What is the Italian meaning of the word? ")
    flashcard.append(flashcards(english, italian))
    ask = input("Would you like to continue, Yes or No? ")
    if(ask != "Yes"):
        user_continue == False
        break

# this function would print the flashcards line by line
        
def see_flashcards():
    print("These are your flashcards: ")
    for i in flashcard:
        print(">", i)
        
# this function would allow the user to review the flashcards and test themselves on what they know. It iterates through the class items in flashcard and tests if the users input is the correct answer
def study_mode():
    i = 0
    while i != len(flashcard):
        answer = input("What is the italian word for " + flashcard[i].english + "? " )
        if answer == flashcard[i].italian:
            print("correct")
            i += 1
        else:
            try_again = input("Wrong, would you like to try again? ")
            if try_again == "Yes":
                continue
            else:
                i+=1
                  

study_mode()
see_flashcards()


# In[ ]:





# In[ ]:


#HANGMAN

import random

wordlist = "words.txt"
print ("Hello, welcome to hangman!")


def hangman():
    filename= wordlist
    f = open(filename, "r", encoding="utf8")
    words=f.readlines()
    f.close
    word = str(random.choice(words).strip())
    start=""
    next=[]
    for i in range(len(word)):
        start = start + "_ "
        next.append("_")
    print(start)
    guess = input("What is your first guess? ")
    letters = ([*word])
    play = True
    turns = 0
    while (play == True):
        turns +=1
        if turns > 15:
            print("Game over, too many turns. The word was: ")
            print(str(word))
            break
        if guess in letters:
            print("your letter is in the word")
            count=0
            for i in letters:
                if i == guess:
                    next[count]= str(guess)
                count+=1
            display = " ".join(next)
            print(display)
            if "_" not in display:
                print("good job")
                play= False
                break
            else:
                guess= input("What is your next guess?")

                
        else:
            print("nope")
            guess = input("Guess again ")
    
    

hangman()


    

