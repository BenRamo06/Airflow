from random import random
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import random



# we get ti = Task instace from DAG

def get_value(ti):
    n = random.randint(1,10)
    print("El valor random es", n)
    if n%2==0:
        ti.xcom_push(key='get_value', value='par' )  
    else:
        ti.xcom_push(key='get_value', value='impar' )


def receive_value(ti):
    value = ti.xcom_pull(key='get_value',task_ids=['obtain_value'])
    print("el valor heredado es",value)




with DAG(dag_id='08.-XCom_Variables',
         description= 'this is mi first dag',
         start_date= datetime(year=2022, month=4, day=15),
         tags=['learn','globant'],
         catchup=False) as dag:
        
         t_begin = DummyOperator(task_id='begin')


         t_get = PythonOperator(task_id='obtain_value', python_callable=get_value)

         t_rec = PythonOperator(task_id='take_value', python_callable=receive_value)

         t_end = DummyOperator(task_id='end')





t_begin >> t_get >> t_rec >> t_end