import tkinter as tk
from tkinter import messagebox
import random

# Sample tips for demonstration
tips = ["Tip 1: Regularly review new words.", "Tip 2: Use words in sentences.", "Tip 3: Practice daily."]

class VocabTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vocab Test App ver. 1.0")
        
        # Set window size
        self.root.geometry("400x300")
        
        # Version label
        self.version_label = tk.Label(self.root, text="ver. 1.0")
        self.version_label.place(x=10, y=10)
        
        # Tip label
        self.tip_label = tk.Label(self.root, text="tip: " + random.choice(tips))
        self.tip_label.place(x=10, y=270)
        
        # Info button
        self.info_button = tk.Button(self.root, text="i", command=self.show_info)
        self.info_button.place(x=370, y=270)
        
        # Test button
        self.test_button = tk.Button(self.root, text="TEST!", command=self.start_test, height=2, width=20)
        self.test_button.place(x=100, y=100)
        
        # Word count label on Test button
        self.word_count_label = tk.Label(self.root, text="4") # Sample word count
        self.word_count_label.place(x=260, y=130)
        
        # Voca Manage button
        self.voca_button = tk.Button(self.root, text="VOCA Manage", command=self.manage_voca, height=2, width=15)
        self.voca_button.place(x=50, y=200)
        
        # Setting button
        self.setting_button = tk.Button(self.root, text="Setting", command=self.open_settings, height=2, width=15)
        self.setting_button.place(x=220, y=200)
        
    def start_test(self):
        test_window = tk.Toplevel(self.root)
        test_window.geometry("400x300")
        test_window.title("Start Test")
        tk.Label(test_window, text="Test Started!").pack()

    def manage_voca(self):
        voca_window = tk.Toplevel(self.root)
        voca_window.geometry("400x300")
        voca_window.title("Manage Vocabulary")
        tk.Label(voca_window, text="Manage your vocabulary here.").pack()
        
    def open_settings(self):
        setting_window = tk.Toplevel(self.root)
        setting_window.geometry("200x100")
        setting_window.title("Settings")
        tk.Label(setting_window, text="Settings").pack()
        
    def show_info(self):
        info_window = tk.Toplevel(self.root)
        info_window.geometry("200x100")
        info_window.title("Info")
        tk.Label(info_window, text="This is a vocab test application.").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabTestApp(root)
    root.mainloop()
