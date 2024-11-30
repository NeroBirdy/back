from typing import Any, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, BigInteger, ForeignKey, String


from src.models import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    token: Mapped[Optional[dict[str, Any]]] = mapped_column(
        JSON,
        nullable=True,
    )