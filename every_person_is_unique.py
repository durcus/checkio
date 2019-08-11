"""
 Вам необходимо создать класс Person, а также несколько методов для работы с его экземплярами. Описание класса смотрите далее.

class Person(first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')

Возвращает новый экземпляр класса Person c именем и фамилией [first_name, last_name], датой рождения - birth_date (в формате 'dd.mm.yyyy'), текущим местом работы - job, количеством проработанных лет - working_years, средней зарплатой за весь период работы - salary (сумма в месяц), страной и городом проживания - [country, city] и полом - gender. Параметр gender может принимать значения 'male' или 'female'. Если этот параметр не задан, то значение по умолчанию - 'unknown'.

Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’) ==

Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’)


Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’) ==

Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’, ‘unknown’)


name()

Возвращает полное имя (имя и фамилию, разделенные пробелом).

Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).name() == ‘John Smith’



age()

Возвращает возраст человека - количество полных прожитых лет. (Считайте текущим днем 01.01.2018)

Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).age() == 38

work()

Возвращает род занятий человека в предложении вида: ‘He is a ...’ (если male) ‘She is a ...’ (female) ‘Is a ...’ (unknown) В зависимости того, какой пол человека задан (м/ж) или, если пол неопределен - возвращает без указания пола.

Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).work() == ‘Is a designer’

money()

Возвращает количество денег, заработанное за весь период работы. Сумму следует выводить в формате xx xxx … - разбивая каждых 3 разряда пробелами. Например: ‘10 568’ ‘1 051 422’

Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648 000’

home()

Возвращает страну и город проживания в формате: ‘Lives in city, country’

Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).home() == ‘Lives in Vienna, Austria’


В этом задании все входные данные коректны, и проверку значений можно не выполнять.

Входные данные: операторы и выражения, использующие класс Person.

Выходные данные: поведение экземпляра как описано выше.

Как это используется: Работа с классами и объектно-ориентированным программированием - более высокий уровень мастерства, которым следует овладеть, чтобы иметь возможность использовать Python в полной мере.

Предусловие: Все данные корректны.
"""


class Person():

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        if self.birth_date[:5] != '01.01':
            if int(self.birth_date[-4:]) < 2000:
                self.age = 2000 - int(self.birth_date[-4:]) + 17
                return self.age
            else:
                self.age = 2017 - int(self.birth_date[-4:])
                return self.age
        else:
            if int(self.birth_date[-4:]) < 2000:
                self.age = 2000 - int(self.birth_date[-4:]) + 18
                return self.age
            else:
                self.age = 2018 - int(self.birth_date[-4:])
                return self.age

    def work(self):
        if self.gender == 'male':
            return 'He is a ' + self.job
        elif self.gender == 'female':
            return 'She is a ' + self.job
        else:
            return 'Is a ' + self.job

    def money(self):
        self.money = str(self.working_years * 12 * self.salary)
        l = []
        for i in range(-1, -len(self.money) - 1, -3):
            l.append(self.money[i - 2:i] + self.money[i])
        l.reverse()
        return " ".join(map(str, l))

    def home(self):
        return 'Lives in ' + self.city + ', ' + self.country


print(Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600,
             'Canada', 'Vancouver', 'male').name() == 'John Smith')
print(Person('John', 'Smith', '19.09.1979', 'welder', 15,
             3600, 'Canada', 'Vancouver', 'male').age() == 38)
print(Person('John', 'Smith', '19.09.2002', 'welder', 15,
             3600, 'Canada', 'Vancouver', 'male').age() == 15)
print(Person('Hanna Rose', 'May', '05.12.1995', 'designer',
             2.2, 2150, 'Austria', 'Vienna').work() == 'Is a designer')
print(Person('Hanna Rose', 'May', '05.12.1995', 'designer',
             2.2, 2150, 'Austria', 'Vienna', 'female').work() == 'She is a designer')
Person('John', 'Smith', '19.09.1979', 'welder', 15,
       3600, 'Canada', 'Vancouver', 'male').money()
print(Person('Hanna Rose', 'May', '05.12.1995', 'designer', 2.2,
             2150, 'Austria', 'Vienna').home() == 'Lives in Vienna, Austria')

p1 = Person("John", "Smith", "19.09.1979", "welder",
            15, 3600, "Canada", "Vancouver", "male")
p2 = Person("Hanna Rose", "May", "05.12.1995",
            "designer", 2.2, 2150, "Austria", "Vienna")
print(p1.name() == "John Smith", "Name")
print(p1.age() == 38, "Age")
print(p2.work() == "Is a designer", "Job")
print(p1.money() == "648 000", "Money")
print(p2.home() == "Lives in Vienna, Austria", "Home")

print(Person('Adam', 'Greene', '24.12.1961', 'director',
             36, 11000, 'England', 'London', 'male').money() == '4 752 000')
