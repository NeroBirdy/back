import os
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class TelegramBotSettings(BaseModel):
    ADMIN_ID: str = os.getenv("ADMIN_ID")
    BASE_SITE: str = os.getenv("BASE_SITE")
    BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    WEBHOOK_PATH: str = f"/bot/{BOT_TOKEN}"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = False

    db: DbSettings = DbSettings()

    telegram_bot: TelegramBotSettings = TelegramBotSettings()
    
    def get_webhook_url(self) -> str:
        """Возвращает URL вебхука с кодированием специальных символов."""
        return f"{self.telegram_bot.BASE_SITE}{self.telegram_bot.WEBHOOK_PATH}"


settings = Settings()
