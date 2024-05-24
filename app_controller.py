import random
import tkinter as tk
from test_controller import TestController
from voca_controller import VocaController

class AppController:
    def __init__(self, view):
        self.view = view
        self.test_controller = TestController(view)
        self.voca_controller = VocaController(view)
        self.tips = ["Tip 1: Regularly review new words.", "Tip 2: Use words in sentences.", "Tip 3: Practice daily."]
        self.word_count = 4 # Sample word count
    
    def get_random_tip(self):
        return random.choice(self.tips)
    
    def get_word_count(self):
        return str(self.word_count)
    
    def start_test(self):
        self.test_controller.start_test()
    
    def manage_voca(self):
        self.voca_controller.manage_voca()
    
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
