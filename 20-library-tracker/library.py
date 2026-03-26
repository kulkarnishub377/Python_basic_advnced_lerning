from book import Book

class Library:
    """
    An Object-Oriented Management class facilitating exactly how users interact 
    with internal Book properties cleanly without mutating isolated state.
    """

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book_obj):
        """Composition: adding explicitly defined external Objects into the catalog array natively."""
        if isinstance(book_obj, Book):
            self.books.append(book_obj)

    def borrow_book(self, title, user_name):
        """
        Locates a book and mutates its property natively.
        Return True if successful, False if unavailable or missing.
        """
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_available:
                    b.borrowed_by = user_name
                    return True
                else:
                    return False
        return False

    def return_book(self, title):
        """
        Restores a Book object safely back into circulation native variables gracefully.
        """
        for b in self.books:
            if b.title.lower() == title.lower():
                if not b.is_available:
                    b.borrowed_by = None
                    return True
        return False

    def search_books(self, query):
        """
        List comprehensions return precisely filtered collections evaluating boolean metrics.
        """
        query = query.lower()
        return [b for b in self.books if query in b.title.lower() or query in b.author.lower()]
