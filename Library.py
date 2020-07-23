from enum import Enum
from datetime import date
from abc import ABC, abstractmethod

class BookStatus(Enum):

  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class Book(ABC):

  def __init__(self,title,author, edition):
    self.__title = title
    self.author = author
    self.edition = edition
  
  @abstractmethod
  def change_status(self, status: BookStatus):
    self.status = status

class Client:

  def __init__(self, name, surname, personal_id, books = None):
    self.name = name
    self.surname = surname
    self.personal_id = personal_id
    self.books = set()
  
  def borrow_book(self, book):
    self.book_borrowed = book
    self.havebook = True
    self.books.add(self.book_borrowed)
    book.status = BookStatus.LOANED
  
  def return_book(self, book):
    if book in self.books:
      self.books.remove(book)
      book.stauts = BookStatus.AVAILABLE
      print (f"{book} was returned successfully")
    else:
      raise ValueError("This user has no book to return")


class BookItem(Book):
  
  def __init__ (self, item, title, author, edition, is_taken = False):
    super().__init__(title, author, edition)
    self.item = item
    self.status = BookStatus.AVAILABLE
    # self.start_date = start_date
    # self.end_date = end_date
  
  def change_status(self, status: BookStatus = BookStatus.AVAILABLE):
    if isinstance(status, BookStatus):
      self.status = status
    else:
      raise ValueError("This is not a valid status") 

  def __repr__(self):
    return self.title
  
