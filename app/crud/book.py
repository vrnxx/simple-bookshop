from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.book import Book
from schemas.book import BookCreate


async def create_book(
    new_book: BookCreate,
    session: AsyncSession,
) -> Book:
    new_book_data = new_book.model_dump()
    db_book = Book(**new_book_data)

    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


async def get_book_id_by_name(
    book_name: str,
    session: AsyncSession,
) -> Optional[int]:
    db_book_id = await session.execute(
        select(Book.id).where(
            Book.name == book_name
        )
    )
    db_book_id = db_book_id.scalars().first()
    return db_book_id
