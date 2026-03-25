# airflow3.1.7_docker

# AIRFLOW CLI

## For DOcker
docker ps
docker exec -it container_id sh  # Get container id using docker ps command
airflow
airflow info
## For Kubernets
kubctl exec -it scheduler pod_name -- sh


## Airlfow commands CLI
airflow users create


## Security >> List >> roles on UI


## Know your airflow environment
airflow version
airflow info  # List providers along with versions   
airflow config list
airlfow config list | grep parallelism
airflow config get-value core max_active_runs_per_dag
airflow cheat-sheet
airflow varaibles export variables.json
airflow db check # “Is my Airflow database alive and reachable?”
airflow dags report # Gives overview/statistics of DAGs
airflow dags list-import-errors # explicitly shows: Syntax errors,Missing dependencies,Broken imports
#Think of it like: “Show me which DAG files failed to load and why.”

## References
[Local Development Environment](http://academy.astronomer.io/local-development-environment)
[Environment Variables ](https://academy.astronomer.io/astro-module-environment-variables)
[Airflow Configuration](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html)
[CLI Commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)
https://academy.astronomer.io/connections-101
[Debugging DAGs](https://academy.astronomer.io/debug-dags)


