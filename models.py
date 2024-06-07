from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)

book_categories_table = Table('book_categories', Base.metadata,
    Column('book_id', ForeignKey('books.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True)
)

class BookCategories(Base):
    __tablename__ = 'book_categories'
    book_id = Column(ForeignKey('books.id'), primary_key=True)
    category_id = Column(ForeignKey('categories.id'), primary_key=True)
    book = relationship("Book", back_populates="categories")
    category = relationship("Category", back_populates="books")

Book.categories = relationship(
    "Category", secondary=book_categories_table, back_populates="books")
Category.books = relationship(
    "Book", secondary=book_categories_table, back_populates="categories")
