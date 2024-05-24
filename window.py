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

def chk_func():
    if chk.get() == 0:
        messagebox.showinfo("", "아 저리가")
    else :
        messagebox.showinfo("", "아 다시 와봐")

#---------------------------------------------------------

TEST_Button = Button(mainscreen, text="TEST!", command= reveal_messagebox)
TEST_Button.pack()

chk =IntVar()
cb1 = Checkbutton(mainscreen, text="누르지마", variable=chk, command=)

window_setup()



mainscreen.mainloop()
#develop에 추가