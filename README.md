# Airflow

### Installation

We will install Airflow with **"pip"** where we will specify: 

* **_[Directory: where Airflow is going to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Airflow version: Airflow version to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Python version: Installation with a specify version of Python (example: 3.8).](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**

Once installed, go to directory and open **standalone_admin_password.txt** file, it contains the password of admin user.

Go to localhost:8080 and login with admin user and password that previously you copied.

We can create a **_[new users](https://github.com/BenRamo06/Airflow/blob/master/installation/create_user.bash)_** with the next roles:

### Concepts and Architecture

Airflow is a platform that lets you build and run workflows. A workflow is represented as a DAG (a Directed Acyclic Graph), and contains individual pieces of work called Tasks, arranged with dependencies and data flows taken into account.

An Airflow installation generally consists of the following components:

* **Scheduler:** which handles both triggering scheduled workflows, and submitting Tasks to the executor to run.

* **Workers:** Pick up tasks that are scheduled for execution and execute them. As such, the workers are responsible for actually “doing the work.”

* **Webserver:** which presents a handy user interface to inspect, trigger and debug the behaviour of DAGs and tasks.

* **Folder of DAG files:** read by the scheduler and executor (and any workers the executor has)

* **Metadata database:** used by the scheduler, executor and webserver to store state.

<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/Architecture.png">
</p>


### DAG (Directed Acyclic Graph)

In Airflow, you define your DAGs using Python code in DAG files, which are essentially Python scripts that describe the structure of the corresponding DAG. As such,each DAG file typically describes the set of tasks for a given DAG and the dependencies between the tasks, which are then parsed by Airflow to identify the DAG structure.

The DAG itself doesn't care about what is happening inside the tasks; it is merely concerned with how to execute them - the order to run them in, how many times to retry them, if they have timeouts, and so on.


<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/DAG.png">
</p>

*   dag_id=<str> : DAG indentify, it will be displayed un Airflow user interface *MANDATORY*
*   description=<str> : description of DAG
*   start_date=<datetime> : when the DAG will begin to execute *MANDATORY*
*   end_date=<datetime> : when the DAG will finish to execute
*   tags=<list[string[,string..]]> : assign it tags to identify more fast our DAGs in webserver
*   catchup=<boolean>: it indicates if we can execute this DAG before of start_date (False), if is not possible "True"
*   dagrun_timeout=<timedelta>: maximum time to execute a DAG
*   schedule_interval=<present|cron|None(manual)|timedelta>: indicate periods of time where the DAG will be executed. We can use present or [cron expressions](https://crontab.guru) like next table:

preset|meaning|cron
------|-------|----
None|Don't schedule; use exclusively "externally triggered" DAGs.|
@once|Schedule once and only once|
@hourly|Run once an hour at the beginning of the hour|0 * * * *
@daily|Run once a day at midnight|0 0 * * *
@weekly|Run once a week at midnight on Sunday morning|0 0 * * 0
@monthly|Run once a month at midnight on the first day of the month|0 0 1 * *
@yearly|Run once a year at midnight of January 1|0 0 1 1 *


*   default_args=<dict>: dict with properties for DAG
    *   owner=<str>: name of owner (is a metadata value in webserver)
    *   retries=<int>: number of tries if a task fail
    *   retry_delay=<timedelta>: time(seconds,minutes,hours,days...) that task must wait to execute again



### Task

A Task is the basic unit of execution in Airflow. Tasks are arranged into DAGs, and then have upstream and downstream dependencies set between them into order to express the order they should run in.

There are three basic kinds of Task:

* Operators, predefined task templates that you can string together quickly to build most parts of your DAGs.

* Sensors, a special subclass of Operators which are entirely about waiting for an external event to happen.

* A TaskFlow-decorated ```@task```, which is a custom Python function packaged up as a Task.


<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/Taks.png">
</p>

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


#### Triggers

Trigger rules are essentially the conditions that Airflow applies to tasks to determine whether they are ready to execute.      
Airflow’s default trigger rule is all_success , which states that all of a task’s dependencies must have completed successfully before the task itself can be executed



Trigger rule|Behavior|Example use case
------|------|------
all_success (default)|Triggers when all parent tasks have been completed successfully|The default trigger rule for a normal workflow
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/all_success.png">
</p>
all_failed|Triggers when all parent tasks have failed (or have failed as a result of a failure in their parents)|Trigger error handling code in situations where you expected at least one success among a group of tasks
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/all_failed.png">
</p>
all_done|Triggers when all parents are done with their execution, regardless of their resulting state|Execute cleanup code that you want to execute when all tasks have finished (e.g., shutting down a machine or stopping a cluster)
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/all_done.png">
</p>
one_failed|Triggers as soon as at least one parent has failed; does not wait for other parent tasks to finish executing|Quickly trigger some error handling code, such as notifications or rollbacks
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/one_failed.png">
</p>
one_success|Triggers as soon as one parent succeeds; does not wait for other parent tasks to finish executing|Quickly trigger downstream computations/notifications as soon as one result becomes available
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/one_success.png">
</p>
none_failed|Triggers if no parents have failed but have either completed successfully or been skipped|Join conditional branches in Airflow DAGs, as shown in section 5.2
<p align="center">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/none_failed.png">
</p>
none_skipped|Triggers if no parents have been skipped but have either completed successfully or failed|Trigger a task if all upstream tasks were executed, ignoring their result(s)
dummy|Triggers regardless of the state of any upstream tasks|Testing

### UI

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/Login.png">
</p>

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/Home.png">
</p>

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/GraphView.png">
</p>

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/GraphViewRunning.png">
</p>

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/ThreeView.png">
</p>

<p align="left">
  <img src="https://github.com/BenRamo06/Airflow/blob/master/images/GraphViewTasks.png">
</p>


### Codes


**_[Create DAG](https://github.com/BenRamo06/Airflow/blob/master/pipeline/01.-Create_DAG.py)_** *We can create a DAG wit standard constructor or context manager*

**_[Create Task](https://github.com/BenRamo06/Airflow/blob/master/pipeline/02.-Create_Task.py)_** *Create a task in a DAG*

**_[Task Dependencies](https://github.com/BenRamo06/Airflow/blob/master/pipeline/03.-Create_Task_Dependencies.py)_** *Create DAG with tasks dependencies*

**_[Task Multiple Dependencie](https://github.com/BenRamo06/Airflow/blob/master/pipeline/04.-Create_Task_Multiple_Dependencies.py)_** *Create DAG with multiple tasks dependencies*

**_[Task Branchs](https://github.com/BenRamo06/Airflow/blob/master/pipeline/05.-Branch_Process.py)_** *Create DAG with Branch defined*

**_[Python Operator Params](https://github.com/BenRamo06/Airflow/blob/master/pipeline/06.-Create_Task_Params.py)_** *Create DAG will use Python Operator with parameters*


All task context variables
Key|Description|Example
------|------|------
conf|Provides access to Airflow configuration|airflow.configuration.AirflowConfigParser object
dag|The current DAG object|DAG object
dag_run|The current DagRun object|DagRun object
ds|execution_date formatted as %Y-%m-%d|“2019-01-01”
ds_nodash|execution_date formatted as %Y%m%d|“20190101”
execution_date|The start datetime of the task’s interval|pendulum.datetime.DateTime object
inlets|Shorthand for task.inlets, a feature to track input data sources for data lineage|[]
macros|airflow.macros module| macros module
next_ds|execution_date of the next interval (= end of current interval) formatted as %Y-%m-%d|“2019-01-02”
next_ds_nodash|execution_date of the next interval (= end of current interval) formatted as %Y%m%d|“20190102”
next_execution_date|The start datetime of the task’s next interval (= end of current interval)|pendulum.datetime.DateTime object
outlets|Shorthand for task.outlets, a feature to track output data sources for data lineage| []
params|User-provided variables to the task context|{}
prev_ds|execution_date of the previous interval formatted as %Y-%m-%d|“2018-12-31”
prev_ds_nodash|execution_date of the previous interval formatted as %Y%m%d|“20181231”
prev_execution_date|The start datetime of the task’s previous interval|pendulum.datetime.DateTime object
prev_execution_date_succes|Start datetime of the last successfully completed run of the same task (only in past)|pendulum.datetime.DateTime object
prev_start_date_success|Date and time on which the last successful run of the same task (only inpast) was started|pendulum.datetime.DateTime object
run_id|The DagRun’s run_id (a key typically composed of a prefix + datetime)| “manual__2019-01-01T00:00:00+00:00”
task|The current operator|PythonOperator object
task_instance|The current TaskInstance object|TaskInstance object
task_instance_key_str|A unique identifier for the current TaskInstance ({dag_id}__{task_id}__{ds_nodash})|“dag_id__task_id__20190101”
templates_dict|User-provided variables to the task context|{}
test_mode|Whether Airflow is running in test mode (configuration property)|False
ti|The current TaskInstance object,same as task_instance|TaskInstance object
tomorrow_ds|ds plus one day|“2019-01-02”
tomorrow_ds_nodash|ds_nodash plus one day|“20190102”
ts|execution_date|formatted according to ISO8601 format|“2019-01-01T00:00:00+00:00”
ts_nodash|execution_date formatted as %Y%m%dT%H%M%S|“20190101T000000”
ts_nodash_with_tz|ts_nodash with time zone information|“20190101T000000+0000”
var|Helpers objects for dealing with Airflow variables|{}
yesterday_ds|ds minus one day|“2018-12-31”
yesterday_ds_nodash|ds_nodash minus one day|“20181231”


**_[Task with Trigger rules](https://github.com/BenRamo06/Airflow/blob/master/pipeline/07.-Create_Task_Trigger.py)_** *Create DAG with task and trigger*



providers GCP

https://github.com/apache/airflow/tree/main/airflow/providers/google/cloud/example_dags
https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/index.html