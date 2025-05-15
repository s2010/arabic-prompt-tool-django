# 🧠 Arabic Prompt Tool – Scalable Dockerized Django Backend

A production-grade, async-ready Django web app for managing and exploring Arabic AI prompts. Designed to be extensible and easily deployable with FastAPI, HTMX, PostgreSQL, and Docker.

---

## 🚀 Features

- 🔐 User authentication (login, logout, register)
- 📝 Submit, approve, and list Arabic prompts
- 🔎 HTMX-based live search & filtering
- 👍 HTMX-powered upvotes
- 🖥️ Django Admin panel for moderation
- 🧬 Async views via ASGI
- 📡 WebSocket-ready using Django Channels
- 🔗 Co-mounted FastAPI endpoints
- 🐳 Fully Dockerized with PostgreSQL backend

---

## ⚙️ Stack

- Python 3.11
- Django 4+ (ASGI support)
- FastAPI
- PostgreSQL
- HTMX (frontend)
- Docker + Docker Compose
- Django Channels (optional, for WebSockets)

---

## 🏁 Quickstart

### 1. Clone and enter the repo
```bash
git clone https://github.com/YOUR_NAME/arabic-prompt-tool.git
cd arabic-prompt-tool
```

### 2. Create `.env` file
```env
DEBUG=True
SECRET_KEY=change-me
DATABASE_URL=postgres://postgres:postgres@db:5432/prompts
```

### 3. Build and run containers
```bash
docker compose up --build
```

### 4. Run migrations and create superuser
```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---

## 🌐 Access Points

| URL                      | Function                            |
|--------------------------|-------------------------------------|
| `/`                      | List approved prompts               |
| `/submit/`               | Submit a new prompt                 |
| `/upvote/<id>/`          | Upvote a prompt (HTMX)              |
| `/admin/`                | Django admin panel                  |
| `/ping/`                 | Async test view                     |
| `/api/ping`              | FastAPI endpoint                    |
| `/dashboard/`            | (optional) User’s own submissions   |

---

## 🛠 Developer Features

- Async Django views
- Django + FastAPI mounted on same ASGI layer
- HTMX frontend for reactive UX without JS frameworks
- Full support for Django Admin and staticfiles via `collectstatic`

---

## 🧪 Running Tests
```bash
docker compose exec web pytest
```

---

## 🧬 Using FastAPI Inside Django

FastAPI routes are served under `/api/` via shared ASGI application in `core/asgi.py`.

---

## 🐳 Deployment Notes

To prepare for production:
```bash
docker compose exec web python manage.py collectstatic --noinput
```

Deploy on:
- Railway
- Google Cloud Run
- Any VPS (with Docker)

---

## 🔮 Planned Enhancements

- GPT-powered Arabic prompt generator
- OCR + summarization for scanned Arabic documents
- User dashboard to manage prompt history
- Token-based API access
- AI-powered prompt ranking

---

## 🧑‍💻 Built By

Crafted for scale, designed for clarity.
