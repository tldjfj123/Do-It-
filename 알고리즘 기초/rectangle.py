n = int(input("직사각형의 넓이를 입력하세요 : "))

for i in range(1, n+1) :
    if i*i > n :
        break
    if n % i :
        continue
    print("{} X {}".format(i, n // i))
    

