from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from config import settings

# Создание движка SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    connect_args={"check_same_thread": False}
)

# Создание фабрики сессий
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовый класс для моделей
Base = declarative_base()


def get_db() -> Session:
    """Dependency для получения сессии БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Создание всех таблиц"""
    Base.metadata.create_all(bind=engine)
