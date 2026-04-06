_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

# Duyệt qua từng phần tử, chỉ lấy những phần tử có số lần đếm (count) bằng 1
_new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)

print("Bài 2 - _new_tuple:", _new_tuple)
# Kết quả: ('b', 'c', 'd')