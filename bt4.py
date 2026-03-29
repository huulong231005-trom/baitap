# Bài 4: Kiểm tra số chia hết cho 2 hoặc cho 3

# Nhập số nguyên dương từ bàn phím
n = int(input("Nhập một số nguyên dương: "))

# Kiểm tra điều kiện số dương
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    # Kiểm tra chia hết cho 2 và/hoặc 3
    chia_het_2 = (n % 2 == 0)
    chia_het_3 = (n % 3 == 0)
    
    # Xuất kết quả
    print(f"\nSố {n}:")
    
    if chia_het_2 and chia_het_3:
        print(f"- {n} chia hết cho cả 2 và 3")
    elif chia_het_2:
        print(f"- {n} chia hết cho 2")
    elif chia_het_3:
        print(f"- {n} chia hết cho 3")
    else:
        print(f"- {n} không chia hết cho 2 và cũng không chia hết cho 3")
        