#!/bin/bash

mkdir -p dags logs plugins config

python3 credentials_render.py

docker compose up airflow-init
