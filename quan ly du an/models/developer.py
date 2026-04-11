from models.employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, language):
        super().__init__(emp_id, name, age, email)
        self.base_salary = base_salary
        self.language = language

    def calculate_salary(self):
        return self.base_salary + 2000000

    def get_role(self):
        return "Developer"

    def __str__(self):
        return (
            f"ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | "
            f"Email: {self.email} | Chức vụ: {self.get_role()} | "
            f"Ngôn ngữ: {self.language} | "
            f"Lương: {self.calculate_salary():,.0f} | "
            f"Hiệu suất: {self.performance} | "
            f"Dự án: {', '.join(self.projects) if self.projects else 'Không có'}"
        )