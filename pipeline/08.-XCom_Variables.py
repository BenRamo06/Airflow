from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(dag_id='07.-Create_Task_Trigger',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:
        
         t_begin = DummyOperator(task_id='begin')



         t_end = DummyOperator(task_id='end')





t_begin