class Employee:
    rais_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first.strip().lower() + '_' + self.last.lower() + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return self.first + ' ' + self.last

    def rais_pay(self):
        self.pay = int(self.pay * self.rais_amount)
        return self.pay


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, lang_prog, courses):
        super().__init__(first, last, pay)
        self.lang_prog = lang_prog
        self.courses = courses

    def display_courses(self):
        html, python, *courses = self.courses
        return courses

    def rais_pay(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


dev1 = Developer('Mahmoud', "Elrasool", 20000, "Python", ['HTML', 'Python', 'Kotlin', 'Java'])
print(dev1.display_courses())
