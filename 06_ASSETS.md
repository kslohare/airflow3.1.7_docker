
# airflow3.1.7_docker

# Assets
```text
In Apache Airflow, the term Asset represents a piece of data that workflows produce or depend on.
Simple Definition:
Asset = a data object that a workflow creates, updates, or consumes.

Examples of assets:
    A table in a database
    A file in S3
    A dataset
    A machine learning model file
    A report generated daily
```

## Why Assets are Important in Airflow

Before assets, DAGs were triggered mainly by:

time schedules (cron)

manual triggers

With assets:

workflows can run when data changes

Example:

Instead of:

Run every day at 1 AM

You can say:

Run when the sales dataset is updated

This is called data-aware scheduling.

| Component | Meaning                                       |
| --------- | --------------------------------------------- |
| Task      | Unit of work                                  |
| DAG       | Workflow of tasks                             |
| Scheduler | Decides when to run DAGs                      |
| **Asset** | Data object produced or consumed by workflows |

##
airflow assets list



