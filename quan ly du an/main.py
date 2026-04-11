from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from exceptions.employee_exceptions import (
    EmployeeException,
    InvalidAgeError,
    InvalidSalaryError,
    InvalidPerformanceError,
)


def load_sample_data(company):
    # Manager
    emp1 = Manager("M01", "Nguyen Van An", 40, "an.manager@abc.com", 20000000)
    emp1.projects = ["ERP", "CRM"]
    emp1.performance = 9.2

    emp2 = Manager("M02", "Tran Thi Hoa", 38, "hoa.manager@abc.com", 18000000)
    emp2.projects = ["HRM"]
    emp2.performance = 8.7

    # Developer
    emp3 = Developer("D01", "Le Quang Minh", 28, "minh.dev@abc.com", 15000000, "Python")
    emp3.projects = ["ERP", "AI Chatbot"]
    emp3.performance = 9.0

    emp4 = Developer("D02", "Pham Tuan Kiet", 26, "kiet.dev@abc.com", 14000000, "Java")
    emp4.projects = ["CRM"]
    emp4.performance = 7.8

    emp5 = Developer("D03", "Vo Ngoc Huyen", 27, "huyen.dev@abc.com", 14500000, "C#")
    emp5.projects = ["Accounting System"]
    emp5.performance = 8.4

    emp6 = Developer("D04", "Do Thanh Tung", 25, "tung.dev@abc.com", 13000000, "JavaScript")
    emp6.projects = ["Website", "Landing Page"]
    emp6.performance = 6.9

    emp10 = Developer("D05", "Nguyen Duc Long", 30, "long.dev@abc.com", 16000000, "PHP")
    emp10.projects = []
    emp10.performance = 5.5
    emp10.is_active = False

    # Intern
    emp7 = Intern("I01", "Bui Gia Bao", 21, "bao.intern@abc.com", 4000000)
    emp7.projects = ["Website"]
    emp7.performance = 7.0

    emp8 = Intern("I02", "Dang Thu Trang", 22, "trang.intern@abc.com", 4500000)
    emp8.projects = ["Testing"]
    emp8.performance = 8.0

    emp9 = Intern("I03", "Hoang Minh Chau", 20, "chau.intern@abc.com", 3500000)
    emp9.projects = []
    emp9.performance = 6.2

    sample_employees = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]

    for emp in sample_employees:
        company.add_employee(emp)


def input_email():
    email = input("Nhập email: ").strip()
    if "@" not in email:
        raise ValueError("Email sai định dạng")
    return email


def input_age():
    age = int(input("Nhập tuổi: "))
    if age < 18 or age > 65:
        raise InvalidAgeError()
    return age


def input_positive_number(message):
    value = float(input(message))
    if value <= 0:
        raise InvalidSalaryError()
    return value


def input_performance():
    score = float(input("Nhập điểm hiệu suất (0-10): "))
    if score < 0 or score > 10:
        raise InvalidPerformanceError()
    return score


def add_employee_menu(company):
    print("\na. Thêm Manager")
    print("b. Thêm Developer")
    print("c. Thêm Intern")
    sub = input("Chọn: ").lower().strip()

    emp_id = input("Nhập ID: ").strip()
    name = input("Nhập tên: ").strip()
    age = input_age()
    email = input_email()

    if sub == "a":
        salary = input_positive_number("Nhập lương cơ bản: ")
        emp = Manager(emp_id, name, age, email, salary)

    elif sub == "b":
        salary = input_positive_number("Nhập lương cơ bản: ")
        language = input("Nhập ngôn ngữ lập trình: ").strip()
        emp = Developer(emp_id, name, age, email, salary, language)

    elif sub == "c":
        stipend = input_positive_number("Nhập trợ cấp: ")
        emp = Intern(emp_id, name, age, email, stipend)

    else:
        print("Lựa chọn không hợp lệ")
        return

    company.add_employee(emp)
    print("Đã thêm nhân viên thành công")


def show_employee_menu(company):
    print("\na. Tất cả nhân viên")
    print("b. Theo loại (Manager/Developer/Intern)")
    print("c. Theo hiệu suất từ cao đến thấp")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        company.show_all()
    elif sub == "b":
        role = input("Nhập loại nhân viên: ").strip()
        company.show_by_role(role)
    elif sub == "c":
        company.show_by_performance_desc()
    else:
        print("Lựa chọn không hợp lệ")


def search_employee_menu(company):
    print("\na. Theo ID")
    print("b. Theo tên")
    print("c. Theo ngôn ngữ lập trình")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        emp_id = input("Nhập ID: ").strip()
        print(company.find_by_id(emp_id))

    elif sub == "b":
        keyword = input("Nhập tên cần tìm: ").strip()
        result = company.find_by_name(keyword)
        if result:
            for emp in result:
                print(emp)
        else:
            print("Không tìm thấy")

    elif sub == "c":
        language = input("Nhập ngôn ngữ: ").strip()
        result = company.find_developer_by_language(language)
        if result:
            for emp in result:
                print(emp)
        else:
            print("Không tìm thấy")

    else:
        print("Lựa chọn không hợp lệ")


