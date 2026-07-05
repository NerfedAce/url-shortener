# URL Shortener

A lightweight URL Shortener built with **Python** and **PostgreSQL**.

This project was created primarily to **test and validate a complete DevOps workflow**, including building, containerizing, deploying, and automating a Python application. While fully functional as a URL shortener, its primary purpose is to serve as a sample application for CI/CD pipelines and infrastructure experimentation.

The repository is **open to forks** and can be freely used for learning, testing, and experimenting with DevOps practices.

---

## Features

- Generate short URLs
- Redirect users to the original URL
- Store URL mappings in PostgreSQL
- Track click count
- Store region information
- Lightweight backend suitable for deployment and DevOps testing

---

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn

### Database

- PostgreSQL
- psycopg2


---

## Project Structure

```text
Url-Shortener/
│
├── backend/
│   ├── Main.py
│   ├── Model.py
│   ├── DBQuery.py
│   ├── requirements.txt
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.10+
- PostgreSQL
- Git

Optional:

- Docker
- Docker Compose

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/Url-Shortener.git
cd Url-Shortener
```

### Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## PostgreSQL Setup

### Install PostgreSQL

Download PostgreSQL from:

https://www.postgresql.org/download/

During installation:

- Remember the password for the `postgres` user.
- Leave the default port (`5432`) unless you need a different one.

### Create the database

```sql
CREATE DATABASE url_shortener;
```

### Create the table

```sql
CREATE TABLE urls (
    short_url VARCHAR(50) PRIMARY KEY,
    long_url TEXT NOT NULL,
    clicks INTEGER DEFAULT 0,
    region VARCHAR(100)
);
```

### Configure the database connection

Open:

```
backend/DBQuery.py
```

Update the connection details:

```python
host = "localhost"
user = "postgres"
password = "your_password"
database = "url_shortener"
port = 5432
```

---

## Running the Application

```bash
python backend/Main.py
```

---

## Running with Docker

If Docker support is available:

```bash
docker compose up --build
```

---

## Purpose

This project serves as a **sample application for DevOps experimentation**. It is intended for:

- CI/CD pipeline testing
- Docker and containerization practice
- Deployment automation
- Infrastructure provisioning
- Learning DevOps concepts

The application is intentionally kept simple, and no major feature additions are planned.

---

## Contributing

Feel free to fork this repository and use it for your own learning, deployments, or DevOps experiments.

If you find a bug or have a useful improvement, feel free to open an issue or submit a pull request.

---

## License

This project is open source and available for educational and personal use.
