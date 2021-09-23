from abc import abstractmethod, ABC


class Employee(ABC):
    def __init__(self, _id, name):
        self.id: int = _id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class PayrollSystem:
    def calculate_payroll(self, employees: list[Employee]):
        print("Calculating Payroll")
        print("===================")

        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print(" ")


class SalaryEmployee(Employee):
    def __init__(self, _id, name, weekly_salary):
        super().__init__(_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, _id, name, hours_worked, hour_rate):
        super().__init__(_id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, _id, name, weekly_salary, commission):
        super().__init__(_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
