import tkinter as tk
import random

class AppController:
    def __init__(self, view):
        self.view = view
        self.tips = ["Tip 1: Regularly review new words.", 
                     "Tip 2: Use words in sentences.", "Tip 3: Practice daily."]
        self.word_count = 4 # Sample word count
    
    def get_random_tip(self):
        return random.choice(self.tips)
    
    def get_word_count(self):
        return str(self.word_count)
    
    def start_test(self):
        test_window = tk.Toplevel(self.view.root)
        test_window.geometry("400x300")
        test_window.title("Start Test")
        tk.Label(test_window, text="Test Started!").pack()
    
    def manage_voca(self):
        voca_window = tk.Toplevel(self.view.root)
        voca_window.geometry("400x300")
        voca_window.title("Manage Vocabulary")
        tk.Label(voca_window, text="Manage your vocabulary here.").pack()
    
    def open_settings(self):
        setting_window = tk.Toplevel(self.view.root)
        setting_window.geometry("200x100")
        setting_window.title("Settings")
        tk.Label(setting_window, text="Settings").pack()
    
    def show_info(self):
        info_window = tk.Toplevel(self.view.root)
        info_window.geometry("200x100")
        info_window.title("Info")
        tk.Label(info_window, text="This is a vocab test application.").pack()
