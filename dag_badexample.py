import pendulum

from airflow import DAG
from airflow.decorators import task

import numpy as np  # <-- THIS IS A VERY BAD IDEA! DON'T DO THAT!

with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def print_array():
        """Print Numpy array."""
        a = np.arange(15).reshape(3, 5)
        print(a)
        return a

    print_array()