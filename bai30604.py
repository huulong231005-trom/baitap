_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

temp_list = []
for x in _tuple:
    # Gợi ý dùng hàm count: nếu phần tử chưa có trong danh sách tạm thì mới thêm vào
    if temp_list.count(x) == 0: 
        # (Trong thực tế, người ta thường dùng 'if x not in temp_list:' cho tối ưu)
        temp_list.append(x)

_new_tuple = tuple(temp_list)

print("Bài 3 - _new_tuple:", _new_tuple)
# Kết quả: ('ab', 'b', 'e', 'c', 'd')