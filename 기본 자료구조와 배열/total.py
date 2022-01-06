print("학생 그룹 점수의 합계와 평균을 구합니다.")

score = []
for i in range(1, 6) :
    s = int(input("{}번 학생의 점수를 입력하세요. : ".format(i)))
    score.append(s)

print("합계는 {}점 입니다.".format(sum(score)))
print("평균은 {}점 입니다.".format(sum(score) / len(score)))