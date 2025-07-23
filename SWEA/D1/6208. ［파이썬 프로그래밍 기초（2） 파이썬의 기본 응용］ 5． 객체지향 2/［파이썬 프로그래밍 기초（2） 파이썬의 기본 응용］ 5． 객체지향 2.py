class Korean :
    def __init__(self, Nationality):
        self.nation = Nationality
        print(Nationality)


my_nationality = Korean('대한민국')

print(my_nationality.nation)