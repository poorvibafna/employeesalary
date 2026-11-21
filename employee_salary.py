def employee_details(name, emp_id, department, salary):
    details = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: Rs. {salary}"
    )
    return details

# Sample employee information
result = employee_details(
    "Rahul",
    101,
    "IT",
    35000
)

print(result)

