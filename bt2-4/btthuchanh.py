import os

# ==================== BÀI 1 ====================
def bai1_doc_n_dong():
    print("\n--- BÀI 1: Đọc n dòng đầu tiên của file ---")
    ten_file = input("Nhập tên file cần đọc: ")
    try:
        n = int(input("Nhập số dòng n cần đọc: "))
        with open(ten_file, 'r', encoding='utf-8') as f:
            dong_dau = [next(f) for _ in range(n) if True]
            # Cách khác an toàn hơn
            # lines = f.readlines()[:n]
        # Cách an toàn hơn, tránh lỗi StopIteration
        with open(ten_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(min(n, len(lines))):
                print(f"Dòng {i+1}: {lines[i].rstrip()}")
    except FileNotFoundError:
        print(f"Không tìm thấy file '{ten_file}'")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ cho n")
    except Exception as e:
        print(f"Lỗi: {e}")

# ==================== BÀI 2 ====================
def bai2_ghi_va_hien_thi():
    print("\n--- BÀI 2: Ghi đoạn văn bản vào file và hiển thị ---")
    ten_file = input("Nhập tên file để ghi (ví dụ: output.txt): ")
    noi_dung = input("Nhập đoạn văn bản cần ghi vào file: ")
    
    # Ghi vào file
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
    print(f"Đã ghi nội dung vào file '{ten_file}' thành công!")
    
    # Hiển thị nội dung vừa ghi
    print("\nNội dung vừa ghi:")
    with open(ten_file, 'r', encoding='utf-8') as f:
        print(f.read())

# ==================== BÀI 3 ====================
def bai3_tao_va_doc_file():
    print("\n--- BÀI 3: Tạo file demo_file1.txt và đọc nội dung ---")
    
    # Tạo file với nội dung như yêu cầu
    ten_file = "demo_file1.txt"
    noi_dung = "Thưc \n hanh \n voi \n file\n IO\n"
    
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
    print(f"Đã tạo file '{ten_file}' với nội dung:")
    print(noi_dung)
    
    # a) Đọc và in nội dung trên một dòng
    print("\n3a) Nội dung file trên một dòng:")
    with open(ten_file, 'r', encoding='utf-8') as f:
        noi_dung_tren_mot_dong = f.read().replace('\n', ' ')
        print(noi_dung_tren_mot_dong)
    
    # b) Đọc và in nội dung theo từng dòng
    print("\n3b) Nội dung file theo từng dòng:")
    with open(ten_file, 'r', encoding='utf-8') as f:
        dong = 1
        for line in f:
            print(f"Dòng {dong}: {line.rstrip()}")  # rstrip() để bỏ ký tự xuống dòng
            dong += 1

# ==================== MAIN - CHẠY CHƯƠNG TRÌNH ====================
def main():
    print("CHƯƠNG TRÌNH THỰC HÀNH XỬ LÝ FILE")
    print("=" * 40)
    
    while True:
        print("\nChọn bài tập muốn chạy:")
        print("1. Đọc n dòng đầu tiên của file")
        print("2. Ghi đoạn văn bản vào file và hiển thị")
        print("3. Tạo file demo_file1.txt và đọc nội dung")
        print("0. Thoát chương trình")
        
        chon = input("Nhập lựa chọn của bạn (0-3): ")
        
        if chon == "1":
            bai1_doc_n_dong()
        elif chon == "2":
            bai2_ghi_va_hien_thi()
        elif chon == "3":
            bai3_tao_va_doc_file()
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 3.")

if __name__ == "__main__":
    main()