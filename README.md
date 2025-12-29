# ✅ Todo App

A full-stack task management application built with Flask and PostgreSQL, fully containerized with Docker.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

## 📁 Project Structure

```
todo-app/
├── docker-compose.yml    # Container orchestration
├── web/                  # Flask application
│   ├── Dockerfile
│   ├── app.py
│   └── templates/
├── db/
│   └── init.sql         # Database initialization
└── nginx/               # Reverse proxy config
```

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/akmalariq/todo-app.git
cd todo-app

# Start the application
docker-compose up -d

# Access the app
open http://localhost:5000
```

## 🐳 Services

| Service | Port | Description |
|---------|------|-------------|
| `web` | 5000 | Flask application |
| `db` | 5432 | PostgreSQL database |

## ✨ Features

- Create, read, update, delete tasks
- Persistent storage with PostgreSQL
- Containerized deployment
- Development hot-reload

## 📝 License

MIT
