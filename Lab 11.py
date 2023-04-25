#!/usr/bin/env python
# coding: utf-8

# In[1]:


#using the code provided for reference I updated gen_radiobuttons and added a delete_radiobuttons function to delete the previous answer choices from displaying
#i also added a submit_answer function to create a button that submits the answer and generates feedback with the eval_score function which also keeps track of points
# i also added the new_question function which has a button that generates a new question from the question list
import random
from tkinter import *
import requests

url = "https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy"
get_request = requests.get(url).json()

root = Tk()
root.title("Trivia")
root.geometry("1000x800")

#creating canvas
canvas = Canvas(root, width=800, height=500, bg="khaki1")
canvas.place(relx=.5, rely=.5,anchor= CENTER) #anchors the canvas in the center

#adding text to the canvas
game_display = canvas.create_text(200, 75, text="", fill="black", font=('Helvetica 15 bold'))

#creating the label that will display if something is correct/incorrect
feedback = Label(root, text="", pady=10, font=("arial", 15, "bold"))

user_answer = StringVar()
user_answer.set("")

score = 0

def generate_qlist(json):
    question_list = []
    for i in json:
        i = i["question"]
        question_list.append(i)
    return question_list

def gen_question(list_):
    choice = random.choice(list_)
    return choice

def generate_answers(json, question): 
    option_list = []
    for i in get_request:
        if i["question"] == question:
            cor = i["correctAnswer"]
            option_list.append(cor)
            for incor in i["incorrectAnswers"]:
                option_list.append(incor)
    random.shuffle(option_list)
    return option_list

def ask_question(question, answers):
    canvas.itemconfig(game_display, text=question, width=300)
    
def gen_radiobuttons(answers):
    y_pos = 150
    radio_buttons = []
    for i in answers:
        rad_btn = Radiobutton(canvas, text=i, variable=user_answer, value=i, font=('Helvetica 10 bold'))
        rad_btn.place(x=50, y=y_pos)
        radio_buttons.append(rad_btn)
        y_pos+=20
    return radio_buttons
    
        
def delete_radiobuttons():
    global radio_buttons
    for button in radio_buttons:
        button.destroy()
    radio_buttons=[]
        
def submit_answer():
    eval_score()
    delete_radiobuttons()
    global current_question
    q_list.remove(current_question)
    if len(q_list) > 0:
        current_question = gen_question(q_list)
        ans_list = generate_answers(get_request, current_question)
        ask_question(current_question, ans_list)
        gen_radiobuttons(ans_list)
    else:
        feedback["text"] = "You finished the quiz! You scored " + str(score) + " points."
        feedback.place(x=400, y=500)


def new_question():
    global current_question, radio_buttons

    # Delete previous radio buttons
    delete_radiobuttons()

    # Get new question and answers
    q_list = generate_qlist(get_request)
    current_question = gen_question(q_list)
    ans_list = generate_answers(get_request, current_question)

    # Update canvas with new question and answers
    ask_question(current_question, ans_list)
    radio_buttons = gen_radiobuttons(ans_list)




    
def eval_score():
    answer = user_answer.get()
    for i in get_request:
        if i["question"] == current_question:
            if i["correctAnswer"] == answer:
                feedback["text"] = "Correct!"
                feedback.place(x=400, y=500)
                global score
                score += 10
                score_label.config(text=f"Score: {score}")
            else:
                feedback["text"] = "Incorrect :("
                feedback.place(x=400, y=500)

def main(): 
    global score, score_label, radio_buttons, current_question, q_list
    
    # Set up score
    score = 0
    score_label = Label(root, text=f"Score: {score}", font=("arial", 15, "bold"))
    score_label.place(x=50, y=50)
    
    # Generate first question and answers
    q_list = generate_qlist(get_request)
    current_question = gen_question(q_list)
    ans_list = generate_answers(get_request, current_question)
    
    # Update canvas with question and answers
    ask_question(current_question, ans_list)
    radio_buttons = gen_radiobuttons(ans_list)
    
    # Add submit and new question buttons
    submit_button = Button(root, text="Submit Answer", font=("arial", 12, "bold"), command=eval_score)
    submit_button.place(x=500, y=400)
    new_question_button = Button(root, text="New Question", font=("arial", 12, "bold"), command=new_question)
    new_question_button.place(x=300, y=400)
    
    root.mainloop()

    
main()
root.mainloop()

