# Note:
# 1. giới hạn bởi cặp ngoặc vuông
# 2. các phần tử của list cách nhau bởi dấu ,
# 3. List có thể chưa được mọi giá trị (int, string, float và list)
# 4. Cách khai báo một giá trị có kiểu dữ liệu là list:
#   a = [] (khai báo giá trị a là một list rỗng)
#   a = [1,2,3.0,"haha",["hihi", "huhu"]] (khai báo list a có 5 phần tử, 2 interger, 1 float , 1 tring và 1 list con 2 phần tử)
# 5. Các tính chất trong list:
#   a. Cộng 2 list
#   b. Nhân list với 1 số nguyên
#   c. Thêm 1 phần tử vào một vị trí xác định trong list bằng hàm insert(index,value)
#   d. Xóa 1 phần tử trong list và trả về phần tử đó bằng cách sử dụng hàm pop(index)
#   e. Xóa 1 phần tử trong list và không trả về kết quả bằng cách sử dụng hàm remove(value)
#   f. Đảo ngược các phần tử trong list bằng hàm
#   g. Sắp xếp tăng dần hoặc giảm dần các phần tử trong mảng bằng hàm sort(reverse=False) -> reverse=True giảm dần, reverse=False tăng dần
#######################################################

# Ví dụ
# 1. cộng list [1,2,4] với list ["a", "b", "c"]:
# kết quả trả về:
#   plus = [1, 2, 4, 'a', 'b', 'c']
plus = [1, 2, 4] + ["a", "b", "c"]

# 2. nhân list [1, 2, 3]
# kết quả trả về:
# [1,2,3,1,2,3]
mul = [1, 2, 3]*2  # nhân list

# 3. Thêm vào vị trí thứ 0 của list insert phần tử có giá trị "test"
# kết quả trả về:
#   insert = ["test", 1, 2, 3, 4]
insert = [1, 2, 3, 4]
insert.insert(0, "test")

# 4. Xóa phần tử thứ 3 ra khỏi list và trả về giá trị của phần tử thứ 3
# kết quả trả về:
#   pop = [1, 2, 3]
#   popResult = 4
pop = [1, 2, 3, 4]
popresult = pop.pop()

# 4. Xóa 1 phần tử trong list và không trả về kết quả
# kết quả trả về:
#   remove = [2, 3, 4]
remove = [1, 2, 3, 4]
remove.remove(1)

# 5. Đảo ngược các phần tử trong mảng
# kết quả trả về:
#   revert = [3, 2, 1]
revert = [1, 2, 3]
revert.reverse()

# 6. sắp xếp mảng 2 mảng trên bằng cách sử dụng hàm sort
# kết quả trả về:
#   sort1 = [3, 4, 5, 7]
#   sort2 = [7, 5, 4, 3]
sort1 = [4, 5, 3, 7]
sort1.sort()
sort2 = [4, 5, 3, 7]
sort2.sort(reverse=True)


# 7. Syntax tạo nhanh mảng sử dụng vòng lặp for
# kết quả trả về:
#   forList = [0, 2, 4, 6, 8]
forList = [i for i in range(10)]


a = []
a.append("maru")  # ["maru"]
a.append("nagomi")  # ["maru", "nagomi"]
a.append("agomi")  # ["maru", "nagomi", "agomi"]


a.sort()  # ["agomi", "maru", "nagomi"]
