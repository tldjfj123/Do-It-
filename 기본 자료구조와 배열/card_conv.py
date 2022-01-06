def card_conv(x : int, r : int) -> str :
    d = ''
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    while x > 0 :
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

if __name__ == "__main__" :
    print("10진수를 n진수로 변환합니다.")
    
    while 1 :
        while 1 :
            no = int(input("변환할 값으로 음이 아닌 정수를 입력하세요. : "))
            if no > 0 :
                break
        
        while 1 :
            cd = int(input("어떤 진수로 변환할까요? : "))
            if 2 <= cd <= 36 :
                break
            
        print(f"{cd}진수로는 {card_conv(no, cd)}입니다.")
        
        retry = input("한번 더 변환할까요?(Y = 예 / N = 아니요) : ")
        if retry in {"N", "n"} :
            break