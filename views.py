import tkinter as tk
from controllers import AppController

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vocab Test App ver. 1.0")
        
        # Set window size
        self.root.geometry("400x300")
        
        self.controller = AppController(self)
        
        # Version label
        self.version_label = tk.Label(self.root, text="ver. 1.0")
        self.version_label.place(x=10, y=10)
        
        # Tip label
        self.tip_label = tk.Label(self.root, text="tip: " + self.controller.get_random_tip())
        self.tip_label.place(x=10, y=270)
        
        # Info button
        self.info_button = tk.Button(self.root, text="i", command=self.controller.show_info)
        self.info_button.place(x=370, y=270)
        
        # Test button
        self.test_button = tk.Button(self.root, text="TEST!", command=self.controller.start_test, height=2, width=20)
        self.test_button.place(x=100, y=100)
        
        # Word count label on Test button
        self.word_count_label = tk.Label(self.root, text=self.controller.get_word_count()) # Sample word count
        self.word_count_label.place(x=260, y=130)
        
        # Voca Manage button
        self.voca_button = tk.Button(self.root, text="VOCA Manage", command=self.controller.manage_voca, height=2, width=15)
        self.voca_button.place(x=50, y=200)
        
        # Setting button
        self.setting_button = tk.Button(self.root, text="Setting", command=self.controller.open_settings, height=2, width=15)
        self.setting_button.place(x=220, y=200)
