# Chương trình tổng hợp cả 2 bài
import math

def bai4():
    print("\n" + "="*50)
    print("BÀI 4: KIỂM TRA SỐ CHIA HẾT CHO 2 HOẶC 3")
    print("="*50)
    
    try:
        n = int(input("Nhập một số nguyên dương: "))
        
        if n <= 0:
            print("❌ Vui lòng nhập số nguyên dương!")
        else:
            chia_het_2 = (n % 2 == 0)
            chia_het_3 = (n % 3 == 0)
            
            print(f"\n✅ Kết quả cho số {n}:")
            
            if chia_het_2 and chia_het_3:
                print(f"   {n} chia hết cho cả 2 và 3")
            elif chia_het_2:
                print(f"   {n} chia hết cho 2")
            elif chia_het_3:
                print(f"   {n} chia hết cho 3")
            else:
                print(f"   {n} không chia hết cho 2 và cũng không chia hết cho 3")
    except ValueError:
        print("❌ Lỗi: Vui lòng nhập số nguyên hợp lệ!")

def bai5():
    print("\n" + "="*50)
    print("BÀI 5: GIẢI PHƯƠNG TRÌNH BẬC 2")
    print("="*50)
    
    try:
        print("Phương trình: ax² + bx + c = 0")
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
        
        print(f"\n📐 Phương trình: {a}x² + {b}x + {c} = 0")
        
        if a == 0:
            print("\n⚠️ Đây là phương trình bậc nhất (a = 0)")
            if b == 0:
                if c == 0:
                    print("✅ Phương trình vô số nghiệm")
                else:
                    print("❌ Phương trình vô nghiệm")
            else:
                x = -c / b
                print(f"✅ Phương trình có 1 nghiệm: x = {x:.2f}")
        else:
            delta = b*b - 4*a*c
            print(f"\n📊 Delta = b² - 4ac = {b}² - 4×{a}×{c} = {delta:.2f}")
            
            if delta < 0:
                print("❌ Phương trình vô nghiệm (Delta < 0)")
            elif delta == 0:
                x = -b / (2*a)
                print(f"✅ Phương trình có nghiệm kép: x₁ = x₂ = {x:.2f}")
            else:
                sqrt_delta = math.sqrt(delta)
                x1 = (-b + sqrt_delta) / (2*a)
                x2 = (-b - sqrt_delta) / (2*a)
                print(f"✅ Phương trình có 2 nghiệm phân biệt:")
                print(f"   x₁ = ({-b} + √{delta:.2f}) / {2*a} = {x1:.2f}")
                print(f"   x₂ = ({-b} - √{delta:.2f}) / {2*a} = {x2:.2f}")
    except ValueError:
        print("❌ Lỗi: Vui lòng nhập số hợp lệ!")

def main():
    while True:
        print("\n" + "="*50)
        print("CHƯƠNG TRÌNH THỰC HÀNH")
        print("="*50)
        print("1. Bài 4 - Kiểm tra số chia hết cho 2 hoặc 3")
        print("2. Bài 5 - Giải phương trình bậc 2")
        print("3. Thoát")
        print("-"*50)
        
        choice = input("Chọn bài tập (1/2/3): ")
        
        if choice == '1':
            bai4()
        elif choice == '2':
            bai5()
        elif choice == '3':
            print("\n👋 Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("\n❌ Lựa chọn không hợp lệ! Vui lòng chọn 1, 2 hoặc 3.")
        
        input("\nNhấn Enter để tiếp tục...")

# Chạy chương trình
if __name__ == "__main__":
    main()