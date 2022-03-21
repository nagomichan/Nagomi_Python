if __name__ == '__main__':
    N = int(input())
    #cho mảng trả về là mảng rỗng
    result = []
    for i in range(N):
        # chuyển input đầu vào thành list split khoảng trắng
        # lis có thể có 1 2 3 phần tử, phần tử đầu tiên luôn là lệnh
        arr = input().split()
        if arr[0] == "insert":
            result.insert(int(arr[1]), int(arr[2]))
        elif arr[0] == "print":
            print(result)       