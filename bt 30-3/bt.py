def bai1():
    print("\n--- Bài 1 ---")
    n = int(input("Nhập n: "))
    for i in range(1, n):
        print(f"{2 * i} = 2 * {i}")


def bai2():
    print("\n--- Bài 2 ---")
    n = int(input("Nhập n: "))
    if n > 10:
        print("Số nhập vào phải bé hơn 10")
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)


def bai3():
    print("\n--- Bài 3 ---")
    for i in range(80, 101):
        if i % 2 == 0 and i % 3 == 0:
            print(i)


def bai4():
    print("\n--- Bài 4 ---")
    n = int(input("Nhập n (n < 20): "))
    if n >= 20:
        print("Vui lòng nhập số nhỏ hơn 20")
    else:
        for i in range(1, n + 1):
            if i % 5 == 0 or i % 7 == 0:
                print(i)


def menu():
    while True:
        print("\n" + "=" * 30)
        print("        MENU CHƯƠNG TRÌNH")
        print("=" * 30)
        print("1. Bài 1 - Tích của 2 với các số nhỏ hơn n")
        print("2. Bài 2 - Số chẵn từ 1 đến n (n <= 10)")
        print("3. Bài 3 - Số chia hết cho 2 và 3 trong khoảng 80-100")
        print("4. Bài 4 - Số chia hết cho 5 hoặc 7 từ 1 đến n (n < 20)")
        print("0. Thoát chương trình")
        print("-" * 30)

        choice = input("Mời bạn chọn (0-4): ")

        if choice == "1":
            bai1()
        elif choice == "2":
            bai2()
        elif choice == "3":
            bai3()
        elif choice == "4":
            bai4()
        elif choice == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình! Tạm biệt!")
            break
        else:
            print("\nLựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 4.")

        input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    menu()