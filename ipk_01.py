import tkinter as tk

class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."


car = Car("car1")
truck = Truck("truck1")

root = tk.Tk()
root.title("문제1")
root.geometry("400x300")

label_info = tk.Label(root, text="버튼을 눌러보세요.")
label_info.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

def run_car():
    result_label.config(text=car.drive())

def run_truck():
    result_label.config(text=truck.drive())

btn_car = tk.Button(root, text="자동차 주행", command=run_car)
btn_truck = tk.Button(root, text="트럭 주행", command=run_truck)

btn_car.pack(pady=5)
btn_truck.pack(pady=5)

root.mainloop()

