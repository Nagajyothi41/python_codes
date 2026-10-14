# 1. Calculate Employee Salary
# Question: Write a Python program to accept an employee's ID, name, basic salary, HRA, and DA, then calculate the gross salary.
# Code:
# employee_id = input("Enter employee ID: ")name = input("Enter employee name: ")basic_salary = float(input("Enter basic salary: "))hra = float(input("Enter HRA: "))da = float(input("Enter DA: "))gross_salary = basic_salary + hra + daprint("\n--- Employee Salary Details ---")print("Employee ID:", employee_id)print("Employee Name:", name)print("Basic Salary:", basic_salary)print("HRA:", hra)print("DA:", da)print("Gross Salary:", gross_salary)



# Output:
# Enter employee ID: E101
# Enter employee name: Ravi
# Enter basic salary: 30000
# Enter HRA: 5000
# Enter DA: 3000

# --- Employee Salary Details ---
# Employee ID: E101
# Employee Name: Ravi
# Basic Salary: 30000.0
# HRA: 5000.0
# DA: 3000.0
# Gross Salary: 38000.0


# 2. Calculate Salary After Deductions
# Question: Write a Python program to calculate an employee's net salary after deducting PF, professional tax, and other deductions from the gross salary.
# Code:
# gross_salary = float(input("Enter gross salary: "))pf = float(input("Enter PF deduction: "))professional_tax = float(input("Enter professional tax: "))other_deductions = float(input("Enter other deductions: "))total_deductions = pf + professional_tax + other_deductionsnet_salary = gross_salary - total_deductionsprint("\n--- Salary Calculation ---")print("Gross Salary:", gross_salary)print("PF Deduction:", pf)print("Professional Tax:", professional_tax)print("Other Deductions:", other_deductions)print("Total Deductions:", total_deductions)print("Net Salary:", net_salary)



# Output:
# Enter gross salary: 38000
# Enter PF deduction: 1800
# Enter professional tax: 200
# Enter other deductions: 500

# --- Salary Calculation ---
# Gross Salary: 38000.0
# PF Deduction: 1800.0
# Professional Tax: 200.0
# Other Deductions: 500.0
# Total Deductions: 2500.0
# Net Salary: 35500.0


# 3. Generate Monthly Payslip
# Question: Write a Python program to accept employee details, salary components, and deductions, then generate a monthly payslip displaying the employee's name, ID, earnings, deductions, and net salary.
# Code:
# employee_id = input("Enter employee ID: ")name = input("Enter employee name: ")basic = float(input("Enter basic salary: "))hra = float(input("Enter HRA: "))da = float(input("Enter DA: "))pf = float(input("Enter PF deduction: "))tax = float(input("Enter professional tax: "))other = float(input("Enter other deductions: "))gross_salary = basic + hra + datotal_deductions = pf + tax + othernet_salary = gross_salary - total_deductionsprint("\n========== MONTHLY PAYSLIP ==========")print("Employee ID:", employee_id)print("Employee Name:", name)print("-------------------------------------")print("Basic Salary: ₹", basic)print("HRA: ₹", hra)print("DA: ₹", da)print("Gross Salary: ₹", gross_salary)print("-------------------------------------")print("PF: ₹", pf)print("Professional Tax: ₹", tax)print("Other Deductions: ₹", other)print("Total Deductions: ₹", total_deductions)print("-------------------------------------")print("Net Salary: ₹", net_salary)print("=====================================")



# Output:
# Enter employee ID: E101
# Enter employee name: Ravi
# Enter basic salary: 30000
# Enter HRA: 5000
# Enter DA: 3000
# Enter PF deduction: 1800
# Enter professional tax: 200
# Enter other deductions: 500

# ========== MONTHLY PAYSLIP ==========
# Employee ID: E101
# Employee Name: Ravi
# -------------------------------------
# Basic Salary: ₹ 30000.0
# HRA: ₹ 5000.0
# DA: ₹ 3000.0
# Gross Salary: ₹ 38000.0
# -------------------------------------
# PF: ₹ 1800.0
# Professional Tax: ₹ 200.0
# Other Deductions: ₹ 500.0
# Total Deductions: ₹ 2500.0
# -------------------------------------
# Net Salary: ₹ 35500.0
# =====================================


# 4. Calculate Overtime Pay
# Question: Write a Python program to calculate an employee's monthly salary by adding overtime payment based on the number of extra hours worked and the overtime rate per hour.
# Code:
# employee_name = input("Enter employee name: ")basic_salary = float(input("Enter monthly salary: "))overtime_hours = float(input("Enter overtime hours: "))overtime_rate = float(input("Enter overtime rate per hour: "))overtime_pay = overtime_hours * overtime_ratetotal_salary = basic_salary + overtime_payprint("\n--- Overtime Salary Details ---")print("Employee Name:", employee_name)print("Basic Monthly Salary: ₹", basic_salary)print("Overtime Hours:", overtime_hours)print("Overtime Pay: ₹", overtime_pay)print("Total Monthly Salary: ₹", total_salary)



# Output:
# Enter employee name: Ravi
# Enter monthly salary: 30000
# Enter overtime hours: 10
# Enter overtime rate per hour: 200

# --- Overtime Salary Details ---
# Employee Name: Ravi
# Basic Monthly Salary: ₹ 30000.0
# Overtime Hours: 10.0
# Overtime Pay: ₹ 2000.0
# Total Monthly Salary: ₹ 32000.0


# 5. Employee Payroll Management Using a Dictionary
# Question: Write a Python program to store multiple employees' details in a dictionary, calculate their net salaries, and display a payroll report containing employee IDs, names, gross salaries, deductions, and net salaries.
# Code:
# employees = {    "E101": {        "name": "Ravi",        "basic": 30000,        "hra": 5000,        "da": 3000,        "deductions": 2500    },    "E102": {        "name": "Priya",        "basic": 40000,        "hra": 6000,        "da": 4000,        "deductions": 3500    },    "E103": {        "name": "Kiran",        "basic": 25000,        "hra": 4000,        "da": 2000,        "deductions": 2000    }}print("========== PAYROLL REPORT ==========")for emp_id, details in employees.items():    gross_salary = details["basic"] + details["hra"] + details["da"]    deductions = details["deductions"]    net_salary = gross_salary - deductions    print("\nEmployee ID:", emp_id)    print("Employee Name:", details["name"])    print("Gross Salary: ₹", gross_salary)    print("Deductions: ₹", deductions)



# Output:
# ========== PAYROLL REPORT ==========

# Employee ID: E101
# Employee Name: Ravi
# Gross Salary: ₹ 38000
# Deductions: ₹ 2500
# Net Salary: ₹ 35500

# Employee ID: E102
# Employee Name: Priya
# Gross Salary: ₹ 50000
# Deductions: ₹ 3500
# Net Salary: ₹ 46500

# Employee ID: E103
# Employee Name: Kiran
# Gross Salary: ₹ 31000
# Deductions: ₹ 2000
# Net Salary: ₹ 29000

# ====================================