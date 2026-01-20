# Superheroes API

## Author
MarkWainainaWagacha

## Description
A Flask REST API for managing superheroes and their superpowers.

## Setup Instructions
```bash
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
python seed.py
python run.py

API Routes :

GET /heroes

GET /heroes/:id

GET /powers

GET /powers/:id

PATCH /powers/:id

POST /hero_powers


Technologies :

Flask

SQLAlchemy

SQLite



