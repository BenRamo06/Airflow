from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


# Standar constructor

# first_dag = DAG(dag_id='first_dag',
#                 description= 'this is mi first dag',
#                 start_date= datetime(year=2022, month=4, day=15),
#                 tags=['learn','globant'],
#                 catchup=False)



# Context Manager

with DAG(dag_id='01.-Create_DAG',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:
         
         
         pass
