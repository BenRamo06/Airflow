from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_function():
    for i in range(0,3):
        if i%2==0:
            return 'pair'
        else:
            return 'inpair'


with DAG(dag_id='05.-Branch_Process',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        
         t_begin = DummyOperator(task_id='begin')

        # We create a  BranchPython to generate multiple outputs 
         t_num = BranchPythonOperator(task_id='numbers', python_callable=print_function)

        # Our function (print function) returns two values "pair" and "inpair", those returns must be TASK with the same name to generate a branch
         t_pair   = BashOperator(task_id='pair', bash_command='echo branch_pair')
         t_inpair = BashOperator(task_id='inpair', bash_command='echo branch_inpair')


         t_end = DummyOperator(task_id='end')


# We specify steps in our DAG, defined us branch 
t_begin >> t_num >> [t_pair, t_inpair]  >> t_end 