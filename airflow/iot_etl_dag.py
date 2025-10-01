from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'krish',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('iot_etl_dag',
         default_args=default_args,
         schedule_interval='@daily',
         start_date=datetime(2025, 1, 1),
         catchup=False) as dag:

    extract = BashOperator(
        task_id='extract_data',
        bash_command='echo "Extracting IoT Data"'
    )

    transform = BashOperator(
        task_id='transform_data',
        bash_command='echo "Transforming IoT Data with Spark"'
    )

    load = BashOperator(
        task_id='load_data',
        bash_command='echo "Loading IoT Data to PostgreSQL"'
    )

    extract >> transform >> load
