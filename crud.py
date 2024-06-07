from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, content=book.content)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_categories(db: Session, categories: list[schemas.CategoryCreate]):
    db_categories = [models.Category(name=cat.name, type=cat.type) for cat in categories]
    db.add_all(db_categories)
    db.commit()
    return db_categories

def get_books(db: Session, skip: int, limit: int):
    return db.query(models.Book).offset(skip).limit(limit).all()
