while True:
    print("\n===== MENU =====")
    print("1. Bài 1 - Tính tổng")
    print("2. Bài 2 - Tính tích")
    print("3. Bài 3 - Tách chẵn lẻ")
    print("4. Bài 4 - Lấy phần tử")
    print("5. Bài 5 - Thêm phần tử")
    print("6. Bài 6 - Chưa có đề")
    print("7. Bài 7 - Xử lý phần tử trùng")
    print("8. Bài 8 - Tìm số lớn nhất")
    print("9. Bài 9 - Tìm số nhỏ nhất")
    print("10. Bài 10 - Copy list")
    print("0. Thoát")

    chon = input("Nhập lựa chọn: ")

    # ===== BÀI 1 =====
    if chon == "1":
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tong = 0
        for i in lst:
            tong += i
        print("Kết quả:", tong)

    # ===== BÀI 2 =====
    elif chon == "2":
        lst = [1, 2, 3, 4, 5]
        tich = 1
        for i in lst:
            tich *= i
        print("Kết quả:", tich)

    # ===== BÀI 3 =====
    elif chon == "3":
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        chan = []
        le = []

        for i in lst:
            if i % 2 == 0:
                chan.append(i)
            else:
                le.append(i)

        print("Số chẵn:", chan)
        print("Số lẻ:", le)

    # ===== BÀI 4 =====
    elif chon == "4":
        lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        new = lst[2:4]
        print("Kết quả:", new)

    # ===== BÀI 5 =====
    elif chon == "5":
        lst = ['zero', 'three']
        lst.insert(1, 'one')
        lst.insert(2, 'two')
        print("Kết quả:", lst)

    # ===== BÀI 6 =====
    elif chon == "6":
        print("Bài 6: Chưa có đề trong ảnh.")

    # ===== BÀI 7 =====
    elif chon == "7":
        lst = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

        print("1. Loại bỏ tất cả phần tử trùng")
        print("2. Với phần tử trùng chỉ giữ lại 1 phần tử")
        chon7 = input("Chọn cách làm: ")

        if chon7 == "1":
            new = []
            for i in lst:
                if lst.count(i) == 1:
                    new.append(i)
            print("Kết quả:", new)

        elif chon7 == "2":
            new = []
            for i in lst:
                if i not in new:
                    new.append(i)
            print("Kết quả:", new)

        else:
            print("Chọn sai.")

    # ===== BÀI 8 =====
    elif chon == "8":
        lst = [11, 2, 23, 45, 6, 9]
        print("Số lớn nhất là:", max(lst))

    # ===== BÀI 9 =====
    elif chon == "9":
        lst = [11, 2, 23, 45, 6, 9]
        print("Số nhỏ nhất là:", min(lst))

    # ===== BÀI 10 =====
    elif chon == "10":
        lst = [11, 2, 23, 45, 6, 9]
        new = lst.copy()
        print("List mới:", new)

    elif chon == "0":
        print("Thoát chương trình")
        break

    else:
        print("Sai lựa chọn")