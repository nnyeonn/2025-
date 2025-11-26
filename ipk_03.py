import tkinter as tk
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def draw(self, canvas):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="tomato", outline="black")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill="skyblue", outline="black")


root = tk.Tk()
root.title("문제3")
root.geometry("300x220")

label_top = tk.Label(root, text="도형을 선택하고 그리기를 누르세요.")
label_top.pack(pady=3)

canvas = tk.Canvas(root, width=280, height=100, bg="white")
canvas.pack(pady=2)

shape_var = tk.StringVar(value="rect")

rb_frame = tk.Frame(root)
rb_frame.pack()

r1 = tk.Radiobutton(rb_frame, text="사각형", variable=shape_var, value="rect")
r2 = tk.Radiobutton(rb_frame, text="원", variable=shape_var, value="circle")
r1.grid(row=0, column=0, padx=10)
r2.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", fg="black")
result_label.pack(pady=5)

def draw_shape():
    canvas.delete("all")
    if shape_var.get() == "rect":
        s = Rectangle(50, 30, 100, 60)
    else:
        s = Circle(150, 70, 40)
    s.draw(canvas)
    result_label.config(text=f"면적={s.area():.2f}, 둘레={s.perimeter():.2f}")

btn = tk.Button(root, text="그리기", width=10, command=draw_shape)
btn.pack(pady=5)

root.mainloop()
