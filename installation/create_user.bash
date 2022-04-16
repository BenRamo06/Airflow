# Initialize the metadata database
#airflow db init

# We create a user admin

airflow users create \
    --username ben \
    --password admin \
    --firstname Ben \
    --lastname Ramos \
    --role Admin \
    --email benramos@migit.com



# Start a Airflow webserver instance with port 8080
#airflow webserver -p 8080

#Start a scheduler instance
#airflow scheduler
