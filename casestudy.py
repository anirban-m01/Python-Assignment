patients = {
    "P01": {"name": "Akash", "age": 30, "gender": "Male"},
    "P02": {"name": "Riya", "age": 25, "gender": "Female"}
}

appointments = [
    {"patient_id": "P01", "doctor": "Dr. Das", "time": "9:00 AM"},
    {"patient_id": "P02", "doctor": "Dr. Roy", "time": "11:00 AM"}
]

with open("medical_records.txt", "a") as f:
    f.write("P01 - Diabetes Checkup\n")

with open("medical_records.txt", "r") as f:
    print(f.read())


doctor1 = ("Dr. Das", "Cardiologist", 15)  
doctor2 = ("Dr. Roy", "Dermatologist", 10)


class Bill:
    def __init__(self, patient_id, amount):
        self.patient_id = patient_id
        self.amount = amount
    
    def display_bill(self):
        print(f"Bill for {self.patient_id}: ₹{self.amount}")

bill1 = Bill("P01", 15000)
bill1.display_bill()


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Patient_ID": ["P01", "P02"],
    "Amount": [15000, 20000]
}
df = pd.DataFrame(data)


print(df)

df.plot(kind="bar", x="Patient_ID", y="Amount", color="skyblue")
plt.title("Billing Report")
plt.show()


