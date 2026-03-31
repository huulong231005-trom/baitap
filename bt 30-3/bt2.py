def bai1():
    i = 1
    tich = 1
    while i <= 10:
        tich *= i
        i += 1
    print("\n>>> Tích của 10 số tự nhiên đầu tiên là:", tich)
    print("-" * 50)

def bai2():
    n = int(input("Nhập số nguyên dương n: "))
    i = 1
    giai_thua = 1
    while i <= n:
        giai_thua *= i
        i += 1
    print(f">>> {n}! = {giai_thua}")
    print("-" * 50)

def bai3():
    n = int(input("Nhập số nguyên dương n: "))
    if n < 2:
        print(">>> Không phải số nguyên tố")
    else:
        i = 2
        la_nguyen_to = True
        while i * i <= n:
            if n % i == 0:
                la_nguyen_to = False
                break
            i += 1
        if la_nguyen_to:
            print(">>> Đây là số nguyên tố")
        else:
            print(">>> Không phải số nguyên tố")
    print("-" * 50)

def bai4():
    n = int(input("Nhập số nguyên n: "))
    i = 0
    tong = 0
    while i < n:
        if i % 2 == 0:
            tong += i
        i += 1
    print(f">>> Tổng các số chẵn nhỏ hơn {n} là: {tong}")
    print("-" * 50)

# Menu chính
while True:
    print("\n" + "=" * 50)
    print("          CHƯƠNG TRÌNH LUYỆN TẬP WHILE")
    print("=" * 50)
    print("1. Tính tích 10 số tự nhiên đầu tiên")
    print("2. Tính giai thừa của n")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tính tổng số chẵn nhỏ hơn n")
    print("0. Thoát chương trình")
    print("-" * 50)
    
    chon = input("Mời bạn chọn (0-4): ")
    
    if chon == "1":
        bai1()
    elif chon == "2":
        bai2()
    elif chon == "3":
        bai3()
    elif chon == "4":
        bai4()
    elif chon == "0":
        print("\n>>> Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break
    else:
        print("\n>>> Lựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 4.")