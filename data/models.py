from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base

class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(150))
    departure: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column()
    picture: Mapped[str] =mapped_column(String(800))
    stars: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(100))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(String(100))


class Reserve(Base):
    __tablename__ = "reserve"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    tour_id: Mapped[int] = mapped_column(ForeignKey(Tour.id))
    tour: Mapped[Tour] = relationship()