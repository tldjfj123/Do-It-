counter = 0

# for else : for문이 완전 실행 되면 else 부분 실행 됨.
for n in range(2, 1001) :
    for i in range(2, n) :
        counter += 1
        if n % i == 0 :
            break
    else :
        print(n)
            
print(f"나눗셈을 실행한 횟수 : {counter}")