import tkinter as tk

class TestController:
    def __init__(self, view):
        self.view = view
    
    def start_test(self):
        test_window = tk.Toplevel(self.view.root)
        test_window.geometry("400x300")
        test_window.title("Start Test")
        tk.Label(test_window, text="Test Started!").pack()
