
ds_tuple = []
# yc 1 2 3
N = int(input("Nhập số lương sinh viên: "))
for i in range(N):
    #nhập thông tin trên một dòng
    infor = input(f"Input all information of sv{i+1} (ex: name age math eng): ")
    #tách chuỗi bởi space
    name, age, math, eng = infor.split()
    #thêm vào mảng
    ds_tuple.append((name, int(age), float(math), float(eng)))
student_tuple = tuple(ds_tuple)

#yc4
#sinh viên đầu tiên
print("First Student Information: ", student_tuple[0])
#sinh viên cuối cùng
print("Final Student Information: ", student_tuple[-1])
#3 sinh viên giữa (nếu đủ)
if len(student_tuple) >= 3:
    mid = len(student_tuple) // 2
    print("   3 sinh viên giữa:", student_tuple[mid-1 : mid+2])
else:
    print("Không đủ sinh viên để lấy 3 sinh viên giữa!")


'''Dùng unpacking để lấy:
+ name
+ và toàn bộ thông tin còn lại đưa vào 1 biến bằng *
'''
for student in student_tuple:
    (name, *other) = student
    print(name + ", " + str(other))

#Đếm số sinh viên có điểm toán = 8.5
count = 0
for student in student_tuple:
    if student[2] == 8.5:
        count += 1
print(count)

#Tìm vị trí đầu tiên của sinh viên tên “An”
i = 0
found = False
for student in student_tuple:
    if student[0] == "An":
        found = True
        break
    i = i + 1
if found:
    print("Vị trí của An là:", i)
else:
    print("Không tìm thấy sinh viên tên An")


#Thêm 1 tuple sinh viên mới vào danh sách
infor = input("Input all information of new sv (ex: name age math eng): ")
name, age, math, eng = infor.split()

# tạo thành một tuple **con**
new_student = (name, int(age), float(math), float(eng))

# nối vào tuple lớn
student_tuple = student_tuple + (new_student,)


#Xóa sinh viên thứ 3 (chuyển qua list → xóa → chuyển lại tuple)
if len(student_tuple) >= 3:
    tmp = list(student_tuple)
    tmp.pop(2)
    student_tuple = tuple(tmp)
    print("Đã xóa sinh viên thứ 3!")
else:
    print("Không đủ sinh viên để xóa!")

#Sắp xếp danh sách theo điểm toán tăng dần
student_tuple = tuple(sorted(student_tuple, key=lambda x: x[2])) #khi sorted nó sẽ trả về dạng list

#Kiểm tra xem “Tú” có trong danh sách không
names = [s[0] for s in student_tuple]

if "Tú" in names:
    print("Tú có trong danh sách")
else:
    print("Tú không có trong danh sách")
