# Airflow

### Installation

We will install Airflow with **"pip"** where we will specify: 

* **_[Directory: where Airflow is going to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Airflow version: Airflow version to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Python version: Installation with a specify version of Python (example: 3.8).](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**

Once installed, go to directory and open **standalone_admin_password.txt** file, it contains the password of admin user.

Go to localhost:8080 and login with admin user and password that previously you copied.

We can create a **_[new users](https://github.com/BenRamo06/Airflow/blob/master/installation/create_user.bash)_** with the next roles:



___
### Concepts

Airflow is a platform that lets you build and run workflows. A workflow is represented as a DAG (a Directed Acyclic Graph), and contains individual pieces of work called Tasks, arranged with dependencies and data flows taken into account.

An Airflow installation generally consists of the following components:

* **Scheduler:** which handles both triggering scheduled workflows, and submitting Tasks to the executor to run.

* **Executor:** which handles running tasks. In the default Airflow installation, this runs everything inside the scheduler, but most production-suitable executors actually push task execution out to workers.

* **Webserver:** which presents a handy user interface to inspect, trigger and debug the behaviour of DAGs and tasks.

* **Folder of DAG files:** read by the scheduler and executor (and any workers the executor has)

* **Metadata database:** used by the scheduler, executor and webserver to store state.

___

### DAG (Directed Acyclic Graph)

Is the core concept of Airflow, collecting Tasks together, organized with dependencies and relationships to say how they should run.

The DAG itself doesn't care about what is happening inside the tasks; it is merely concerned with how to execute them - the order to run them in, how many times to retry them, if they have timeouts, and so on.




<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/DAG.png">
</p>





*   dag_id=<str> : identify of DAG *MANDATORY*
*   description=<str> : description of DAG
*   start_date=<datetime> : when the DAG will begin to execute *MANDATORY*
*   end_date=<datetime> : when the DAG will finish to execute
*   tags=<list[string[,string..]]> : assign it tags to identify more fast our DAGs in webserver
*   catchup=<boolean>: it indicates if we can execute this DAG before of start_date (False), if is not possible "True"
*   schedule_interval=<present|cron>: indicate periods of time where the DAG will be executed. We can us present or [cron](#CronSpecifications) like next table:

preset|meaning|cron
------|-------|----
None|Don't schedule; use exclusively "externally triggered" DAGs.|
@once|Schedule once and only once|
@hourly|Run once an hour at the beginning of the hour|0 * * * *
@daily|Run once a day at midnight|0 0 * * *
@weekly|Run once a week at midnight on Sunday morning|0 0 * * 0
@monthly|Run once a month at midnight on the first day of the month|0 0 1 * *
@yearly|Run once a year at midnight of January 1|0 0 1 1 *

___


### Task

A Task is the basic unit of execution in Airflow. Tasks are arranged into DAGs, and then have upstream and downstream dependencies set between them into order to express the order they should run in.

There are three basic kinds of Task:

* Operators, predefined task templates that you can string together quickly to build most parts of your DAGs.

* Sensors, a special subclass of Operators which are entirely about waiting for an external event to happen.

* A TaskFlow-decorated ```@task```, which is a custom Python function packaged up as a Task.


#### Dependencies/ Control Flow

A Task/Operator does not usually live alone; it has dependencies on other tasks (those upstream of it), and other tasks depend on it (those downstream of it. Declaring these dependencies between tasks is what makes up the DAG structure (the edges of the directed acyclic graph).

There are two main ways to declare individual task dependencies. 

 The recommended one is to use the >> and << operators:

```python
first_task >> [second_task, third_task]
fourth_task << third_task
```

Or, you can also use the more explicit set_upstream and set_downstream methods:

```python
first_task.set_downstream([second_task, third_task])
fourth_task.set_upstream(third_task)
```

#### Operators

While DAGs describe how to run a workflow, Operators determine what actually gets done by a task.

An operator describes a single task in a workflow. Operators are usually (but not always) atomic, meaning they can stand on their own and don’t need to share resources with any other operators. The DAG will make sure that operators run in the correct order; other than those dependencies, operators generally run independently. In fact, they may run on two completely different machines.

```python
with DAG("my-dag") as dag:
    ping = SimpleHttpOperator(endpoint="http://example.com/update/")
    email = EmailOperator(to="admin@example.com", subject="Update complete")

    ping >> email
```

Operator examples: SimpleHttpOperator and EmailOperator

Airflow has a very extensive set of operators available, with some built-in to the core or pre-installed providers. Some popular operators from core include:

* BashOperator - executes a bash command
* PythonOperator - calls an arbitrary Python function
* EmailOperator - sends an email


#### Branch


#### Cron Specifications


To support more complicated scheduling intervals, Airflow allows us to define scheduling intervals using the same syntax as used by cron, a time-based job scheduler used by Unix-like computer operating systems such as macOS and Linux. This syntax consists of five components and is defined as follows:

```
┌─────── minute (0 - 59)
│ ┌────── hour (0 - 23)
│ │ ┌───── day of the month (1 - 31)
│ │ │ ┌───── month (1 - 12)
│ │ │ │ ┌──── day of the week (0 - 6) (Sunday to Saturday;
│ │ │ │ │       7 is also Sunday on some systems)
* * * * *
```

Examples:

* 0 * * * * = hourly (running on the hour)
* 0 0 * * * = daily (running at midnight)
* 0 0 * * 0 = weekly (running at midnight on Sunday)
* 0 0 1 * * = midnight on the first of every month
* 45 23 * * SAT = 23:45 every Saturday







**_[Create DAG](https://github.com/BenRamo06/Airflow/blob/master/pipeline/01.-Create_DAG.py)_** *We can create a DAG wit standard constructor or context manager*

**_[Create Task](https://github.com/BenRamo06/Airflow/blob/master/pipeline/02.-Create_Task.py)_** *Create a task in a DAG*

**_[Task Dependencies](https://github.com/BenRamo06/Airflow/blob/master/pipeline/03.-Create_Task_Dependencies.py)_** *Create DAG with tasks dependencies*

**_[Task Multiple Dependencie](https://github.com/BenRamo06/Airflow/blob/master/pipeline/04.-Create_Task_Multiple_Dependencies.py)_** *Create DAG with multiple tasks dependencies*

**_[Task Branchs](https://github.com/BenRamo06/Airflow/blob/master/pipeline/05.-Branch_Process.py)_** *Create DAG with Branch defined*


providers GCP

https://github.com/apache/airflow/tree/main/airflow/providers/google/cloud/example_dags
https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html