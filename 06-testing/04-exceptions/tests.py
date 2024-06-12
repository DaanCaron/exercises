import pytest
from book import Book


# valid tests
@pytest.mark.parametrize('title', [
    'Watchmen',
    'Flowers for Algernon',
    'Ulysses'
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])

def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


#invalid tests (no name)
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])

def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        assert Book("", isbn)



#invalid isbn numbers
@pytest.mark.parametrize('title', [
    'Watchmen',
    'Flowers for Algernon',
    'Ulysses'
])
@pytest.mark.parametrize('isbn', [
    '978-1779501126',
    '9780735611331',
    '978-1709571127',
    '978-1-77-950182-7',
    '97817795011271',
    '978073561131'
])

def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        assert Book(title, isbn)