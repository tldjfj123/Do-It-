print("1부터 n까지 정수의 합을 구합니다.")
n = int(input("n값을 입력하세요 : "))

sum = 0
for i in range(1, n+1) :
    sum += i
    
print("1부터 {}까지 정수의 합은 {}입니다.".format(n, sum))    
    