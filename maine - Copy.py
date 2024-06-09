import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import sqlite3
import requests
import random
import html

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")
        self.root.title("Modern Login UI using Customtkinter")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self.root, text="General Quiz", font=("Helvetica", 18))
        self.label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text='User login')
        self.label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username", border_width=1)
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", border_width=1)
        self.user_pass.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.frame, text='Login', command=self.login)
        self.button.pack(pady=12, padx=10)

        self.checkbox = ctk.CTkCheckBox(master=self.frame, text='Remember Me', checkbox_height=15, checkbox_width=15, border_width=1)
        self.checkbox.pack(pady=12, padx=10)

    def login(self):
        username = ""
        password = ""

        if self.user_entry.get() == username and self.user_pass.get() == password:
            self.confirm_action(0)
        else:
            self.confirm_action(1)

    def confirm_action(self, k):
        if k == 0:
            confirm_window = ctk.CTkToplevel()
            confirm_window.geometry("300x100")
            confirm_window.title("Successful")
            confirm_window.lift()
            confirm_window.attributes('-topmost', True)

            label = ctk.CTkLabel(confirm_window, text="Login successful, press ok to continue")
            label.pack(pady=10)

            def ok_button_click():
                print("User confirmed the action")
                confirm_window.destroy()
                self.open_dashboard()

            ok_button = ctk.CTkButton(confirm_window, text="ok", command=ok_button_click)
            ok_button.pack(padx=20, pady=10)
            confirm_window.mainloop()

        else:
            error_window = ctk.CTkToplevel()
            error_window.geometry("300x100")
            error_window.title("Error")
            error_window.lift()
            error_window.attributes('-topmost', True)

            label = ctk.CTkLabel(error_window, text="Wrong username or password")
            label.pack(pady=10)

            def button_click():
                print("User confirmed the action")
                error_window.destroy()

            tg_button = ctk.CTkButton(error_window, text="Try Again", command=button_click)
            tg_button.pack(padx=20, pady=10)

    def clear_options(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def open_dashboard(self):
        self.clear_options()
        DashPage(self.root)
            
            

class DashPage:
    def __init__(self, root):
        self.root = root
        self.btnState = False
        self.btnStateprof = False
        self.clr = 0
        self.wdth = 400

        self.root.geometry("400x600")
        self.root.title("Dash")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("light")
        
        self.createwidgets()
        
    def createwidgets(self):    

        self.frame = ctk.CTkFrame(self.root, height=45, fg_color="transparent", border_width=1, corner_radius=0)
        self.frame.pack(side="top", fill="x") #top label/bar

        self.nav_frame = ctk.CTkFrame(master=self.root, width=300, height=1000)
        self.nav_frame.place(x=-300, y=0) #collapsible sidebar

        self.immage = ctk.CTkImage(Image.open("menu2.png"), size=(26, 26)) #collapsible sidebar image
        self.button1 = ctk.CTkButton(self.frame, image=self.immage, fg_color="transparent", width=20, height=20, text=None, hover_color="#999999", command=self.switchsidebar)
        self.button1.pack(side="left", padx=5, pady=5) #collapsible sidebar button

        self.image2 = ctk.CTkImage(Image.open("light.png"), size=(24, 24))
        self.theme = ctk.CTkButton(self.frame, image=self.image2, fg_color="transparent", width=22, height=22, text=None, hover_color="#999999", command=self.chtheme)
        self.theme.pack(side="right", pady=5, padx=5) #theme change button

        self.nav_framebar = ctk.CTkFrame(self.nav_frame, height=40, fg_color="#7777db")
        self.nav_framebar.pack(side="top", fill="x") #top bar of collapsible side bar

        self.button2 = ctk.CTkButton(self.nav_framebar, image=self.immage, fg_color="transparent", width=20, text=None, command=self.switchsidebar)
        self.button2.pack(side="left", padx=5, pady=5) #close btn of collapsible side bar

        self.nav_frameframe = ctk.CTkFrame(self.nav_frame, height=1000, fg_color="gray17")
        self.nav_frameframe.pack() #remaining window of sidebar
        
        self.dashboard = ctk.CTkLabel(master=self.frame, text="Dashboard", font=("Serif", 17, 'bold'))
        self.dashboard.pack(pady=10)        #dashboard text 

        self.welcome = ctk.CTkLabel(master=self.root, text="Welcome, User!", font=("Serif", 17))
        self.welcome.pack(pady=20) #welcome text

        self.mainframe = ctk.CTkFrame(master=self.root)
        self.mainframe.pack(pady=15, padx=40, fill='both', expand=True) #window for dahboard buttons

        self.mydash = ctk.CTkFrame(master=self.mainframe, fg_color="transparent")
        self.mydash.pack(side="top", pady=5, fill="x") #text holder for "My Dashboard"
        self.mydashtxt = ctk.CTkLabel(master=self.mydash, text="My Dashboard", font=("Serif", 17))
        self.mydashtxt.pack(side="left", pady=5, padx=30) #"My Dashboard" text

        self.startquiz = ctk.CTkButton(self.mainframe, text="Start Quiz", font=("Serif", 17), text_color="black", fg_color="#fff200", border_width=1, height=75, width=250, command=self.open_quizpage)
        self.startquiz.pack(padx=30)
        self.viewscore = ctk.CTkButton(self.mainframe, text="View Scores", font=("Serif", 17), text_color="black", fg_color="#ff99cc", border_width=1, height=75, width=250, command=self.switchprofbar)
        self.viewscore.pack(pady=10, padx=30)

        self.prof_frame = ctk.CTkFrame(master=self.root, height=1000, width=400)
        self.prof_frame.place(x=-400, y=0)
        self.prof_frame.winfo_visual()

        self.topframe = ctk.CTkFrame(master=self.prof_frame, height=150, width=400, fg_color="#ffa64d", corner_radius=20)
        self.topframe.place(x=0, y=-20)

        self.toplbl = ctk.CTkLabel(self.topframe, height=45, text="Profile", text_color="Black", width=400, font=("Serif", 17, 'bold'))
        self.toplbl.place(x=0, y=20)

        self.backbtn = ctk.CTkButton(master=self.topframe, text="<", font=("Serif", 17), width=20, fg_color="transparent", text_color="black", hover_color="#ffa64d", command=self.switchprofbar)
        self.backbtn.place(x=5, y=25)

        self.picholder = ctk.CTkFrame(master=self.prof_frame, height=90, width=360, corner_radius=10, background_corner_colors=["#ffa64d", "#ffa64d", None, None], border_color="white", border_width=1)
        self.picholder.place(x=20, y=105)

        self.imgprof = ctk.CTkImage(Image.open("prof.png"), size=(60, 60))
        self.pic = ctk.CTkLabel(master=self.picholder, image=self.imgprof, height=50, width=50, fg_color="transparent", text=None)
        self.pic.place(x=15, y=15)

        self.username = ctk.CTkLabel(master=self.picholder, text="Username", font=("Serif", 17))
        self.username.place(x=100, y=20)

        self.options = ctk.CTkLabel(master=self.prof_frame, text="Sample text: ", font=("Serif", 17), fg_color="transparent")
        self.options.place(x=25, y=220)

        self.mainpframe = ctk.CTkFrame(master=self.prof_frame, width=360, height=1000, border_color="white", border_width=1)
        self.mainpframe.place(x=20, y=250)

    def switchsidebar(self):
        self.nav_frame.lift()

        if self.btnState is True:
            self.btnState = False
            for i in range(0, 401, 2):
                self.nav_frame.place(x=-i, y=0)
                self.root.update()
        else:
            for i in range(-400, 0):
                self.nav_frame.place(x=i, y=0)
                self.root.update()
            self.btnState = True

    def chtheme(self):
        if self.clr == 1:
            ctk.set_appearance_mode("dark")
            self.clr = 0
            self.image2 = ctk.CTkImage(Image.open("dark.png"), size=(24, 24))
            self.theme.configure(image=self.image2)
            self.theme._draw()
        else:
            ctk.set_appearance_mode("light")
            self.clr = 1
            self.image2 = ctk.CTkImage(Image.open("light.png"), size=(24, 24))
            self.theme.configure(image=self.image2)
            self.theme._draw()

    def switchprofbar(self):
        self.prof_frame.lift()

        if self.btnStateprof is True:
            self.btnStateprof = False
            for i in range(10, self.wdth + 1, 10):
                self.prof_frame.place(x=-i, y=0)
                self.root.update()
        else:
            for i in range(-self.wdth, 10, 10):
                self.prof_frame.place(x=i, y=0)
                self.root.update()
            self.btnStateprof = True
            
            
    def clear_options(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def open_quizpage(self):
        self.clear_options()
        Quizwindow(self.root)


class Quizwindow:
    def __init__(self, root):
        self.root=root
        self.btnState=False
        self.current_question=0
        self.questions = []
        self.score = 0
        self.clr = 1 #for theme
        
        self.create_widgets()
   	
 
    def create_widgets(self):
        self.frame = ctk.CTkFrame(self.root, height=45, fg_color="transparent", border_width=1, corner_radius=0)
        self.frame.pack(side="top", fill="x") #top label/bar

        self.nav_frame = ctk.CTkFrame(master=self.root, width=300, height=1000)
        self.nav_frame.place(x=-300, y=0) #collapsible sidebar

        self.immage = ctk.CTkImage(Image.open("menu2.png"), size=(26, 26)) #collapsible sidebar image
        self.button1 = ctk.CTkButton(self.frame, image=self.immage, fg_color="transparent", width=20, height=20, text=None, hover_color="#999999", command=self.switchsidebar)
        self.button1.pack(side="left", padx=5, pady=5) #collapsible sidebar button

        self.image2 = ctk.CTkImage(Image.open("light.png"), size=(24, 24))
        self.theme = ctk.CTkButton(self.frame, image=self.image2, fg_color="transparent", width=22, height=22, text=None, hover_color="#999999", command=self.chtheme)
        self.theme.pack(side="right", pady=5, padx=5) #theme change button

        self.nav_framebar = ctk.CTkFrame(self.nav_frame, height=40, fg_color="#7777db")
        self.nav_framebar.pack(side="top", fill="x") #top bar of collapsible side bar

        self.button2 = ctk.CTkButton(self.nav_framebar, image=self.immage, fg_color="transparent", width=20, text=None, command=self.switchsidebar)
        self.button2.pack(side="left", padx=5, pady=5) #close btn of collapsible side bar

        self.nav_frameframe = ctk.CTkFrame(self.nav_frame, height=1000, fg_color="gray17")
        self.nav_frameframe.pack() #remaining window of sidebar
        
        self.quizpg = ctk.CTkLabel(master=self.frame, text="Quiz", font=("Serif", 17, 'bold'))
        self.quizpg.pack(pady=10) #"Quiz" text on top label 
        
        self.questions_label = ctk.CTkLabel(master=self.root, text="", font=("Helvetica", 17), wraplength=300)
        self.questions_label.pack(pady=30)
        
        self.get_questions()
        
    def get_questions(self, amount=10, category=31, difficulty='easy'):
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
        response = requests.get(url)
        data = response.json()
        self.questions = data['results'] #stores the list
        self.display_question()
        
    def display_question(self):
        question = self.questions[self.current_question] #selects first element of list=dictionary
        self.questions_label.configure(text=html.unescape(question['question']))
        
        options = question['incorrect_answers'] + [question['correct_answer']]
        options = [html.unescape(option) for option in options]
        random.shuffle(options)
        correct_answer = question["correct_answer"]
        
        
        for i in range(0,len(options)):
            option_button = ctk.CTkButton(master=self.root, text=options[i], font=("Arial", 17), width=300, height=45)
            option_button.configure(command=lambda ans=options[i]: self.check_answer(ans, correct_answer))
            option_button.pack(pady=10)
                
    def check_answer(self, selected_answer, correct_answer):
        for widget in self.root.winfo_children():
            if isinstance(widget, ctk.CTkButton) and widget.winfo_y() > 120:
                if widget.cget("text") == selected_answer:
                    if selected_answer == correct_answer:
                	    widget.configure(fg_color="#7FFF7F")  # Green for correct ans
                    else:
                	    widget.configure(fg_color="#FF7F7F")  # Red for wrong answer
                elif  widget.cget("text") == correct_answer:
                     widget.configure(fg_color="#7FFF7F")
                widget.configure(state="disabled")
        if selected_answer == correct_answer:
            self.score += 1
        self.next_button = ctk.CTkButton(self.root, text="Next", font=("Arial", 10), fg_color="yellow", text_color="black", command=self.next_question)
        self.next_button.pack(pady=(40,40))

    def next_question(self):
        self.current_question += 1
        self.clearoptions()
        self.display_question()
        

    def clearoptions(self):
        for widget in self.root.winfo_children():
            if (isinstance(widget, ctk.CTkButton) or isinstance(widget, tk.Button)) and widget.winfo_y() > 120:
                widget.destroy()

        
    def switchsidebar(self):
        self.nav_frame.lift()

        if self.btnState is True:
            self.btnState = False
            for i in range(0, 401, 2):
                self.nav_frame.place(x=-i, y=0)
                self.root.update()
        else:
            for i in range(-400, 0):
                self.nav_frame.place(x=i, y=0)
                self.root.update()
            self.btnState = True
            
    def chtheme(self):
        if self.clr == 1:
            ctk.set_appearance_mode("dark")
            self.clr = 0
            self.image2 = ctk.CTkImage(Image.open("dark.png"), size=(24, 24))
            self.theme.configure(image=self.image2)
            self.theme._draw()
        else:
            ctk.set_appearance_mode("light")
            self.clr = 1
            self.image2 = ctk.CTkImage(Image.open("light.png"), size=(24, 24))
            self.theme.configure(image=self.image2)
            self.theme._draw()
            
        
        
     



















if __name__ == "__main__":
    app = ctk.CTk()
    LoginPage(app)
    app.mainloop()