def salary_menu(company):
    print("\na. Tính lương từng nhân viên")
    print("b. Tính tổng lương công ty")
    print("c. Top 3 nhân viên lương cao nhất")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        employees = company.get_all_employees()
        if not employees:
            print("Chưa có dữ liệu")
            return
        for emp in employees:
            print(f"{emp.name} - {emp.calculate_salary():,.0f}")

    elif sub == "b":
        print(f"Tổng lương công ty: {company.total_salary():,.0f}")

    elif sub == "c":
        top = company.top_3_salary()
        if top:
            for emp in top:
                print(emp)
        else:
            print("Chưa có dữ liệu")

    else:
        print("Lựa chọn không hợp lệ")


def project_menu(company):
    print("\na. Phân công nhân viên vào dự án")
    print("b. Xóa nhân viên khỏi dự án")
    print("c. Hiển thị dự án của 1 nhân viên")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        emp_id = input("Nhập ID nhân viên: ").strip()
        project = input("Nhập tên dự án: ").strip()
        company.allocate_project(emp_id, project)
        print("Phân công thành công")

    elif sub == "b":
        emp_id = input("Nhập ID nhân viên: ").strip()
        project = input("Nhập tên dự án: ").strip()
        company.remove_project(emp_id, project)

    elif sub == "c":
        emp_id = input("Nhập ID nhân viên: ").strip()
        emp = company.find_by_id(emp_id)
        if emp.projects:
            print(f"Dự án của {emp.name}: {', '.join(emp.projects)}")
        else:
            print(f"{emp.name} chưa có dự án nào")

    else:
        print("Lựa chọn không hợp lệ")


def performance_menu(company):
    print("\na. Cập nhật điểm hiệu suất")
    print("b. Hiển thị nhân viên xuất sắc (> 8)")
    print("c. Hiển thị nhân viên cần cải thiện (< 5)")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        emp_id = input("Nhập ID nhân viên: ").strip()
        score = input_performance()
        company.update_performance(emp_id, score)
        print("Cập nhật thành công")

    elif sub == "b":
        result = company.excellent_employees()
        if result:
            for emp in result:
                print(emp)
        else:
            print("Không có nhân viên xuất sắc")

    elif sub == "c":
        result = company.weak_employees()
        if result:
            for emp in result:
                print(emp)
        else:
            print("Không có nhân viên cần cải thiện")

    else:
        print("Lựa chọn không hợp lệ")


def hr_menu(company):
    print("\na. Xóa nhân viên khỏi danh sách")
    print("b. Tăng lương / trợ cấp")
    print("c. Giảm lương / trợ cấp")
    print("d. Thăng chức")
    print("e. Cho nghỉ việc")
    print("f. Tính đền bù hợp đồng")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        emp_id = input("Nhập ID cần xóa: ").strip()
        company.remove_employee(emp_id)
        print("Đã xóa nhân viên")

    elif sub == "b":
        emp_id = input("Nhập ID nhân viên: ").strip()
        amount = input_positive_number("Nhập số tiền tăng: ")
        company.increase_base_salary(emp_id, amount)

    elif sub == "c":
        emp_id = input("Nhập ID nhân viên: ").strip()
        amount = input_positive_number("Nhập số tiền giảm: ")
        company.decrease_base_salary(emp_id, amount)

    elif sub == "d":
        emp_id = input("Nhập ID nhân viên: ").strip()
        company.promote_employee(emp_id)

    elif sub == "e":
        emp_id = input("Nhập ID nhân viên: ").strip()
        company.terminate_employee(emp_id)

    elif sub == "f":
        emp_id = input("Nhập ID nhân viên: ").strip()
        compensation = company.compensation_employee(emp_id)
        print(f"Số tiền đền bù hợp đồng: {compensation:,.0f}")

    else:
        print("Lựa chọn không hợp lệ")


def report_menu(company):
    print("\na. Số lượng nhân viên theo loại")
    print("b. Tổng lương theo loại")
    print("c. Điểm hiệu suất trung bình")
    sub = input("Chọn: ").lower().strip()

    if sub == "a":
        company.report_count_by_role()
    elif sub == "b":
        company.report_total_salary_by_role()
    elif sub == "c":
        company.report_average_performance()
    else:
        print("Lựa chọn không hợp lệ")


def main():
    company = Company()
    load_sample_data(company)

    while True:
        try:
            print("\n" + "=" * 65)
            print("           HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
            print("=" * 65)
            print("1. Thêm nhân viên mới")
            print("2. Hiển thị danh sách nhân viên")
            print("3. Tìm kiếm nhân viên")
            print("4. Quản lý lương")
            print("5. Quản lý dự án")
            print("6. Đánh giá hiệu suất")
            print("7. Quản lý nhân sự")
            print("8. Thống kê báo cáo")
            print("9. Thoát")

            choice = input("Chọn chức năng (1-9): ").strip()

            if choice == "1":
                add_employee_menu(company)
            elif choice == "2":
                show_employee_menu(company)
            elif choice == "3":
                search_employee_menu(company)
            elif choice == "4":
                salary_menu(company)
            elif choice == "5":
                project_menu(company)
            elif choice == "6":
                performance_menu(company)
            elif choice == "7":
                hr_menu(company)
            elif choice == "8":
                report_menu(company)
            elif choice == "9":
                print("Thoát chương trình")
                break
            else:
                raise ValueError("Nhập số không hợp lệ, vui lòng nhập từ 1 đến 9")

        except EmployeeException as e:
            print("Lỗi:", e)
        except ValueError as e:
            print("Lỗi:", e)
        except IndexError:
            print("Lỗi: Chưa có dữ liệu")


if __name__ == "__main__":
    main()