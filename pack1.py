from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", bg = "red", fg= "white")
button2= Button(root, text="버튼2", bg = "blue", fg = "black")
button3 = Button(root, text = "버튼3", bg = "green", fg = "black")
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

root.mainloop()