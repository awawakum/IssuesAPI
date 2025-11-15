from fastapi import FastAPI
from routing.issue import router as issue_routing
from database import create_tables
from config import settings
from logging_config import setup_logging

# Настроим логирование как можно раньше
setup_logging()

# Создание таблиц при старте приложения
create_tables()

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION,
)

app.include_router(issue_routing)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="127.0.0.1", port=8010, reload=True)
