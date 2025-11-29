import random
matrix = []
#Tạo một ma trận 3x3 với giá trị ngẫu nhiên từ 1 đến 10.
def create_list():
    # cách 1: matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(10)]
    # cách 2:
    for i in range(3):
        arr = [] #lưu từng hàng
        for j in range(3):
            arr.append(random.randint(1,10))
        matrix.append(arr)

def display_list():
    print("-----Matrix-----")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=" ")
        print()

def diagonal():
    sum = 0
    for i in range(3):
        sum += matrix[i][i]
    return sum

def max_value():
    sum = 0
    for i in range(3):
        sum += matrix[i][i]
create_list()
display_list()