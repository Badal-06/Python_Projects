from tkinter import *

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100  # convert cm to meters
        weight = float(entry_weight.get())
        bmi = weight / (height * height)
        result_label.config(text=f"Your BMI is: {round(bmi, 2)}")
    except ValueError:
        result_label.config(text="❌ Enter valid numbers!")

# GUI Setup
root = Tk()
root.title("BMI Calculator")
root.geometry("300x200")

Label(root, text="Height (cm):").pack(pady=5)
entry_height = Entry(root)
entry_height.pack()

Label(root, text="Weight (kg):").pack(pady=5)
entry_weight = Entry(root)
entry_weight.pack()

Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = Label(root, text="")
result_label.pack()

root.mainloop()