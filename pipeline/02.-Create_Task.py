from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime


with DAG(dag_id='02.-Create_Task',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        # We create a task with DummyOperator with task_id equal "begin"
         t_begin = DummyOperator(task_id='begin')


# We specify steps in our DAG. t_begin is the only one task to execute.
t_begin