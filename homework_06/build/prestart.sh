#!/usr/bin/env bash
#echo "/app"
#ls -l /app

#echo "Waiting for database to be ready..."
#
## доступность порта 5432 с использованием netcat
##while ! nc -zv pg 5432 &> /dev/null
#while ! telnet pg 5432 </dev/null 2>&1 | grep -q Connected;
#do
#    echo "Database is not yet reachable, waiting..."
#    sleep 1
#done
#
#echo "Database is now reachable"

echo "Run migrations"

flask db upgrade

echo "Migrations applied"

python app.py
