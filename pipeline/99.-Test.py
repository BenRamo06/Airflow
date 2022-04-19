from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_function(**kwargs):
    if datetime.today().day%2==0:
        return 'pair'
    else:
        return 'inpair'
        

def is_pair():
    print('is pair')


def is_inpair():
    print('is inpair')


with DAG(dag_id='99.-Test',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        
         t_begin = DummyOperator(task_id='begin')

        # We create a  BranchPython to generate multiple outputs 
         t_num = BranchPythonOperator(task_id='numbers', python_callable=print_function)

        # Our function (print function) returns two values "pair" and "inpair", those returns must be TASK_ID to generate a branch
         t_pair   = PythonOperator(task_id='pair', python_callable=is_pair)
         t_inpair = PythonOperator(task_id='inpair', python_callable=is_inpair)


         t_end = DummyOperator(task_id='end')


# We specify steps in our DAG, defined us branch 
t_begin >> t_num >> [t_pair, t_inpair]  
t_pair >> t_end
t_inpair >> t_end