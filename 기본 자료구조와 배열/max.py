from typing import Any, Sequence

def max_of(a : Sequence) -> Any :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]
    return maximum

if __name__ == '__main__' :
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수를 입력하세요 : "))
    x = [None] * num
    
    for i in range(num) :
        x[i] = int(input("x[{}]값을 입력하세요. : ".format(i)))
    
    print("최댓값은 {}입니다.".format(max_of(x)))