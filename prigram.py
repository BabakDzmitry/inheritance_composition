from disgruntled import DisgruntledEmployee
from hr import SalaryEmployee, PayrollSystem, Employee
from hr import HourlyEmployee
from hr import CommissionEmployee

salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "John Doe", 40, 15)
commission_employee = CommissionEmployee(3, "Kevin Bacon", 1000, 250)
disgruntled_employee = DisgruntledEmployee(20000, "Anon")
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(
    [
        salary_employee,
        hourly_employee,
        commission_employee,
        disgruntled_employee,
    ]
)
