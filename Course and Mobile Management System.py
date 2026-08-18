class Course:
    def __init__(self,course_name,duration,fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

    def Course_Category(self):
        if self.duration <=1:
            return "Short term course category"
        else:
            return "Long term course category "

    def Display(self):
        print(f"{self.course_name:<20} {self.duration:<18} {self.fees:<13} {self.Course_Category()}")

class Institute:
    def __init__(self,name):
        self.name = name
        self.courses =[]


    def Add_courses(self,course_name,duration,fees):
        course= Course(course_name,duration,fees)
        self.courses.append(course)
        print(f"Course added successfully: {course_name} -{duration}(in years)")

    def display(self):
        print(f"========== {self.name} =========")
        print(f"{'Course':<20} {'Duration(years)':<18} {'Fees':<13} {'Category'}")
        for cour in self.courses:
            cour.Display()

institute = Institute("MIT ADT UNIVERSITY")
institute.Add_courses("BTech in CSE",4,1272000)
institute.Add_courses("IBM Data science",0.3,6000)
institute.Add_courses("BBA",3,900000)

institute.display()

#Output
'''
Course added successfully: BTech in CSE -4(in years)
Course added successfully: IBM Data science -0.3(in years)
Course added successfully: BBA -3(in years)
========== MIT ADT UNIVERSITY =========
Course               Duration(years)    Fees          Category
BTech in CSE         4                  1272000       Long term course category 
IBM Data science     0.3                6000          Short term course category
BBA                  3                  900000        Long term course category
'''


# Mobile Management System
class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def Mob_Category(self):
        if self.price >=60000:
            return "Premium Category"
        elif self.price >=25000 and self.price<60000:
            return "Mid - range category"
        else:
            return "Budget"

    def Display(self):
        print(f"{self.brand:<10} {self.model:<15} {self.price:<12} {self.Mob_Category()}")

class Store:
    def __init__(self,name):
        self.name = name
        self.mobiles =[]


    def Add_mobiles(self,brand,model,price):
        mobile = Mobile(brand,model,price)
        self.mobiles.append(mobile)
        print(f"Mobile added successfully: {brand} {model}")

    def display(self):
        print(f"========== {self.name} =========")
        print(f"{'Brand':<10} {'Model':<15} {'Price':<12} {'Category'}")
        for mob in self.mobiles:
            mob.Display()

store = Store("Arnav mobile store")
store.Add_mobiles("Apple","Iphone 17 pro",95000)
store.Add_mobiles("samsung","F23",35000)
store.Add_mobiles("Mototrola","g57 power",19000)

store.display()


# Output
'''Mobile added successfully: Apple Iphone 17 pro
Mobile added successfully: samsung F23
Mobile added successfully: Mototrola g57 power
========== Arnav mobile store =========
Brand      Model           Price        Category
Apple      Iphone 17 pro   95000        Premium Category
samsung    F23             35000        Mid - range category
Mototrola  g57 power       19000        Budget'''
