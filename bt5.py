# Bài 5: Giải phương trình bậc 2: ax² + bx + c = 0

import math

# Nhập các hệ số
print("Giải phương trình bậc 2: ax² + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Xử lý trường hợp a = 0
if a == 0:
    print("\nĐây là phương trình bậc nhất (a = 0)")
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print(f"Phương trình có 1 nghiệm: x = {x:.2f}")
else:
    # Tính delta
    delta = b*b - 4*a*c
    
    print(f"\nDelta = {b}² - 4×{a}×{c} = {delta:.2f}")
    
    # Xét các trường hợp của delta
    if delta < 0:
        print("Phương trình vô nghiệm (Delta < 0)")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x₁ = x₂ = {x:.2f}")
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt:")
        print(f"  x₁ = {x1:.2f}")
        print(f"  x₂ = {x2:.2f}")