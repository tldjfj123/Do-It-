print("a부터 b까지 정수의 합을 구합니다.")
a = int(input("정수 a를 입력하세요 : "))
b = int(input("정수 b를 입력하세요 : "))

if a > b :
    a, b = b, a
    
sum = 0

if a == b :
    for i in range(a, b+1) :
        sum += i
    print("{} = {}".format(a, sum))
else :
    print("{}".format(a), end = "")
    sum += a
    for j in range(a+1, b+1) :
        sum += j
        print(" + {}".format(j), end = "")
    print(" = {}".format(sum))        