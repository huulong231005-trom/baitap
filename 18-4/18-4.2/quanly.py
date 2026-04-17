class QuanLyCuaHang:
    def __init__(self):
        # Dữ liệu lưu trữ dạng Dictionary để dễ dàng tìm kiếm qua Mã (ID)
        self.ds_mat_hang = {}  # {ma_mh: {'ten': '', 'nguon_goc': '', 'don_gia': 0}}
        self.ds_khach_hang = {} # {ma_kh: {'ten': '', 'dia_chi': '', 'sdt': ''}}
        self.ds_don_hang = {}   # {ma_dh: {'ma_kh': '', 'chi_tiet': [{'ma_mh': '', 'so_luong': 0}]}}

    # ==========================================
    # 1. QUẢN LÝ THÔNG TIN MẶT HÀNG
    # ==========================================
    def hien_thi_mat_hang(self):
        print("\n--- DANH SÁCH MẶT HÀNG ---")
        if not self.ds_mat_hang:
            print("Chưa có mặt hàng nào.")
            return
        print(f"{'Mã MH':<10} | {'Tên mặt hàng':<20} | {'Nguồn gốc':<15} | {'Đơn giá':<15}")
        print("-" * 65)
        for ma, info in self.ds_mat_hang.items():
            print(f"{ma:<10} | {info['ten']:<20} | {info['nguon_goc']:<15} | {info['don_gia']:<15}")

    def them_mat_hang(self):
        ma_mh = input("Nhập mã mặt hàng: ")
        if ma_mh in self.ds_mat_hang:
            print("Mã mặt hàng đã tồn tại!")
            return
        ten_mh = input("Nhập tên mặt hàng: ")
        nguon_goc = input("Nhập nguồn gốc: ")
        don_gia = float(input("Nhập đơn giá: "))
        self.ds_mat_hang[ma_mh] = {'ten': ten_mh, 'nguon_goc': nguon_goc, 'don_gia': don_gia}
        print("Thêm mặt hàng thành công!")

    def sua_mat_hang(self):
        ma_mh = input("Nhập mã mặt hàng cần sửa: ")
        if ma_mh not in self.ds_mat_hang:
            print("Không tìm thấy mặt hàng!")
            return
        print("Nhập thông tin mới (để trống nếu không muốn đổi):")
        ten = input(f"Tên mới ({self.ds_mat_hang[ma_mh]['ten']}): ")
        nguon_goc = input(f"Nguồn gốc mới ({self.ds_mat_hang[ma_mh]['nguon_goc']}): ")
        gia_str = input(f"Đơn giá mới ({self.ds_mat_hang[ma_mh]['don_gia']}): ")

        if ten: self.ds_mat_hang[ma_mh]['ten'] = ten
        if nguon_goc: self.ds_mat_hang[ma_mh]['nguon_goc'] = nguon_goc
        if gia_str: self.ds_mat_hang[ma_mh]['don_gia'] = float(gia_str)
        print("Sửa mặt hàng thành công!")

    def xoa_mat_hang(self):
        ma_mh = input("Nhập mã mặt hàng cần xoá: ")
        if self.ds_mat_hang.pop(ma_mh, None):
            print("Xoá mặt hàng thành công!")
        else:
            print("Không tìm thấy mặt hàng!")

    def tim_kiem_mat_hang(self):
        tu_khoa = input("Nhập mã, tên hoặc nguồn gốc để tìm: ").lower()
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        found = False
        for ma, info in self.ds_mat_hang.items():
            if tu_khoa in ma.lower() or tu_khoa in info['ten'].lower() or tu_khoa in info['nguon_goc'].lower():
                print(f"Mã: {ma} | Tên: {info['ten']} | Nguồn gốc: {info['nguon_goc']} | Giá: {info['don_gia']}")
                found = True
        if not found: print("Không tìm thấy kết quả nào.")

    # ==========================================
    # 2. QUẢN LÝ THÔNG TIN KHÁCH HÀNG
    # ==========================================
    def hien_thi_khach_hang(self):
        print("\n--- DANH SÁCH KHÁCH HÀNG ---")
        if not self.ds_khach_hang:
            print("Chưa có khách hàng nào.")
            return
        print(f"{'Mã KH':<10} | {'Tên khách hàng':<20} | {'Địa chỉ':<20} | {'SĐT':<15}")
        print("-" * 75)
        for ma, info in self.ds_khach_hang.items():
            print(f"{ma:<10} | {info['ten']:<20} | {info['dia_chi']:<20} | {info['sdt']:<15}")

    def them_khach_hang(self):
        ma_kh = input("Nhập mã khách hàng: ")
        if ma_kh in self.ds_khach_hang:
            print("Mã khách hàng đã tồn tại!")
            return
        ten_kh = input("Nhập tên khách hàng: ")
        dia_chi = input("Nhập địa chỉ: ")
        sdt = input("Nhập số điện thoại: ")
        self.ds_khach_hang[ma_kh] = {'ten': ten_kh, 'dia_chi': dia_chi, 'sdt': sdt}
        print("Thêm khách hàng thành công!")

    def sua_khach_hang(self):
        ma_kh = input("Nhập mã KH cần sửa: ")
        if ma_kh not in self.ds_khach_hang:
            print("Không tìm thấy khách hàng!")
            return
        print("Nhập thông tin mới (để trống nếu không muốn đổi):")
        ten = input(f"Tên mới ({self.ds_khach_hang[ma_kh]['ten']}): ")
        dia_chi = input(f"Địa chỉ mới ({self.ds_khach_hang[ma_kh]['dia_chi']}): ")
        sdt = input(f"SĐT mới ({self.ds_khach_hang[ma_kh]['sdt']}): ")

        if ten: self.ds_khach_hang[ma_kh]['ten'] = ten
        if dia_chi: self.ds_khach_hang[ma_kh]['dia_chi'] = dia_chi
        if sdt: self.ds_khach_hang[ma_kh]['sdt'] = sdt
        print("Sửa khách hàng thành công!")

    def xoa_khach_hang(self):
        ma_kh = input("Nhập mã KH cần xoá: ")
        if self.ds_khach_hang.pop(ma_kh, None):
            print("Xoá khách hàng thành công!")
        else:
            print("Không tìm thấy khách hàng!")

    def tim_kiem_khach_hang(self):
        tu_khoa = input("Nhập mã, tên, địa chỉ hoặc SĐT để tìm: ").lower()
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        found = False
        for ma, info in self.ds_khach_hang.items():
            if tu_khoa in ma.lower() or tu_khoa in info['ten'].lower() or tu_khoa in info['dia_chi'].lower() or tu_khoa in info['sdt'].lower():
                print(f"Mã KH: {ma} | Tên: {info['ten']} | Đ/c: {info['dia_chi']} | SĐT: {info['sdt']}")
                found = True
        if not found: print("Không tìm thấy kết quả nào.")

    # ==========================================
    # 3. QUẢN LÝ ĐƠN HÀNG
    # ==========================================
    def tinh_tong_tien(self, ma_dh):
        tong = 0
        if ma_dh in self.ds_don_hang:
            for item in self.ds_don_hang[ma_dh]['chi_tiet']:
                ma_mh = item['ma_mh']
                if ma_mh in self.ds_mat_hang:
                    tong += item['so_luong'] * self.ds_mat_hang[ma_mh]['don_gia']
        return tong

    def hien_thi_don_hang(self):
        print("\n--- DANH SÁCH ĐƠN HÀNG ---")
        if not self.ds_don_hang:
            print("Chưa có đơn hàng nào.")
            return
        print(f"{'Mã ĐH':<10} | {'Mã KH':<10} | {'Tên khách hàng':<20} | {'Tổng tiền':<15}")
        print("-" * 65)
        for ma_dh, info in self.ds_don_hang.items():
            ten_kh = self.ds_khach_hang.get(info['ma_kh'], {}).get('ten', 'Không xác định')
            tong_tien = self.tinh_tong_tien(ma_dh)
            print(f"{ma_dh:<10} | {info['ma_kh']:<10} | {ten_kh:<20} | {tong_tien:<15}")

    def them_don_hang(self):
        ma_dh = input("Nhập mã đơn hàng: ")
        if ma_dh in self.ds_don_hang:
            print("Mã đơn hàng đã tồn tại!")
            return
        ma_kh = input("Nhập mã khách hàng: ")
        if ma_kh not in self.ds_khach_hang:
            print("Khách hàng không tồn tại! Vui lòng thêm khách hàng trước.")
            return

        chi_tiet = []
        while True:
            ma_mh = input("Nhập mã mặt hàng mua (hoặc gõ '0' để dừng): ")
            if ma_mh == '0': break
            if ma_mh not in self.ds_mat_hang:
                print("Mặt hàng không tồn tại!")
                continue
            so_luong = int(input(f"Nhập số lượng cho '{self.ds_mat_hang[ma_mh]['ten']}': "))
            chi_tiet.append({'ma_mh': ma_mh, 'so_luong': so_luong})

        self.ds_don_hang[ma_dh] = {'ma_kh': ma_kh, 'chi_tiet': chi_tiet}
        print("Thêm đơn hàng thành công!")

    def xoa_don_hang(self):
        ma_dh = input("Nhập mã ĐH cần xoá: ")
        if self.ds_don_hang.pop(ma_dh, None):
            print("Xoá đơn hàng thành công!")
        else:
            print("Không tìm thấy đơn hàng!")

    def tim_kiem_don_hang(self):
        tu_khoa = input("Nhập mã đơn hàng hoặc mã khách hàng để tìm: ").lower()
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        found = False
        for ma_dh, info in self.ds_don_hang.items():
            if tu_khoa in ma_dh.lower() or tu_khoa in info['ma_kh'].lower():
                print(f"Mã ĐH: {ma_dh} | Mã KH: {info['ma_kh']} | Tổng tiền: {self.tinh_tong_tien(ma_dh)}")
                found = True
        if not found: print("Không tìm thấy kết quả nào.")

    def chi_tiet_don_hang(self):
        ma_dh = input("Nhập mã hóa đơn để xem chi tiết: ")
        if ma_dh not in self.ds_don_hang:
            print("Không tìm thấy đơn hàng!")
            return
        
        info = self.ds_don_hang[ma_dh]
        ten_kh = self.ds_khach_hang.get(info['ma_kh'], {}).get('ten', 'N/A')
        
        print(f"\n--- CHI TIẾT ĐƠN HÀNG: {ma_dh} ---")
        print(f"Khách hàng: {ten_kh} (Mã: {info['ma_kh']})")
        print(f"{'Tên mặt hàng':<20} | {'Số lượng':<10} | {'Đơn giá':<15} | {'Thành tiền':<15}")
        print("-" * 65)
        
        tong_cong = 0
        for item in info['chi_tiet']:
            ma_mh = item['ma_mh']
            if ma_mh in self.ds_mat_hang:
                ten_mh = self.ds_mat_hang[ma_mh]['ten']
                don_gia = self.ds_mat_hang[ma_mh]['don_gia']
                sl = item['so_luong']
                thanh_tien = sl * don_gia
                tong_cong += thanh_tien
                print(f"{ten_mh:<20} | {sl:<10} | {don_gia:<15.0f} | {thanh_tien:<15.0f}")
        
        print("-" * 65)
        print(f"TỔNG CỘNG HÓA ĐƠN: {tong_cong:,.0f} VNĐ")


