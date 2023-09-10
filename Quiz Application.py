#Quiz App

import tkinter as tk 
from tkinter import messagebox

class quizapp:
    def __init__(self): 
        self.quiz_ques = [
        { 
        'Questions' : 'when did chandrayan 3 Launched ? ' ,
        'Options' : ['14 th July','14 th August','14 th May',' 14 th March '],
        'Correct_answer' : 0 
        } ,
        { 
        'Questions' : 'what is the capital of AndhraPradesh ? ' ,
        'Options' : ['Amaravathi','Kurnool','Vijayawada','Kadapa'],
        'Correct_answer' : 0 
        } ,
        {
         'Questions' : 'who is the current Chair Person of Tata Groups ? ' ,
        'Options' : ['Natarajan Chandrasekaran','Shivan Chadrasekaran','Narendra Modi','Y.S Jagan'],
        'Correct_answer' : 0
        }
        ]
        self.current_question_index = 0
        self.score = 0
        
        self.window = tk.Tk()
        self.window.title('Quiz App')
        
        self.question_label = tk.Label(self.window , text ='')
        self.question_label.pack()
        
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame , text = ' ',width= 30 , command =lambda i=i : self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)
            
        self.next_question_button = tk.Button(self.window , text = 'Next Question' , width =30 , command = self.next_question)
        self.next_question_button.pack(pady=10)
            

    def check_answer (self,selected_option):
         question_data= self.quiz_ques[self.current_question_index]
         answer = question_data['Correct_answer']
         if selected_option == answer:
             self.score= self.score + 1
             messagebox.showinfo('Correct','Your answer is correct')
         else :
             messagebox.showinfo('Incorrect','Your answer is wrong')
             
         
    def load_question(self):
        question_data= self.quiz_ques[self.current_question_index]
        self.question_label.config(text=question_data['Questions'])
        options = question_data['Options']
        for i in range(4):
            self.option_buttons[i].config(text = options[i])
    
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_ques):
            messagebox.showinfo('Quiz Over','Your Score Is '+str(self.score))
            self.window.quit()
        else :
            self.load_question()
    
      
    def start_quiz(self):
            self.load_question()
            self.window.mainloop()
            
quiz_app=quizapp()
quiz_app.start_quiz()