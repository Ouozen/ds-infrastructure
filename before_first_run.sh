#!/bin/bash

mkdir -p dags logs plugins config postgres_data ./mlflow/minio_config

docker compose up airflow-init
