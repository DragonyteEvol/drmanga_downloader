import tkinter as tk
from PIL import Image

path = '2.png'

root = tk.Tk()
img = tk.PhotoImage(file=path)
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()

