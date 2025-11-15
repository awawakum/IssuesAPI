from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфигурация приложения"""
    
    # Database
    DATABASE_URL: str = "sqlite:///./issues.db"
    DATABASE_ECHO: bool = True  # SQL логирование
    
    # API
    API_TITLE: str = "IssuesAPI"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "API for issues management"
    # Logging
    LOG_LEVEL: str = "INFO"
    # File logging
    LOG_TO_FILE: bool = True
    LOG_FILE_PATH: str = "logs/issuesapi.log"
    # If True, use RotatingFileHandler with max bytes and backup count
    LOG_ROTATE: bool = True
    LOG_MAX_BYTES: int = 10 * 1024 * 1024  # 10 MB
    LOG_BACKUP_COUNT: int = 5
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
