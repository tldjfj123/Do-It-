def judge(n) :
    if n > 0 :
        print("이 수는 양수입니다.")
    elif n < 0 :
        print("이 수는 음수입니다.")
    else :
        print("이 수는 0입니다.")

num = int(input("정수를 입력하세요 : "))

judge(num)