# FastAPI App Template

FastAPI application template with comprehensive tooling and best practices built-in.

## Features

- **FastAPI Framework**: Fast web framework for building APIs with Python
- **Async Database**: PostgreSQL with SQLAlchemy 2.0 and asyncpg
- **Dependency Injection**: Clean architecture with Punq DI container
- **Database Migrations**: Alembic for database schema management
- **Environment Management**: Pydantic Settings for type-safe configuration
- **Code Quality**: Black, isort, and Ruff for formatting and linting
- **Testing**: Pytest with async support and comprehensive test structure
- **Docker Support**: Multi-stage Dockerfile with Poetry
- **Development Tools**: Makefile for common development tasks
- **Health Checks**: Built-in health check endpoints
- **Logging**: Structured logging configuration

## Tech Stack

- **Python**: 3.12+
- **Framework**: FastAPI 0.115+
- **Database**: PostgreSQL with SQLAlchemy 2.0
- **Async**: uvloop for enhanced performance
- **Dependency Management**: Poetry
- **Testing**: Pytest with async support
- **Code Quality**: Black, isort, Ruff
- **Containerization**: Docker with multi-stage builds

## Quick Start

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ApriCotBrain/FastAPI-app-template.git
   cd FastAPI-app-template
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   ```bash
   cp compose/local/.env_example compose/local/.env
   # Edit compose/local/.env with your configuration
   ```

4. **Run the application**
   ```bash
   poetry run python manage.py run-api
   ```

### Option 2: Docker Development

1. **Start the application with Docker Compose**
   ```bash
   cd compose/local
   docker-compose up -d --build
   ```

The API will be available at `http://localhost:8000`

## Project Structure

```
FastAPI-app-template/
├── app/                    # Application source code
│   ├── api/               # API layer
│   │   ├── v1/           # API version 1 endpoints
│   │   ├── health_checks/ # Health check endpoints
│   │   ├── globals/      # Global API configurations
│   │   ├── application.py # FastAPI application setup
│   │   ├── bootstrap.py  # Dependency injection setup
│   │   └── main.py       # Application entry point
│   └── core/             # Core application modules
│       ├── database/     # Database configuration and models
│       ├── logging/      # Logging configuration
│       └── settings.py   # Application settings
├── tests/                # Test suite
│   ├── api/             # API tests
│   ├── database/        # Database tests
│   ├── helpers/         # Test helpers
│   └── utils/           # Test utilities
├── compose/             # Docker Compose configurations
│   ├── local/          # Local development setup
│   └── dev/            # Development environment
├── pyproject.toml      # Poetry configuration and dependencies
├── Dockerfile          # Multi-stage Docker build
├── manage.py           # CLI management commands
├── Makefile           # Development task automation
└── alembic.ini        # Database migration configuration
```

## Development Commands

### Code Formatting and Linting

```bash
# Format code
make run_formatters

# Check code formatting
make run_linters

# Individual commands
make black_formatter    # Format with Black
make isort_formatter    # Sort imports
make ruff_checker       # Run Ruff linter
```

### Database Operations

```bash
# Run database migrations
alembic upgrade heads

# Create new migration
alembic revision --autogenerate -m "Description"

# Rollback migration
alembic downgrade -1
```

### Testing

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=app

# Run specific test file
poetry run pytest tests/api/test_example.py
```

### Application Management

```bash
# Run API server
poetry run python manage.py run-api

# Run workers (placeholder)
poetry run python manage.py run-workers

# Run consumers (placeholder)
poetry run python manage.py run-consumers
```

## Configuration

The application uses Pydantic Settings for configuration management. Key configuration classes:

- **DatabaseSettings**: PostgreSQL connection and pool settings
- **ServerSettings**: Uvicorn server configuration
- **SystemSettings**: Environment and system-wide settings

Configuration can be set via:
- Environment variables
- `.env` file
- Nested environment variables using `__` delimiter

### Example Environment Variables

```bash
# Database
DATABASE__DSN=postgresql+asyncpg://user:password@localhost/dbname
DATABASE__ENGINE_POOL_SIZE=20

# Server
SERVER__PORT=8000
SERVER__WORKERS=1
SERVER__RELOAD=true

# System
SYSTEM__ENVIRONMENT=dev
SYSTEM__HOME_URL=http://localhost:8000

# Logging
LOGGING_LEVEL=DEBUG
```

## Docker

The project includes a multi-stage Dockerfile optimized for production:

- **Builder stage**: Installs dependencies and creates virtual environment
- **App stage**: Minimal runtime image with application code

### Docker Commands

```bash
# Build image
docker build -t fastapi-app .

# Run container
docker run -p 8000:8000 fastapi-app

# Use Docker Compose for development
cd compose/local
docker-compose up --build
```

## Testing

The project includes a comprehensive test suite with:

- **Pytest**: Test framework with async support
- **Respx**: HTTP mocking for external API calls
- **Test fixtures**: Database and application fixtures
- **Test helpers**: Utility functions for testing

### Test Structure

- `tests/api/`: API endpoint tests
- `tests/database/`: Database model and query tests
- `tests/helpers/`: Test helper functions
- `tests/utils/`: Test utilities
- `tests/conftest.py`: Pytest configuration and fixtures

## API Documentation

When the application is running, you can access:

- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`
- **OpenAPI schema**: `http://localhost:8000/openapi.json`

## Health Checks

The application includes built-in health check endpoints:

- **Health check**: `GET /health`
- **Readiness check**: `GET /ready`
- **Liveness check**: `GET /live`


## Author

**Olga Melikhova** - [melihovao@yandex.ru](mailto:melihovao@yandex.ru)
