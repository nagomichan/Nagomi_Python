if __name__ == '__main__':
    names = []
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    scores.sort()
    for i in scores:
        if i > scores[0]:
            second = i
            break
    for student in students:
        if student[1] == second:
            names.append(student[0])
    names.sort()
    for i in names:
        print(i)
