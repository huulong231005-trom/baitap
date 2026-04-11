class Employee:
    def __init__(self, emp_id, name, age, email):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.projects = []
        self.performance = 0
        self.is_active = True

    def calculate_salary(self):
        return 0

    def add_project(self, project_name):
        if len(self.projects) >= 5:
            return False
        self.projects.append(project_name)
        return True

    def remove_project(self, project_name):
        if project_name in self.projects:
            self.projects.remove(project_name)
            return True
        return False

    def set_performance(self, score):
        self.performance = score

    def get_role(self):
        return "Employee"

    def get_compensation(self):
        return self.calculate_salary() * 2

    def __str__(self):
        status = "Đang làm việc" if self.is_active else "Đã nghỉ việc"
        return (
            f"ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | "
            f"Email: {self.email} | Chức vụ: {self.get_role()} | "
            f"Lương: {self.calculate_salary():,.0f} | "
            f"Hiệu suất: {self.performance} | "
            f"Trạng thái: {status} | "
            f"Dự án: {', '.join(self.projects) if self.projects else 'Không có'}"
        )