# ==========================================
# GIAO DIỆN MENU (CLI) CHÍNH
# ==========================================
def main():
    app = QuanLyCuaHang()
    
    # --- DỮ LIỆU MẪU ĐÃ ĐƯỢC THÊM SẴN ---
    app.ds_mat_hang = {
        'MH01': {'ten': 'Laptop Dell', 'nguon_goc': 'USA', 'don_gia': 15000000},
        'MH02': {'ten': 'Chuột Logitech', 'nguon_goc': 'China', 'don_gia': 500000},
        'MH03': {'ten': 'Bàn phím cơ', 'nguon_goc': 'VN', 'don_gia': 1200000}
    }
    
    # ĐÃ BỔ SUNG THÊM NHIỀU KHÁCH HÀNG HƠN
    app.ds_khach_hang = {
        'KH01': {'ten': 'Nguyễn Văn A', 'dia_chi': 'Hà Nội', 'sdt': '0901234567'},
        'KH02': {'ten': 'Trần Thị B', 'dia_chi': 'TP.HCM', 'sdt': '0988777666'},
        'KH03': {'ten': 'Lê Hoàng C', 'dia_chi': 'Đà Nẵng', 'sdt': '0912345678'},
        'KH04': {'ten': 'Phạm Thị D', 'dia_chi': 'Hải Phòng', 'sdt': '0923456789'},
        'KH05': {'ten': 'Vũ Văn E', 'dia_chi': 'Cần Thơ', 'sdt': '0934567890'},
        'KH06': {'ten': 'Hoàng Bích F', 'dia_chi': 'Nha Trang', 'sdt': '0945678901'},
        'KH07': {'ten': 'Đặng Ngọc G', 'dia_chi': 'Huế', 'sdt': '0956789012'},
        'KH08': {'ten': 'Bùi Thanh H', 'dia_chi': 'Vũng Tàu', 'sdt': '0967890123'},
        'KH09': {'ten': 'Đỗ Hữu I', 'dia_chi': 'Quảng Ninh', 'sdt': '0978901234'},
        'KH10': {'ten': 'Ngô Kim K', 'dia_chi': 'Bình Dương', 'sdt': '0989012345'}
    }

    app.ds_don_hang = {
        'DH01': {
            'ma_kh': 'KH01', 
            'chi_tiet': [
                {'ma_mh': 'MH01', 'so_luong': 1},
                {'ma_mh': 'MH02', 'so_luong': 2}
            ]
        },
        'DH02': {
            'ma_kh': 'KH02',
            'chi_tiet': [
                {'ma_mh': 'MH03', 'so_luong': 1},
                {'ma_mh': 'MH02', 'so_luong': 1}
            ]
        }
    }

    # --- MENU ĐIỀU HƯỚNG ---
    while True:
        print("\n" + "="*30)
        print("   PHẦN MỀM QUẢN LÝ CỬA HÀNG")
        print("="*30)
        print("1. Quản lý Mặt Hàng")
        print("2. Quản lý Khách Hàng")
        print("3. Quản lý Đơn Hàng")
        print("0. Thoát")
        
        chon_chinh = input("Chọn chức năng (0-3): ")
        
        if chon_chinh == '0':
            print("Cảm ơn bạn đã sử dụng phần mềm!")
            break
            
        elif chon_chinh == '1':
            while True:
                print("\n-- QUẢN LÝ MẶT HÀNG --")
                print("1. Hiển thị danh sách | 2. Thêm | 3. Sửa | 4. Xóa | 5. Tìm kiếm | 0. Trở lại")
                chon = input("Chọn: ")
                if chon == '1': app.hien_thi_mat_hang()
                elif chon == '2': app.them_mat_hang()
                elif chon == '3': app.sua_mat_hang()
                elif chon == '4': app.xoa_mat_hang()
                elif chon == '5': app.tim_kiem_mat_hang()
                elif chon == '0': break
                
        elif chon_chinh == '2':
            while True:
                print("\n-- QUẢN LÝ KHÁCH HÀNG --")
                print("1. Hiển thị danh sách | 2. Thêm | 3. Sửa | 4. Xóa | 5. Tìm kiếm | 0. Trở lại")
                chon = input("Chọn: ")
                if chon == '1': app.hien_thi_khach_hang()
                elif chon == '2': app.them_khach_hang()
                elif chon == '3': app.sua_khach_hang()
                elif chon == '4': app.xoa_khach_hang()
                elif chon == '5': app.tim_kiem_khach_hang()
                elif chon == '0': break
                
        elif chon_chinh == '3':
            while True:
                print("\n-- QUẢN LÝ ĐƠN HÀNG --")
                print("1. Hiển thị danh sách (có tổng tiền)")
                print("2. Thêm đơn hàng")
                print("3. Xóa đơn hàng")
                print("4. Tìm kiếm đơn hàng")
                print("5. Xem CHI TIẾT hóa đơn (Mặt hàng, SL, Giá, Thành tiền)")
                print("0. Trở lại")
                chon = input("Chọn: ")
                if chon == '1': app.hien_thi_don_hang()
                elif chon == '2': app.them_don_hang()
                elif chon == '3': app.xoa_don_hang()
                elif chon == '4': app.tim_kiem_don_hang()
                elif chon == '5': app.chi_tiet_don_hang()
                elif chon == '0': break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

# Chạy chương trình
if __name__ == "__main__":
    main()