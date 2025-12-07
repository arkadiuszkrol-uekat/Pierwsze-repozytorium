from zad_1 import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return (
            f"Library: {self._city}, {self._street}, {self._zip_code}, "
            f"open hours: {self._open_hours}, "
            f"phone: {self._phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self):
        return (
            f"Employee: {self._first_name} {self._last_name}, "
            f"hired: {self._hire_date}, birth date: {self._birth_date}, "
            f"adress: {self._city}, {self._street}, {self._zip_code}, "
            f"phone: {self._phone}"
        )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
        title,
    ):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages
        self._title = title

    def __str__(self):
        return (
            f"\nBook: {self._title}, author: {self._author_name} {self._author_surname}, "
            f"{self._number_of_pages} pages, publicated on: {self._publication_date}, "
            f"in library: {self._library._city}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self._employee = employee
        self._student = student
        self._books = books  # lista obiektów klasy Book
        self._order_date = order_date

    def __str__(self):
        books_str = "".join(str(book) for book in self._books)
        return (
            f"Order: {self._order_date}, "
            f"Employee: {self._employee._first_name} {self._employee._last_name}, "
            f"Student: {self._student._name}, "
            f"Books: {books_str}"
        )


# Tworzymy biblioteki
lib1 = Library("Bytom", "Cyryna i Metodego", "41-909", "8-18", "123-456-789")
lib2 = Library(
    "Warszawa", "ul. Pola Mokotowskie", "32-909", "9-19", "987-654-321"
)

# Tworzymy książki
book1 = Book(lib1, "2020-01-01", "Ewa", "Chodakowska", 200, "W drogę")
book2 = Book(lib1, "2019-05-12", "Andrzej", "Duda", 150, "Prezydenci i ja")
book3 = Book(lib2, "2018-07-23", "Tomek", "Pociąg", 300, "Po torach")
book4 = Book(lib2, "2021-11-30", "Kai", "Sa", 250, "ADC basics")
book5 = Book(lib1, "2022-03-15", "Arek", "Król", 180, "Chess 2.0")

# Tworzymy pracowników
emp1 = Employee(
    "Anna",
    "Kowal",
    "2020-01-01",
    "1990-05-05",
    "Warszawa",
    "ul. Kwiatowa 5",
    "00-001",
    "123-456-789",
)
emp2 = Employee(
    "Jan",
    "Nowak",
    "2019-02-10",
    "1985-03-15",
    "Kraków",
    "ul. Leśna 10",
    "30-002",
    "987-654-321",
)
emp3 = Employee(
    "Marta",
    "Wiśniewska",
    "2021-06-20",
    "1992-07-07",
    "Warszawa",
    "ul. Słoneczna 1",
    "00-003",
    "321-654-987",
)

# Tworzymy studentów
student1 = Student("Asia", [60, 70, 80])
student2 = Student("Kasia", [40, 50, 45])
student3 = Student("Basie", [55, 60, 65])

# Tworzymy zamówienia
order1 = Order(emp1, student1, [book1, book2, book5], "2023-11-30")
order2 = Order(emp2, student2, [book3, book4], "2023-11-29")

# Wyświetlamy zamówienia
print(order1)
print()
print(order2)
