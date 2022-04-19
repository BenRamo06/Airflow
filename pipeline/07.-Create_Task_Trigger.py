from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_function():
    if datetime.today().day%2==0:
        return 'pair'
    else:
        return 'inpair'


with DAG(dag_id='07.-Create_Task_Trigger',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:
        
         t_begin = DummyOperator(task_id='begin')

         t_num = BranchPythonOperator(task_id='numbers', python_callable=print_function)

         t_pair   = BashOperator(task_id='pair', bash_command='echo branch_pair')
         t_inpair = BashOperator(task_id='inpair', bash_command='echo branch_inpair')

        #  We define the rule "none_failed_or_skipped" for us brach, because without it our "end" task won't be executed
         t_end = DummyOperator(task_id='end',
                               trigger_rule='none_failed_or_skipped')


t_begin >> t_num >> [t_pair, t_inpair]  >> t_end 