import tkinter as tk

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0)

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.grid(row=1, column=0)

        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)

        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_and_display_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_and_display_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = self.calculate_bmi_number(weight, height)
            self.show_bmi_status(bmi)
        except ValueError:
            self.result_label.config(text="Please enter valid input")

    def calculate_bmi_number(self, weight_kg, height_m):
        bmi = weight_kg / (height_m ** 2)
        return bmi

    def show_bmi_status(self, bmi):
        status = self.get_bmi_status_description(bmi)
        self.result_label.config(text=f"BMI: {bmi:.2f}, {status}")

    def get_bmi_status_description(self, bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Healthy Weight'
        else:
            return 'Overweight'


root = tk.Tk()
bmi_calculator = BMI_Calculator(root)
root.mainloop()
