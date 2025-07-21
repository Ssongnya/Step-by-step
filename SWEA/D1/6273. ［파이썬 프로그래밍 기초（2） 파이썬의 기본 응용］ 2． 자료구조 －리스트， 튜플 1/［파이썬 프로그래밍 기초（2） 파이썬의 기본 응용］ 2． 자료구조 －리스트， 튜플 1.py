#리스트, 튜플 연습문제

stu_1 = (90, 80)
stu_2 = (85, 75)
stu_3 = (90, 100)

lst = [stu_1, stu_2, stu_3]

for i in range(3):
    print("%d번 학생의 총점은 %d점이고, 평균은 %.1f입니다." % (i+1, sum(lst[i]), sum(lst[i])/2))
