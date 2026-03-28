# Bài 3: Tính tuổi từ năm sinh
import time

x = time.localtime()
year = x[0]

birth_year = int(input("Nhập năm sinh: "))
age = year - birth_year

print(f"Năm sinh {birth_year}, vậy bạn {age} tuổi")