#!/bin/sh

# rm -f tmp/pids/server.pid
# mkdir -p tmp/sockets
# mkdir -p tmp/pids

# DBが起動できるまでsleepする
until nc -z ${DB_HOST} 3306; do
  >&2 echo "mysql is unavailable - waiting"
  sleep 3
done

mysql -h ${DB_HOST} -u ${DB_USERNAME} -p${DB_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS ${DB_DATABASE}"


# DBの準備
current_dir=$(pwd)
cd db && alembic upgrade head
cd "$current_dir"

# uvicorn起動
uvicorn main:app --reload --host 0.0.0.0 --port 8000
