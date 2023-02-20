from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import os

from datetime import datetime

with DAG(
    dag_id='aiComedian_dag',
    start_date=datetime(2023, 2, 18),
    schedule_interval=None
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )
    startRegex = BashOperator(
        task_id='executeRegex',
        bash_command='python /opt/ai/regex.py'
        #bash_command='echo $PWD'
    )

    end_task = EmptyOperator(
        task_id='end'
    )

start_task >> startRegex
startRegex >> end_task