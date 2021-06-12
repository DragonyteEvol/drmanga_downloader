import tkinter as tk
from tkinter import ttk
class Progress_Bar(ttk.Frame): 
    
    def __init__(self, main_window):
        s = ttk.Style()
        s.theme_use('clam')
        s.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='#f8f5f1',
            background='#5e8b7e',
            darkcolor="#f8f5f1",
            #lightcolor="#ED28F0",
            bordercolor="#f8f5f1",
            borderwidth=0,
            )

        super().__init__(main_window)
        self.progressbar = ttk.Progressbar(self,mode="indeterminate",style="custom.Horizontal.TProgressbar",orient="horizontal")
        self.progressbar.step(100)
        self.progressbar.grid(row=6,column=0,columnspan=1)
        self.grid(row=6,column=0,columnspan=1)
        self.progressbar.start(10)
