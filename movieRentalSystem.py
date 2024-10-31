# 12. Movie Rental System
# • Description: Develop a console application for managing a movie rental service. Implement classes for Movie, Customer, and Rental. Include features for renting and returning movies and tracking rental history.
# • OOP Concepts: Inheritance (different movie genres), Composition (rentals consist of movies), and Encapsulation (managing customer data).

class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True

    def __str__(self):
        available = "Available" if self.available else "Not available"
        return f'Movie name: {self.title}\nGenre: {self.genre}\nYear of release: {self.year}\nAvailability: {available}\n'
    
class Customer:
    def __init__(self, name, address, phone_no):
        self.name = name
        self.__address = address
        self.__phone = phone_no
        self.rented = []
    
    def rent_movie(self, movie):
        if movie.available:
            movie.available = False
            self.rented.append(movie)
            print(f"{self.name} rented {movie.title}.")
        else:
            print(f"{movie.title} is not available right now.")
    
    def return_movie(self, movie_title):
        for movie in self.rented:
            if movie.title == movie_title:
                movie.available = True
                self.rented.remove(movie)
                print(f"{self.name} returned {movie.title}.")
                return
        print(f"{self.name} has not rented {movie_title}.")
    
    def view_rented(self):
        if self.rented:
            print(f"The movies rented by {self.name} are: ")
            for movie in self.rented:
                print(movie)
            print()
        else:
            print(f"{self.name} has not rented any movies.")

class ComedyMovie(Movie):
    def __init__(self, title, year):
        super().__init__(title, "Comedy", year)

class MarvelMovie(Movie):
    def __init__(self, title, year):
        super().__init__(title, "Sci-Fi", year)
    
class MovieRentalSystem:
    def __init__(self):
        self.movies = []
        self.customers = []

    def add_movie(self, movie):
        self.movies.append(movie)
        

    def add_customer(self, customer):
        self.customers.append(customer)
        

    def display_movies(self):
        print("\n--- Available Movies ---")
        for movie in self.movies:
            print(movie)
        print("-"*25)

    def rent_movie(self, customer_name, movie_title):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        movie = next((m for m in self.movies if m.title == movie_title), None)
        
        if not customer:
            print(f"Customer {customer_name} not found.")
            return
        if not movie:
            print(f"Movie {movie_title} not found.")
            return
        
        customer.rent_movie(movie)

    def return_movie(self, customer_name, movie_title):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if not customer:
            print(f"Customer {customer_name} not found.")
            return

        customer.return_movie(movie_title)
s = MovieRentalSystem()

m1 = ComedyMovie("Phir Hera Phiri", 2015)
m2 = MarvelMovie("Avengers", 2018)
m3 = MarvelMovie("Spider-Man", 2019)
s.add_movie(m1)
s.add_movie(m2)
s.add_movie(m3)
c1 = Customer("Pragyan", "Bhaktapur", "98401111111")
c2 = Customer("Hari", "Kathmandu", "019829382")
s.add_customer(c1)
s.add_customer(c2)
s.display_movies()

s.rent_movie("Hari", "Avengers")
s.rent_movie("Hari", "Phir Hera Phiri")

s.display_movies()

s.return_movie("Hari", "Phir Hera Phiri")
s.display_movies()
c1.view_rented()
c2.view_rented()