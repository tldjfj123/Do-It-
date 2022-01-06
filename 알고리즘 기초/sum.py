print("a부터 b까지 정수의 합을 구합니다.")
a = int(input("정수 a를 입력하세요 : "))
b = int(input("정수 b를 입력하세요 : "))

if a > b :
    a, b = b, a

sum = 0

for i in range(a, b+1) :
    sum += i

print("{}부터 {}까지 정수의 합은 {}입니다.".format(a, b, sum))