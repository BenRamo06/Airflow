# Airflow

### Installation

We will install Airflow with **"pip"** where we will specify: 

* **_[Directory: where Airflow is going to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Airflow version: Airflow version to be installed.](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**
* **_[Python version: Installation with a specify version of Python (example: 3.8).](https://github.com/BenRamo06/Airflow/blob/master/installation/pipinstall.bash)_**

Once installed, go to directory and open **standalone_admin_password.txt** file, it contains the password of admin user.

Go to localhost:8080 and login with admin user and password that previously you copied.

<!-- 
<p align="center">
  <img src="https://github.com/BenRamo06/PySpark/blob/master/images/ems5cAs.png">
</p> -->

### Concepts

Airflow is a platform that lets you build and run workflows. A workflow is represented as a DAG (a Directed Acyclic Graph), and contains individual pieces of work called Tasks, arranged with dependencies and data flows taken into account.

A DAG specifies the dependencies between Tasks, and the order in which to execute them and run retries; the Tasks themselves describe what to do, be it fetching data, running analysis, triggering other systems, or more.


An Airflow installation generally consists of the following components:

* **Scheduler:** which handles both triggering scheduled workflows, and submitting Tasks to the executor to run.

* **Executor:** which handles running tasks. In the default Airflow installation, this runs everything inside the scheduler, but most production-suitable executors actually push task execution out to workers.

* **Webserver:** which presents a handy user interface to inspect, trigger and debug the behaviour of DAGs and tasks.

* **Folder of DAG files:** read by the scheduler and executor (and any workers the executor has)

* **Metadata database:** used by the scheduler, executor and webserver to store state.


### Control Flow

Tasks have dependencies declared on each other. You'll see this in a DAG either using the >> and << operators:

```python
first_task >> [second_task, third_task]
fourth_task << third_task
```

Or, with the set_upstream and set_downstream methods:

```python
first_task.set_downstream([second_task, third_task])
fourth_task.set_upstream(third_task)
```