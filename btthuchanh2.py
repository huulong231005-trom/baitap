import os

# ==================== BÀI 4 ====================
def bai4_luu_va_doc_thong_tin_ca_nhan():
    print("\n--- BÀI 4: Lưu và đọc thông tin cá nhân ---")
    ten_file = "setInfo.txt"
    
    # a) Nhập thông tin và lưu vào file
    print("\nNhập thông tin cá nhân của bạn:")
    ten = input("Họ và tên: ")
    tuoi = input("Tuổi: ")
    email = input("Email: ")
    skype = input("Skype: ")
    dia_chi = input("Địa chỉ: ")
    noi_lam_viec = input("Nơi làm việc: ")
    
    # Ghi thông tin vào file
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(f"Họ và tên: {ten}\n")
        f.write(f"Tuổi: {tuoi}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Skype: {skype}\n")
        f.write(f"Địa chỉ: {dia_chi}\n")
        f.write(f"Nơi làm việc: {noi_lam_viec}\n")
    
    print(f"\nĐã lưu thông tin vào file '{ten_file}' thành công!")
    
    # b) Đọc thông tin từ file và hiển thị
    print("\n--- Đọc thông tin từ file ---")
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print(noi_dung)
    except FileNotFoundError:
        print(f"Không tìm thấy file '{ten_file}'")

# ==================== BÀI 5 ====================
def bai5_dem_tu_trong_file():
    print("\n--- BÀI 5: Đếm số lượng xuất hiện của các từ trong file ---")
    ten_file = "demo_file2.txt"
    
    # Tạo file demo_file2.txt với nội dung yêu cầu
    noi_dung_file = 'Dem so luong tu xuat hien abc abc abc 12 12 it it eaut'
    
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung_file)
    print(f"Đã tạo file '{ten_file}' với nội dung: {noi_dung_file}")
    
    # Đọc file và đếm số lần xuất hiện của từng từ
    with open(ten_file, 'r', encoding='utf-8') as f:
        noi_dung = f.read()
    
    # Tách các từ (dùng split để tách theo khoảng trắng)
    cac_tu = noi_dung.split()
    
    # Đếm số lần xuất hiện
    dem_tu = {}
    for tu in cac_tu:
        if tu in dem_tu:
            dem_tu[tu] += 1
        else:
            dem_tu[tu] = 1
    
    # In kết quả
    print("\nKết quả đếm từ:")
    print(dem_tu)
    
    # In đẹp hơn (tùy chọn)
    print("\nChi tiết:")
    for tu, so_lan in sorted(dem_tu.items()):
        print(f"  '{tu}': {so_lan} lần")

# ==================== MAIN ====================
def main():
    print("CHƯƠNG TRÌNH THỰC HÀNH XỬ LÝ FILE (TIẾP)")
    print("=" * 45)
    
    while True:
        print("\nChọn bài tập muốn chạy:")
        print("4. Lưu và đọc thông tin cá nhân (setInfo.txt)")
        print("5. Đếm số lần xuất hiện của từ trong file")
        print("0. Thoát chương trình")
        
        chon = input("Nhập lựa chọn của bạn (0, 4, 5): ")
        
        if chon == "4":
            bai4_luu_va_doc_thong_tin_ca_nhan()
        elif chon == "5":
            bai5_dem_tu_trong_file()
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn 4, 5 hoặc 0.")

if __name__ == "__main__":
    main()