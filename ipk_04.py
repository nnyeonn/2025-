import tkinter as tk

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = []

    def enrollCourse(self, subject):
        self.classes.append(subject)

    def clearCourses(self):
        self.classes = []

student = Student("홍길동")

root = tk.Tk()
root.title("문제4")
root.geometry("380x280")

label_title = tk.Label(root, text="학생: 홍길동")
label_title.pack(pady=10)

var_py = tk.IntVar()
var_ai = tk.IntVar()
var_ds = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Python", variable=var_py)
cb2 = tk.Checkbutton(root, text="AI", variable=var_ai)
cb3 = tk.Checkbutton(root, text="DataScience", variable=var_ds)

cb1.pack()
cb2.pack()
cb3.pack()

result_label = tk.Label(root, text="과목을 선택하고 등록하기를 누르세요.")
result_label.pack(pady=15)

def register():
    student.clearCourses()
    if var_py.get() == 1: student.enrollCourse("Python")
    if var_ai.get() == 1: student.enrollCourse("AI")
    if var_ds.get() == 1: student.enrollCourse("DataScience")

    if student.classes:
        result_label.config(text=f"등록된 과목: {', '.join(student.classes)}")
    else:
        result_label.config(text="등록된 과목: 없음")

def reset():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    student.clearCourses()
    result_label.config(text="모든 선택을 해제했습니다.")

btn_reg = tk.Button(root, text="등록하기", command=register)
btn_reset = tk.Button(root, text="초기화", command=reset)
btn_reg.pack()
btn_reset.pack()

root.mainloop()
