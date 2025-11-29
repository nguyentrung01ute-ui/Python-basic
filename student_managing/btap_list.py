
ds_Students = [] #ds chứa các infor của sinh viên

#Cho phép người dùng nhập thông tin sinh viên (mã SV, tên, điểm) và thêm vào danh sách.
def nhap():
    mssv = int(input("Enter Student Number: "))
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    ds_Students.append([mssv, name, score])

    print("add to success!")

#Hiển thị danh sách sinh viên
def disPlay():
    if not ds_Students:
        print("Student list empty!")
        return
    print("Below is the list of students")

    for student in ds_Students:
        print(student)

#Sắp xếp danh sách theo điểm giảm dần.
def sortStudentsbyscore():
    ds_Students.sort(key=lambda x: x[2], reverse=True)
    print("the list of students sorted by score")

#Tìm và xóa sinh viên theo mã SV.
def find_and_delete():
    mssv = int(input("Enter Student Number that you want to delete: "))
    for student in ds_Students:
        if student[0] == mssv:
            ds_Students.remove(student)
            print("student deleted successfully!")
            return
    print("Student number not exist")

#Tính điểm trung bình của lớp.
def averageScore() -> float:
    average = 0.0
    for student in ds_Students:
        average += student[2]

    return average/len(ds_Students)

#Hiển thị danh sách sinh viên có điểm trên trung bình.
def disPlayconditions():
    if not ds_Students:
        print("Student list empty!")
        return
    average = averageScore()
    check = False
    for student in ds_Students:
        if student[2] >= average:
            print(f"MSSV: {student[0]}, Tên: {student[1]}, Điểm: {student[2]}")
            check = True

    if not check:
        print("No student has a score above average.")

while True:
    print("--------Options--------")
    print("1. Nhập thông tin sinh viên")
    print("2. Hiển thị danh sách sinh viên.")
    print("3. Sắp xếp danh sách theo điểm giảm dần")
    print("4. Tìm và xóa sinh viên theo mã SV")
    print("5. Tính điểm trung bình của lớp")
    print("6. Hiển thị danh sách sinh viên có điểm trên trung bình.")
    print("7. Hủy")

    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 7:
        print("invalid choice")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        nhap()
    elif choice == 2:
        disPlay()
    elif choice == 3:
        sortStudentsbyscore()
    elif choice == 4:
        find_and_delete()
    elif choice == 5:
        print("điểm trung bình cuả lớp là: " + str(averageScore()))
    elif choice == 6:
        disPlayconditions()
    else:
        print("Bye!")
        break

