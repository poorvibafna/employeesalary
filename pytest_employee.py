from employee_salary import employee_details

def test_employee():
    assert employee_details("Rahul", 101, "IT", 35000) == "Employee Name: Rahul\nEmployee ID: 101\nDepartment: IT\nSalary: Rs. 35000"

def test_employee_hr():
    assert employee_details("Priya", 102, "HR", 40000) == "Employee Name: Priya\nEmployee ID: 102\nDepartment: HR\nSalary: Rs. 40000"

def test_employee_zero_salary():
    assert employee_details("Amit", 103, "Sales", 0) == "Employee Name: Amit\nEmployee ID: 103\nDepartment: Sales\nSalary: Rs. 0"
