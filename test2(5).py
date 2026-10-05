year = int(input("년도 입력: "))

if year % 400 == 0:
    print(f"{year}년은 윤년입니다")
elif year % 100 == 0:
    print(f"{year}년은 평년입니다")
elif year % 4 == 0:
    print(f"{year}년은 윤년입니다")
else:
    print(f"{year}년은 평년입니다")