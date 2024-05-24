import tkinter as tk

class VocaController:
    def __init__(self, view):
        self.view = view
    
    def manage_voca(self):
        voca_window = tk.Toplevel(self.view.root)
        voca_window.geometry("400x300")
        voca_window.title("Manage Vocabulary")
        tk.Label(voca_window, text="Manage your vocabulary here.").pack()
