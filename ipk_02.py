import tkinter as tk

class Pet:
    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

person = Person("홍길동")

root = tk.Tk()
root.title("문제2")
root.geometry("400x200")

label_top = tk.Label(root, text="반려동물을 선택하고 '말하기'를 누르세요.")
label_top.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

def select_dog():
    person.pet = Dog()
    result_label.config(text="강아지를 선택했습니다.")

def select_cat():
    person.pet = Cat()
    result_label.config(text="고양이를 선택했습니다.")

def speak():
    if person.pet:
        result = person.pet.speak()
        result_label.config(text=f"{person.name}의 반려동물 → {result}")
    else:
        result_label.config(text="반려동물을 먼저 선택하세요.")

btn_dog = tk.Button(root, text="강아지 선택", command=select_dog)
btn_cat = tk.Button(root, text="고양이 선택", command=select_cat)
btn_speak = tk.Button(root, text="말하기", command=speak)

btn_dog.pack()
btn_cat.pack()
btn_speak.pack()

root.mainloop()
