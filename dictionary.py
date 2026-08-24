# Create employee dictionary
employee = {
    "E1": {"emp-name": "Ani", "designation": "Manager", "dept": "HR", "salary": 70000},
    "E2": {"emp-name": "Mehu", "designation": "Developer", "dept": "IT", "salary": 65000},
    "E3": {"emp-name": "Soumitra", "designation": "Analyst", "dept": "Finance", "salary": 55000},
    "E4": {"emp-name": "Rima", "designation": "Designer", "dept": "Creative", "salary": 40000},
    "E5": {"emp-name": "Sonai", "designation": "Tester", "dept": "QA", "salary": 48000}
}

# a. Print the record of employee with employee_id E1
print("Record of E1:", employee["E1"])

# b. Print the department of employee E4
print("Department of E4:", employee["E4"]["dept"])

# c. Print the record of employee having maximum salary
max_salary_emp = max(employee, key=lambda emp_id: employee[emp_id]["salary"])
print("Employee with maximum salary:", employee[max_salary_emp])

# d. Insert a new employee record in the existing dictionary
employee["E6"] = {"emp-name": "Suman", "designation": "Intern", "dept": "IT", "salary": 30000}

print("\nUpdated Dictionary:")
for emp_id, details in employee.items():
    print(emp_id, ":", details)


