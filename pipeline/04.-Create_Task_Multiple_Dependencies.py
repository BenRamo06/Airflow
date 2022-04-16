from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_function():
    print('Hello Python')


with DAG(dag_id='04.-Create_Task_Multiple_Dependencies',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        # We create a task with an operator (DummyOperator) 
         t_begin = DummyOperator(task_id='begin')

         t_hello_bash = BashOperator(task_id='echoHello', bash_command='echo Hello')

         t__hello_python = PythonOperator(task_id='printHello', python_callable=print_function)

         # We create a task with an operator (DummyOperator) 
         t_end = DummyOperator(task_id='end')


# We specify steps in our DAG
t_begin >> [t_hello_bash,t__hello_python]  >> t_end 