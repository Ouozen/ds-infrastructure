#!/bin/bash

mkdir -p dags logs plugins config

python3 render_credentials.py

docker compose up airflow-init
