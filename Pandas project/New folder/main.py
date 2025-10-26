from tkinter import *
import pandas as pd

window = Tk()
window.minsize(width=600,height=600)
window.title("Plant Label")
window.mainloop()

data = pd.read_csv("C:\Users\Swati\Pandas project\New folder\plant_part.csv")