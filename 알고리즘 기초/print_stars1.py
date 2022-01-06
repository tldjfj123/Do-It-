print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요? : "))
c = int(input("몇 개마다 줄바꿈할까요? : "))

for i in range(n) :
    print("*", end = "")
    if i % c == c - 1 :
        print()
