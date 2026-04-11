from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    ProjectAllocationError,
    DuplicateEmployeeError,
    InvalidSalaryError,
)

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        for emp in self.employees:
            if emp.emp_id == employee.emp_id:
                raise DuplicateEmployeeError()
        self.employees.append(employee)

    def get_all_employees(self):
        return self.employees

    def find_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        raise EmployeeNotFoundError(emp_id)

    def find_by_name(self, keyword):
        keyword = keyword.lower()
        return [emp for emp in self.employees if keyword in emp.name.lower()]

    def find_developer_by_language(self, language):
        language = language.lower()
        result = []
        for emp in self.employees:
            if emp.get_role() == "Developer" and hasattr(emp, "language"):
                if emp.language.lower() == language:
                    result.append(emp)
        return result

    def show_all(self):
        if not self.employees:
            print("Danh sách nhân viên rỗng")
            return
        for emp in self.employees:
            print(emp)

    def show_by_role(self, role):
        found = False
        for emp in self.employees:
            if emp.get_role().lower() == role.lower():
                print(emp)
                found = True
        if not found:
            print("Không có nhân viên thuộc loại này")

    def show_by_performance_desc(self):
        if not self.employees:
            print("Danh sách rỗng")
            return
        sorted_list = sorted(self.employees, key=lambda x: x.performance, reverse=True)
        for emp in sorted_list:
            print(emp)

    def total_salary(self):
        return sum(emp.calculate_salary() for emp in self.employees if emp.is_active)

    def top_3_salary(self):
        active_employees = [emp for emp in self.employees if emp.is_active]
        sorted_list = sorted(active_employees, key=lambda x: x.calculate_salary(), reverse=True)
        return sorted_list[:3]

    def allocate_project(self, emp_id, project_name):
        emp = self.find_by_id(emp_id)
        if not emp.is_active:
            print("Nhân viên đã nghỉ việc, không thể phân công dự án")
            return
        if not emp.add_project(project_name):
            raise ProjectAllocationError()

    def remove_project(self, emp_id, project_name):
        emp = self.find_by_id(emp_id)
        if emp.remove_project(project_name):
            print("Đã xóa nhân viên khỏi dự án")
        else:
            print("Nhân viên không thuộc dự án này")

    def update_performance(self, emp_id, score):
        emp = self.find_by_id(emp_id)
        emp.set_performance(score)

    def excellent_employees(self):
        return [emp for emp in self.employees if emp.performance > 8]

    def weak_employees(self):
        return [emp for emp in self.employees if emp.performance < 5]

    def remove_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        self.employees.remove(emp)

    def increase_base_salary(self, emp_id, amount):
        emp = self.find_by_id(emp_id)
        if amount <= 0:
            raise InvalidSalaryError()

        if hasattr(emp, "base_salary"):
            emp.base_salary += amount
            print("Đã tăng lương")
        elif hasattr(emp, "stipend"):
            emp.stipend += amount
            print("Đã tăng trợ cấp")
        else:
            print("Không thể tăng lương")

    def decrease_base_salary(self, emp_id, amount):
        emp = self.find_by_id(emp_id)
        if amount <= 0:
            raise InvalidSalaryError()

        if hasattr(emp, "base_salary"):
            if emp.base_salary - amount < 0:
                raise InvalidSalaryError()
            emp.base_salary -= amount
            print("Đã giảm lương")
        elif hasattr(emp, "stipend"):
            if emp.stipend - amount < 0:
                raise InvalidSalaryError()
            emp.stipend -= amount
            print("Đã giảm trợ cấp")
        else:
            print("Không thể giảm lương")

    def terminate_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        emp.is_active = False
        emp.projects.clear()
        print(f"Nhân viên {emp.name} đã nghỉ việc")

    def compensation_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        compensation = emp.get_compensation()
        return compensation

    def promote_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        current_role = emp.get_role()

        if current_role == "Intern":
            from models.developer import Developer
            new_emp = Developer(emp.emp_id, emp.name, emp.age, emp.email, 8000000, "Python")
            new_emp.projects = emp.projects
            new_emp.performance = emp.performance
            new_emp.is_active = emp.is_active
        elif current_role == "Developer":
            from models.manager import Manager
            new_emp = Manager(emp.emp_id, emp.name, emp.age, emp.email, 15000000)
            new_emp.projects = emp.projects
            new_emp.performance = emp.performance
            new_emp.is_active = emp.is_active
        else:
            print("Manager không thể thăng chức thêm")
            return

        self.employees.remove(emp)
        self.employees.append(new_emp)
        print(f"Đã thăng chức {current_role} -> {new_emp.get_role()}")

    def report_count_by_role(self):
        manager_count = sum(1 for emp in self.employees if emp.get_role() == "Manager")
        developer_count = sum(1 for emp in self.employees if emp.get_role() == "Developer")
        intern_count = sum(1 for emp in self.employees if emp.get_role() == "Intern")

        print(f"Manager: {manager_count}")
        print(f"Developer: {developer_count}")
        print(f"Intern: {intern_count}")

    def report_total_salary_by_role(self):
        manager_salary = sum(emp.calculate_salary() for emp in self.employees if emp.get_role() == "Manager" and emp.is_active)
        developer_salary = sum(emp.calculate_salary() for emp in self.employees if emp.get_role() == "Developer" and emp.is_active)
        intern_salary = sum(emp.calculate_salary() for emp in self.employees if emp.get_role() == "Intern" and emp.is_active)

        print(f"Tổng lương Manager: {manager_salary:,.0f}")
        print(f"Tổng lương Developer: {developer_salary:,.0f}")
        print(f"Tổng lương Intern: {intern_salary:,.0f}")

    def report_average_performance(self):
        if not self.employees:
            print("Chưa có dữ liệu")
            return
        avg = sum(emp.performance for emp in self.employees) / len(self.employees)
        print(f"Điểm hiệu suất trung bình: {avg:.2f}")