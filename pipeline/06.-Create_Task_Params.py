from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_function(ds, **kwargs):
    print('ds=')
    print(ds)

    print('kwargs')
    print(kwargs)

    print('kwargs[number]')
    print(kwargs['number'])

    print('kwargs[string]')
    print(kwargs['string'])






with DAG(dag_id='06.-Create_Task_Params',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        # We create a task with an operator (DummyOperator) 
         t_begin = DummyOperator(task_id='begin')

         t_hello_python = PythonOperator(task_id='printHello', 
                                         python_callable=print_function, 
                                         provide_context=True,
                                         op_kwargs={'number': 100, 'string':'hahaha'})

         # We create a task with an operator (DummyOperator) 
         t_end = DummyOperator(task_id='end')


# We specify steps in our DAG
t_begin >> t_hello_python >> t_end 