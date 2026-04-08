# Bảng mã quy định bởi từ điển
cipher_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

# 1. HÀM MÃ HÓA (Encode)
def encode_text(text, cipher):
    encoded = ""
    for char in text:
        # Nếu ký tự có trong từ điển thì lấy mã tương ứng, nếu không có thì giữ nguyên
        encoded += cipher.get(char, char) 
    return encoded

# 2. HÀM GIẢI MÃ (Decode)
def decode_text(text, cipher):
    # Tạo một từ điển đảo ngược (đổi value thành key, key thành value)
    reverse_cipher = {v: k for k, v in cipher.items()}
    
    decoded = ""
    for char in text:
        decoded += reverse_cipher.get(char, char)
    return decoded

# --- Chạy thử ---
van_ban_goc = "bad cat"
print("\n--- Luyện tập 1.8 ---")
print("Văn bản gốc:", van_ban_goc)

van_ban_ma_hoa = encode_text(van_ban_goc, cipher_dict)
print("Sau khi mã hóa:", van_ban_ma_hoa) 
# Kết quả: @!$ #!t

van_ban_giai_ma = decode_text(van_ban_ma_hoa, cipher_dict)
print("Sau khi giải mã:", van_ban_giai_ma)
# Kết quả: bad cat