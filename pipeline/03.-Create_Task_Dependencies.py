from platform import python_branch
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(dag_id='03.-Create_Task_Dependencies',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:

        # We create a task with an operator (DummyOperator) 
         t_begin = DummyOperator(task_id='begin')

         t_hello = BashOperator(task_id='printHello', bash_command='echo Hello')

         # We create a task with an operator (DummyOperator) 
         t_end = DummyOperator(task_id='end')


# We specify steps in our DAG
# One time t_begin has been executed, t_end will be executed .
t_begin >> t_hello >> t_end

# Other ways to specify t_begin >> t_hello
t_begin.set_downstream(t_hello)
t_hello.set_upstream(t_begin)
t_hello << t_begin

# Other ways to specify t_hello >> t_end
t_hello.set_downstream(t_end)
t_end.set_upstream(t_hello)
t_end << t_hello