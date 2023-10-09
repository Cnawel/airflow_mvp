import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="extended_example_python_operator",
    schedule_interval=None,  # Use cron expression or timedelta objects for scheduling
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["extended_example"],
) as dag:

    @task()
    def generate_data():
        """Generate data using NumPy."""
        import numpy as np
        data = np.random.randn(10, 10)
        return data.tolist()

    @task()
    def perform_computation(data):
        """Perform computations using SciPy on the input data."""
        from scipy import linalg
        import numpy as np
        data_np = np.array(data)
        det = linalg.det(data_np)
        return det

    @task()
    def summarize_result(det):
        """Summarize the result."""
        print(f"Determinant of the matrix is {det}")

    # Defining task dependencies
    data = generate_data()
    det = perform_computation(data)
    summarize_result(det)