from typing import Any, Sequence

def bin_search(a : Sequence, key = Any) -> int :
    left = 0
    right = len(a)-1
    
    while 1 :
        center = left + right // 2
        if a[center] == key :
            return center
        elif a[center] < key :
            left = center + 1
        else :
            right = center - 1
        
        if left > right :
            break
    
    return -1

if __name__ == '__main__' :
    num = int(input("원소 수를 입력하세요. : "))
    x = [None] * num
    
    print("배열 데이터를 오름차순으로 입력하세요. :")
    
    x[0] = int(input('x[0] : '))
    
    for i in range(1, num) :
        while 1 :
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1] :
                break
    
    ky = int(input("검색할 값을 입력하세요. : "))
    
    idx = bin_search(x, ky)
    
    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')