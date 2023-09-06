#!/bin/bash

mkdir -p dags logs plugins config postgres_data postgres_prod clickhouse_data s3_data

python3 render_credentials.py

docker compose up airflow-init
