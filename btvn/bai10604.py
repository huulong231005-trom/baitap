_tuple = ('a', 'b', 'd', 'e')

# Cách 1: Sử dụng cắt ghép (Slicing) - cách "Pythonic" nhất
_new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

# Cách 2: Chuyển sang list để dùng hàm insert
# temp_list = list(_tuple)
# temp_list.insert(2, 'c')
# _new_tuple = tuple(temp_list)

print("Bài 1 - _new_tuple:", _new_tuple)
# Kết quả: ('a', 'b', 'c', 'd', 'e')