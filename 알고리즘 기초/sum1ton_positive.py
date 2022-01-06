print("1부터 n까지 정수의 합을 구합니다.")

while 1 :
    n = int(input("n의 값을 입력하세요. : "))
    if n > 0 :
        break

sum = 0
i = 1

for i in range(1, n+1) :
    sum += i
    i += 1

print("1부터 {}까지 정수의 합은 {}입니다.".format(n, sum))