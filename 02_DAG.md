
# Airflow DAG Setup Guide

## 1. Create Your First DAG

Create a DAG file inside the `dags` folder, for example: `dags/1_first_dag.py`.

Use the decorator:

```python
@dag(schedule_interval="@daily", start_date='2023-01-01', catchup=False)
```

## 2. How DAGs Sync with Docker

DAGs are automatically synchronized with the Docker container using bind mounts. Any file you put in your project's `dags` folder will be available in the Docker container at `/opt/airflow/dags`.

## 3. Airflow Config Creation

When you create your first DAG, the `config/airflow.cfg` file will be created automatically. You will see configurations such as:

```ini
dag_folder = /opt/airflow/dags
dagbag_import_timeout = 30.0
```

## 4 If Dag is not showing on UI or parsig error
1) - If you have a syntax error in your DAG or DAG parsing is not completed, logs will not be generated in the `logs` folder.
2) ps aux | grep airflow - make sure scheduler and dag processor is running
3) Check DAG Folder Path
airflow config get-value core dags_folder


## 5 How to verify Dag are present in dags folder in docker container
```sh
docker ps | grep scheduler
docker exec -it airflow317_docker-airflow-scheduler-1 bash
ls /opt/airflow/dags
airflow config get-value core dags_folder
```

## 6 How To See Final Resolved Value (Best Way)
```bash
docker compose config
```