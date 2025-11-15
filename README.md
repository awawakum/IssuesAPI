# IssuesAPI

API для управления проблемами, построенный на FastAPI и SQLAlchemy.

## 🛠️ Технологический стек

- **FastAPI** 0.121.2 — современный веб-фреймворк
- **SQLAlchemy** 2.0.44 — ORM для работы с БД
- **SQLite** — встроенная база данных
- **Pydantic** 2.12.4 — валидация данных
- **Uvicorn** 0.38.0 — ASGI сервер
- **Python** 3.8+

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/IssuesAPI.git
cd IssuesAPI
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

Активация на Windows:
```bash
venv\Scripts\Activate
```

Активация на Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
python main.py
```

Приложение будет доступно по адресу: `http://127.0.0.1:8010`

Документация Swagger: `http://127.0.0.1:8010/docs`

Документация ReDoc: `http://127.0.0.1:8010/redoc`

## 📚 API Endpoints

### Получить все issue
```http
GET /issue/issues
```

**Ответ:**
```json
[
  {
    "id": 1,
    "text": "Описание issue",
    "status": "open",
    "source": "operator",
    "created_at": "2023-11-15T10:00:00",
    "updated_at": "2024-11-15T10:00:00"
  }
]
```

### Получить issue по ID
```http
GET /issue/{issue_id}
```

**Параметры:**
- `issue_id` (int) — идентификатор issue

### Получить issue по статусу
```http
GET /issue/status/{status}
```

**Параметры:**
- `status` (string) — статус issue (например: "open", "closed", т.д.)

**Ответ:**
```json
[
  {
    "id": 1,
    "text": "test",
    "status": "open",
    "source": "operator",
    "created_at": "2025-11-15T10:00:00",
    "updated_at": "2025-11-15T10:00:00"
  }
]
```

### Создать новую issue
```http
POST /issue/
```

**Тело запроса:**
```json
{
  "text": "test",
  "status": "open",
  "source": "operator"
}
```

**Ответ:** (201 Created)
```json
{
  "id": 2,
  "text": "test",
  "status": "open",
  "source": "operator",
  "created_at": "2025-11-15T10:30:00",
  "updated_at": "2025-11-15T10:30:00"
}
```

### Обновить issue
```http
PUT /issue/{issue_id}
```

**Параметры:**
- `issue_id` (int) — идентификатор issue

**Тело запроса:**
```json
{
  "text": "Обновленное описание",
  "status": "closed",
  "source": "operator"
}
```

**Ответ:**
```json
{
  "id": 1,
  "text": "Обновленное описание",
  "status": "closed",
  "source": "operator",
  "created_at": "2025-11-15T10:00:00",
  "updated_at": "2025-11-15T11:00:00"
}
```

### Удалить issue
```http
DELETE /issue/{issue_id}
```

**Параметры:**
- `issue_id` (int) — идентификатор issue

**Ответ:** (204 No Content)

## 🏗️ Архитектура проекта

```
IssuesAPI/
├── main.py                 # Точка входа приложения
├── config.py              # Конфигурация приложения
├── database.py            # Подключение к БД и сессии
├── logging_config.py      # Настройка логирования
├── requirements.txt       # Зависимости Python
├── models/
│   └── issue.py          # ORM модель Issue
├── schemas/
│   └── issue.py          # Pydantic схемы для валидации
├── repositories/
│   └── issue.py          # Слой доступа к данным
├── services/
│   └── issue.py          # Бизнес-логика
├── routing/
│   └── issue.py          # API маршруты
└── logs/                 # Логи приложения
```

### Слои приложения

1. **Models** (`models/`) — Модели для работы с БД
2. **Schemas** (`schemas/`) — Pydantic модели для валидации входных/выходных данных
3. **Repositories** (`repositories/`) — Слой доступа к данным (Data Access Layer)
4. **Services** (`services/`) — Слой бизнес-логики (Business Logic Layer)
5. **Routing** (`routing/`) — API маршруты и обработчики (Handler Layer)

## 📝 Использование примеры

### Python requests

```python
import requests

# Получить все issue
response = requests.get('http://127.0.0.1:8010/issue/issues')
print(response.json())

# Создать новую issue
new_issue = {
    "text": "test",
    "status": "open",
    "source": "operator"
}
response = requests.post('http://127.0.0.1:8010/issue/', json=new_issue)
print(response.json())

# Обновить issue
updated_issue = {
    "status": "closed"
}
response = requests.put('http://127.0.0.1:8010/issue/1', json=updated_issue)
print(response.json())

# Удалить issue
response = requests.delete('http://127.0.0.1:8010/issue/1')
print(response.status_code)
```

### curl

```bash
# Получить все issues
curl http://127.0.0.1:8010/issue/issues

# Создать issue
curl -X POST http://127.0.0.1:8010/issue/ \
  -H "Content-Type: application/json" \
  -d '{"text":"test","status":"open","source":"operator"}'

# Обновить issue
curl -X PUT http://127.0.0.1:8010/issue/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"closed"}'

# Удалить issue
curl -X DELETE http://127.0.0.1:8010/issue/1
```

## Тестовые данные

Для добавления тестовых данных:

```bash
python add_test_data.py
```

## 📋 Модель данных

### Issue

| Поле | Тип | Описание |
|------|-----|---------|
| id | int | Уникальный идентификатор |
| text | string | Описание issue (макс. 128 символов) |
| status | string | Статус issue (open / close / in_progress) |
| source | string | Источник issue (operator / monitoring / partner) |
| created_at | datetime | Время создания |
| updated_at | datetime | Время последнего обновления |

## 📖 Документация

- **Swagger UI**: После запуска приложения перейдите на `http://127.0.0.1:8010/docs`
- **ReDoc**: `http://127.0.0.1:8010/redoc`

## 📊 Логирование

Приложение использует структурированное логирование. Логи записываются:

- В консоль 
- В файл `logs/issuesapi.log` 
