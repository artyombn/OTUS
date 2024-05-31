#!/usr/bin/env bash

echo "Starting"

# Применение миграций в контексте Poetry
poetry run flask db upgrade

echo "Migrations applied"

# Запуск Flask-приложения в контексте Poetry
poetry run python app.py
