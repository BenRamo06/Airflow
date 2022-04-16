from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


# Standar constructor

first_dag = DAG(dag_id='first_dag',
                description= 'this is mi first dag',
                start_date= datetime(year=2022, month=4, day=15),
                tags=['learn','globant'],
                catchup=False)

t_begin = DummyOperator(task_id='begin', dag=first_dag)

t_end = DummyOperator(task_id='end', dag=first_dag)


t_begin >> t_end