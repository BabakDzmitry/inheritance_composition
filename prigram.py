from hr import CommissionEmployee
from hr import Employee
from hr import HourlyEmployee
from hr import PayrollSystem
from hr import SalaryEmployee

salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "John Doe", 40, 15)
commission_employee = CommissionEmployee(3, "Kevin Bacon", 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(
    [
        salary_employee,
        hourly_employee,
        commission_employee,
    ]
)
