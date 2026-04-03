import math

# 1. Hàm tính tổng 2 số truyền vào
def tong_hai_so(a, b):
    return a + b

# 2. Hàm tính tổng các số truyền vào (dùng *args)
def tong_nhieu_so(*args):
    return sum(args)

# 3. Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Hàm tìm số nguyên tố trong khoảng [a, b]
def tim_so_nguyen_to_trong_khoang(a, b):
    ket_qua = []
    for so in range(a, b + 1):
        if kiem_tra_nguyen_to(so):
            ket_qua.append(so)
    return ket_qua

# 5. Hàm kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(n):
    if n < 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# 6. Hàm tìm số hoàn hảo trong khoảng [a, b]
def tim_so_hoan_hao_trong_khoang(a, b):
    ket_qua = []
    for so in range(a, b + 1):
        if kiem_tra_so_hoan_hao(so):
            ket_qua.append(so)
    return ket_qua

# 7. Menu chính
def menu():
    while True:
        print("\n" + "=" * 40)
        print("           MENU CHỌN CHỨC NĂNG")
        print("=" * 40)
        print("1. Tính tổng 2 số")
        print("2. Tính tổng các số truyền vào")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát chương trình")
        print("=" * 40)
        
        chon = input("Mời bạn chọn chức năng (0-6): ")
        
        if chon == "1":
            try:
                so1 = float(input("Nhập số thứ nhất: "))
                so2 = float(input("Nhập số thứ hai: "))
                print(f"Kết quả: {so1} + {so2} = {tong_hai_so(so1, so2)}")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
        
        elif chon == "2":
            try:
                day_so = input("Nhập các số cách nhau bằng dấu cách: ").split()
                day_so_so = [float(x) for x in day_so]
                print(f"Tổng các số {day_so_so} = {tong_nhieu_so(*day_so_so)}")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
        
        elif chon == "3":
            try:
                n = int(input("Nhập số nguyên cần kiểm tra: "))
                if kiem_tra_nguyen_to(n):
                    print(f"{n} LÀ số nguyên tố")
                else:
                    print(f"{n} KHÔNG phải là số nguyên tố")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        
        elif chon == "4":
            try:
                a = int(input("Nhập a (đầu khoảng): "))
                b = int(input("Nhập b (cuối khoảng): "))
                if a > b:
                    print("Lỗi: a phải <= b!")
                else:
                    ket_qua = tim_so_nguyen_to_trong_khoang(a, b)
                    if ket_qua:
                        print(f"Các số nguyên tố trong [{a}, {b}] là: {ket_qua}")
                    else:
                        print(f"Không có số nguyên tố nào trong khoảng [{a}, {b}]")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        
        elif chon == "5":
            try:
                n = int(input("Nhập số cần kiểm tra: "))
                if kiem_tra_so_hoan_hao(n):
                    print(f"{n} LÀ số hoàn hảo")
                else:
                    print(f"{n} KHÔNG phải là số hoàn hảo")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        
        elif chon == "6":
            try:
                a = int(input("Nhập a (đầu khoảng): "))
                b = int(input("Nhập b (cuối khoảng): "))
                if a > b:
                    print("Lỗi: a phải <= b!")
                else:
                    ket_qua = tim_so_hoan_hao_trong_khoang(a, b)
                    if ket_qua:
                        print(f"Các số hoàn hảo trong [{a}, {b}] là: {ket_qua}")
                    else:
                        print(f"Không có số hoàn hảo nào trong khoảng [{a}, {b}]")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 6!")

# Chạy chương trình
if __name__ == "__main__":
    menu()