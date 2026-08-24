# Movie Collection Management System

class Movie:
    def __init__(self, movie_name, rating, ticket_price, category):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price
        self.category = category

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category:", self.category)
        print()


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Movie Details ---")
        for movie in self.movies:
            movie.display()


cinema = Cinema()

n = int(input("Enter number of movies: "))

for i in range(n):
    print("\nEnter details for Movie", i + 1)
    movie_name = input("Enter Movie Name: ")
    rating = float(input("Enter Rating: "))
    ticket_price = float(input("Enter Ticket Price: "))
    category = input("Enter Category (Hit/Average/Flop): ")

    movie = Movie(movie_name, rating, ticket_price, category)
    cinema.add_movie(movie)

cinema.display_movies()

'''
Output
Enter number of movies: 3

Enter details for Movie 1
Enter Movie Name: KGF
Enter Rating: 9
Enter Ticket Price: 499
Enter Category (Hit/Average/Flop): Hit

Enter details for Movie 2
Enter Movie Name: Spider-Man
Enter Rating: 8
Enter Ticket Price: 499
Enter Category (Hit/Average/Flop): Hit

Enter details for Movie 3
Enter Movie Name: Avengers-End Game
Enter Rating: 10
Enter Ticket Price: 599
Enter Category (Hit/Average/Flop): Hit

--- Movie Details ---
Movie Name: KGF
Rating: 9.0
Ticket Price: 499.0
Category: Hit

Movie Name: Spider-Man
Rating: 8.0
Ticket Price: 499.0
Category: Hit

Movie Name: Avengers-End Game
Rating: 10.0
Ticket Price: 599.0
Category: Hit
'''





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
