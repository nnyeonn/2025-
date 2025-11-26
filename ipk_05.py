import tkinter as tk

class Pet:
    def __init__(self, name):
        self.name = name

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
root.title("문제 5")
root.geometry("700x300")

label_title = tk.Label(root, text="반려동물 등록하기", font=("Arial", 14))
label_title.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack()

kind = tk.StringVar(value="dog")
rb1 = tk.Radiobutton(root, text="강아지", variable=kind, value="dog")
rb2 = tk.Radiobutton(root, text="고양이", variable=kind, value="cat")
rb1.pack()
rb2.pack()

vaccine = tk.IntVar()
neutral = tk.IntVar()
cb1 = tk.Checkbutton(root, text="예방접종 완료", variable=vaccine)
cb2 = tk.Checkbutton(root, text="중성화 완료", variable=neutral)
cb1.pack()
cb2.pack()

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=15)

def register_pet():
    name = entry.get().strip()
    if name == "":
        name = "이름없음"

    if kind.get() == "dog":
        pet = Dog(name)
    else:
        pet = Cat(name)

    person.pet = pet

    vtxt = "예방접종 완료" if vaccine.get() else "예방접종 미완료"
    ntxt = "중성화 완료" if neutral.get() else "중성화 미완료"

    result = (
        f"반려동물 등록 완료!\n"
        f"이름: {pet.name}\n"
        f"종류: {pet.__class__.__name__}\n"
        f"소리: {pet.speak()}\n"
        f"{vtxt}, {ntxt}"
    )
    result_label.config(text=result)

def reset_all():
    entry.delete(0, tk.END)
    vaccine.set(0)
    neutral.set(0)
    result_label.config(text="")

btn_reg = tk.Button(root, text="등록하기", command=register_pet)
btn_reset = tk.Button(root, text="초기화", command=reset_all)

btn_reg.pack()
btn_reset.pack()

root.mainloop()
