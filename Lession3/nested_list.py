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
    for score in scores:
        if score > scores[0]:
            break
    for student in students:
        if student[1] == score:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)

    
    