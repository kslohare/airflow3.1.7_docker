from airflow.sdk import dag, task
from datetime import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"],
)
def hello_dag():

    @task
    def task_1():
        print("I am task 1")

    @task
    def task_2():
        print("I am task 2")

    @task
    def task_3():
        print("I am task 3")

    t1 = task_1()
    t2 = task_2()
    t3 = task_3()

    t1 >> t2 >> t3


hello_dag()