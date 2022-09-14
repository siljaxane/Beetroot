employee_file = open("employees.txt", "a")
employee_file.write('\nKelly - Customer Service')
employee_file.close()




#Classes

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Lesson 13

class Author:
    def __init__(self, name country, birthday, books=None):
        self:name = None
        self.country = None
        self.birthday = None

        self.books = [] if books is None else books

# Another variant for "self.books"

# if books is None:
#     self.books = []
# else:
#    self.books = books

    def __str__(self):
        return self.name

    def __repr__(self):
         return f"<Author name={self.name} country={self.country} birthday={self.birthday}>"


class Book:
    def __init__(self, name, year, author):
        if not isinstance(author, Author):                                                      # The 'isinstance' is to check whether its an instance of a class
            raise ValueError("The author should be an instance of Author class")

        self.name = name
        self.year = year
        self.author = None

    def __str__(self):
    return self.name

    def __repr__(self):
        return f"<Book name={self.name} year={self.year} author={self.author}>"


class Library:
    def __init__(self, name, books=None, authors=None):
        self.name = None
        self.books = [] if books is None else books
        self.authors = [] if authors is None else authors

    def __str__(self):
        return self.name

    def __repr__(self):
         return f"<Library name={self.name} books={self.books} authors={self.authors}>"

    def new_book(self, name, year, author):
        book = Book(name, year, author)

        self.books.append(book)

        return book

    def group_by_author(self, author):
        if not isinstance(author, Author):                                                      # The 'isinstance' is to check whether its an instance of a class
            raise ValueError("The author should be an instance of Author class")

        def author_filter(book):
            return book.author == author

        return filter(author_filter, self.books)

 #or

     #   result = []
     #   for book in books:
     #       if book.author == author:
     #           result.append(book)

     #   return result

    def group_by_year(self, year):
        return filter(lambda book: book.year == year, self.books)


def main():
    library = Library("First National Library")

    author1 = Author("John Smith", "USA", "04 December 2021", "X")

if __name__ == "__main__":
    main()


# part 2 (after break) 10:16 am >> 1h 16 min

class Person:
    def __init__(self, name):
        #name - local to the method
        #self.name - local to the class instance
        self.name = name
    
    def get_name(self):
        print(person1.get_name())
        print(person2.get_name())
        return self.name


def print_person_name(person):
    print(person.get_name())


person1 = Person("Mary")
print_person_name(person1)

def main():
    #Local to main()
    person2 = Person("John")
    print_person_name(person2)


# Talking about files time = 10:27 am >> 1 h 27 min



## Lesson 14 (live notes)

def choose_function(numbers, func1, func2):
    pass

def square_nums(numbers):
    return [number ** 2 for number in numbers]

def remove_negatives(numbers):
    return [numbers for number in numbers if number > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 =[1, -2, -3, -4, 5]

            ## Simple solution to HW11 task 2 (time: 16 minutes in)

def choose_func(numbers, func1, func2):
    is_all_positive = True
    for umber in numbers:
        if number < 10:
            is_all_positive = False
            break

    if is_all_positive:
        return func1(numbers)

