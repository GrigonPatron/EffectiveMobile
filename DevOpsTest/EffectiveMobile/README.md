# Effective Mobile - Test DevOps Project

Веб-приложение с backend на Python и reverse proxy через Nginx, запущенное в Docker-контейнерах.

---

## Структура проекта:

- Docker
- Docker Compose
- Nginx
- Python (http.server)

## **Схема файлов и папок:**

EffectiveMobile/
├ ─ backend/
│ - app.py
│ - Dockerfile
├ ─ nginx/
│ - nginx.conf
│ - docker-compose.yml
├ - README.md

## **Схема проекта:**

Пользователь -> Nginx (принимает HTTP запросы на 80-ый порт) -> Nginx проксирует запросы к backend сервису -> backend слушает порт 8080 внутри сети Docker (внутрення сеть Docker) -> ответ Пользователю

***Также**:*

- Backend запускается от пользователя без прав
- Healthcheck настроен для backend
- Backend не доступен с хоста
- Только 80-ый порт для nginx

**Технологии**:

- Docker
- Docker Compose
- Python 3 (http.server)
- nginx:1.28.3-alpine

## Запуск проекта:

git clone <repository_url>
cd EffectiveMobile
docker-compose up
curl http://localhost
result: Hello from Effective Mobile!
by *@GrigonPatron*
