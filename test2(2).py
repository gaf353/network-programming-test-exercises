
students = {}
while True:
    student_id = input("학번 입력 (종료: Fin): ")
    if student_id == "Fin":
        break
    name = input("이름 입력: ")
    students[student_id] = name
    print(students)

while True:
    query = input("학번 입력 (종료: Quit): ")
    if query == "Quit":
        break
    if query in students:
        print(students[query])
    else:
        print("not found!")