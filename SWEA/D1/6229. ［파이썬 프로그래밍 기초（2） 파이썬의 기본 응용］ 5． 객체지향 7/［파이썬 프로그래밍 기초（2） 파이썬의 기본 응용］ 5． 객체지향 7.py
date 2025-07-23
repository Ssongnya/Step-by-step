class Person :
    def getGender(self) :
        return "Unknown"
    
class Male(Person):
    def getGender(self):
        return "Male"
    
class Female(Person):
    def getGender(self):
        return "Female"
    
Gender_is_male = Male()
Gender_is_female = Female()

print(Gender_is_male.getGender())
print(Gender_is_female.getGender())