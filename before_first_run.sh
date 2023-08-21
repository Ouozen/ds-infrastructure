#!/bin/bash

mkdir -p dags logs plugins config postgres_data

docker compose up airflow-init
