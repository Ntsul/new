

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, გამოცემის წელი: {self.year}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\nწიგნი '{book.title}' წარმატებით დაემატა!")

    def view_books(self):
        if not self.books:
            print("\nწიგნების სია ცარიელია.")
        else:
            print("\n ყველა წიგნის სია:")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print("\n ნაპოვნი წიგნები:")
            for book in results:
                print(book)
        else:
            print("\n წიგნი არ მოიძებნა.")


def main():
    manager = BookManager()

    while True:
        print("\n წიგნების მართვის სისტემა")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სათაურით")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპცია (1-4): ")

        if choice == "1":
            title = input("შეიყვანეთ წიგნის სათაური: ").strip()
            author = input("შეიყვანეთ ავტორი: ").strip()
            year = input("შეიყვანეთ გამოცემის წელი: ").strip()

            # ვალიდაცია
            if title and author and year.isdigit():
                book = Book(title, author, int(year))
                manager.add_book(book)
            else:
                print("\n გთხოვთ, შეიყვანეთ ვალიდური ინფორმაცია.")

        elif choice == "2":
            manager.view_books()

        elif choice == "3":
            title = input("შეიყვანეთ ძიების სათაური: ").strip()
            manager.search_by_title(title)

        elif choice == "4":
            print("\n დროებით!")
            break

        else:
            print("\n არასწორი ინფორმაცია. გთხოვთ, სცადოთ თავიდან.")

if __name__ == "__main__":
    main()
