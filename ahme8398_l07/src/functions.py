def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    OVERTIME_FACTOR = 1.5
    OVERTIME_RATE = 40
    TAX_RATE = 0.03625
    
    total_pay = 0
    total_employees = 0
    
    while True:
        emp_id = input("Employee ID: ")
        if emp_id == '0':
            break
            
        hourly_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))
        
        gross_pay = hourly_rate * hours_worked
        overtime_pay = 0
        
        if hours_worked > OVERTIME_RATE:
            overtime_hours = hours_worked - OVERTIME_RATE
            overtime_pay = overtime_hours * hourly_rate * OVERTIME_FACTOR
            gross_pay += overtime_pay
        
        net_pay = gross_pay * (1 - TAX_RATE)
        total_pay += net_pay
        total_employees += 1
        
        print(f"Net payment for employee {emp_id}: ${net_pay:.2f}\n")
    
    average_pay = total_pay / total_employees
    return total_pay, average_pay
