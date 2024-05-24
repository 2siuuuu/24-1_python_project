from tkinter import *
from tkinter import messagebox

mainscreen = Tk()

#---------------------------------------------------------

def window_setup():
    mainscreen.title("윈도우 창 연습")
    mainscreen.geometry("800x400") 
    mainscreen.resizable(width = FALSE, height = FALSE)

def reveal_messagebox():
    messagebox.showinfo("왜 눌러", "나가라")

#---------------------------------------------------------

TEST_Button = Button(mainscreen, text="TEST!", command= reveal_messagebox)
TEST_Button.pack()

window_setup()



mainscreen.mainloop()
#develop에 추가