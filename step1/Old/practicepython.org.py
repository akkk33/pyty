class HundredYearsCounter():
    def __init__(self):
        age = int(input("Enter your age: "))
        if 100 > age > 0:
            remaining = 100 - age
            print("You'll be 100 years old after ", end = str(remaining))
        else:
            print("please input a valid value")


myAge = HundredYearsCounter()