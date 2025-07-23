class Student :

    def __init__(self, name):
        self.name = name

    
    # def __str__(self) :
    #     return f'이름: {self.name}'
    # --> 마지막에 print(s1) 으로 값 구하기 가능
        

class GraduateStudent(Student) :
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def __str__(self):
        return f'이름: {self.name}, 전공: {self.major}'
    
s1 = Student('홍길동')
s2 = GraduateStudent('이순신', '컴퓨터')

print("이름:", s1.name)
print(s2)