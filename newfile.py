import tkinter as tk
from tkinter import messagebox
import random

btnState=False
k=0
class Quiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#FFF6E7")
        self.root.geometry("400x800")
        self.questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Mercury", "Jupiter"], "answer": "Mars"},
        {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"], "answer": "Blue Whale"},
        {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"], "answer": "Leonardo da Vinci"},
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": "H2O"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], "answer": "William Shakespeare"},
        {"question": "What is the tallest mountain in the world?", "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "answer": "Mount Everest"},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["Japan", "China", "South Korea", "Thailand"], "answer": "Japan"},
        {"question": "What is the primary ingredient in guacamole?", "options": ["Avocado", "Tomato", "Onion", "Lime"], "answer": "Avocado"},
        {"question": "Who discovered penicillin?", "options": ["Marie Curie","Alexander Fleming", "Albert Einstein", "Isaac Newton"], "answer": "Alexander Fleming"}
        ]
        self.current_question_index = 0
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        self.lab1 = tk.Frame(self.root, bg="#52FF7D")
        self.lab1.pack(fill=tk.X,  pady=(0,50))
        
        self.quiz_label = tk.Frame(self.lab1, height="40", bg="#52FF7D")
        self.quiz_label.pack()
       
        
        
        self.navbarBtn = tk.Button(self.lab1, text="☰", font=("Arial", 17),bg="#52ff7d", activebackground="orange", command=self.switch)
        self.navbarBtn.place(x=0, y=0)
        
        self.questions_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength="500",bg="#fff6e7")
        self.questions_label.pack(pady=(0,40)) 
        
        # setting Navbar frame:
        self.navRoot = tk.Frame(self.root, bg="gray17", height=10000, width=300)
       
        self.lab2=tk.Frame(self.navRoot, bg="orange", height="40", width="300")
        self.navRoot.place(x=-300, y=0)
        
        
        self.navFrame = tk.Frame(self.navRoot, bg="gray17", height=10000, width=300)
        
         
        self.res1 = tk.Button(self.navRoot, text="Restart",fg="white" , relief=tk.FLAT, height="2",bd=0, font=("Arial", 12),width=27, bg="gray17",highlightbackground="gray17", command=self.restart_quiz)
        self.lab2.pack()
        
        self.closeBtn = tk.Button(self.navRoot, text="☰", font=("Arial", 17), bg="orange", bd=0, activebackground="orange", command=self.switch)
        self.closeBtn.place(x=0,y=0)
        self.res1.pack() 
        self.navFrame.pack()
         
        self.display_question()  # Display the first question
        
        
    def restart_quiz(self):
    	response = messagebox.askyesno("Restart Quiz", "Restart the quiz?")
    	if response:
        	self.goback()  # Restart the quiz
        
    def goback(self):	 
   	 self.clear_options()  # Clear all the widgets 
   	 self.current_question_index = 0  # Reset the question index
   	 self.score = 0  # Reset the score
   	 self.switch()
   	 self.display_question()  # Redisplay the first question

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            question_text = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["answer"]
            self.questions_label.config(text=question_text)
            # Display option buttons
            for i, option in enumerate(options):
                option_button = tk.Button(self.root, text=option, font=("Arial", 10), bg="#FFC298", width=20)
                option_button.config(command=lambda ans=option: self.check_answer(ans, correct_answer))
                option_button.pack(pady=30)
            
        else:
            self.questions_label.config(text=f"Quiz Completed.\nYour score: {self.score}")
            self.back=tk.Button(text="Play again", command=self.goback)
            self.back.pack (pady=50)
           
        self.navRoot.lift()

    def check_answer(self, selected_answer, correct_answer):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                if widget.cget("text") == selected_answer:
                    if selected_answer == correct_answer:
                	    widget.config(bg="#7FFF7F")  # Green for correct answer
                    else:
                	    widget.config(bg="#FF7F7F")  # Red for wrong answer
                elif  widget.cget("text") == correct_answer:
                     widget.config(bg="#7FFF7F")
                widget.config(state="disabled")
        if selected_answer == correct_answer:
            self.score += 1
        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 10), bg="yellow", command=self.next_question)
        self.next_button.pack(pady=(40,40))
        

    def clear_options(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        
                
                
    def next_question(self):
    	self.current_question_index += 1
    	self.clear_options()
    	self.display_question()

    # setting switch function:
    def switch(self):
        global btnState
        self.navRoot.lift()
       
        if btnState is True:
        	btnState = False
        	for i in range(0, 301, 5):
        	   	self.navRoot.place(x=-i, y=0)
        	   	self.lab1.update()
        else:
            for i in range(-300, 0, 5):
            	self.navRoot.place(x=i, y=0)
            	self.lab1.update()

            # turing button ON:
            btnState = True

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run()

