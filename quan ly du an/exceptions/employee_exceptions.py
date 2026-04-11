class EmployeeException(Exception):
    pass


class EmployeeNotFoundError(EmployeeException):
    def __init__(self, emp_id):
        super().__init__(f"Không tìm thấy nhân viên có ID: {emp_id}")


class InvalidSalaryError(EmployeeException):
    def __init__(self):
        super().__init__("Lương không hợp lệ")


class InvalidAgeError(EmployeeException):
    def __init__(self):
        super().__init__("Tuổi không hợp lệ (phải từ 18 đến 65)")


class ProjectAllocationError(EmployeeException):
    def __init__(self):
        super().__init__("Phân công dự án thất bại (nhân viên đã có tối đa 5 dự án)")


class DuplicateEmployeeError(EmployeeException):
    def __init__(self):
        super().__init__("Trùng mã nhân viên")


class InvalidPerformanceError(EmployeeException):
    def __init__(self):
        super().__init__("Điểm hiệu suất không hợp lệ (0-10)")