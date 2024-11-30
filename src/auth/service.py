from sqlalchemy.future import select
from sqlalchemy import update
from fastapi import HTTPException, status


from src.auth import models as auth_models
from src.auth import schemas as auth_schemas
from src.database import async_session_maker


class UserService:
    @staticmethod
    async def get_by_telegram_id(telegram_id: int) -> auth_models.User:
        """
        Получить пользователя по telegram_id.
        """
        async with async_session_maker() as session:
            query = select(auth_models.User).where(auth_models.User.telegram_id == telegram_id)
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User with telegram_id {telegram_id} not found.",
                )
            return user


    @staticmethod
    async def create(user_data: auth_schemas.UserCreateDB) -> auth_models.User:
        """
        Создать нового пользователя.
        """
        async with async_session_maker() as session:
            new_user = auth_models.User(
                **user_data.model_dump()
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    @staticmethod
    async def update(telegram_id: int, user_data: auth_schemas.UserUpdateDB) -> auth_models.User:
        """
        Обновить данные пользователя.
        """
        async with async_session_maker() as session:
            query = (
                update(auth_models.User)
                .where(auth_models.User.telegram_id == telegram_id)
                .values(**user_data.model_dump(exclude_unset=True))
                .returning(auth_models.User)
            )
            result = await session.execute(query)
            updated_user = result.fetchone()
            if not updated_user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User with telegram_id {telegram_id} not found.",
                )
            await session.commit()
            return updated_user
