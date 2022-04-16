#!/usr/bin/bash


# Airflow needs a home. `~/airflow` is the default, but you can put it
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.2.5
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

# Install Airflow using the constraints file
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone

# Visit localhost:8080 in the browser and use the admin account details
# shown on the terminal to login.

echo "The directory from Airflow is $AIRFLOW_HOME and we will install Airflow version $AIRFLOW_VERSION for Python version $PYTHON_VERSION"