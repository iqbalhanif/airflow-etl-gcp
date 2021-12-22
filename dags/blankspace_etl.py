from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1, 
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id = 'blankspace_etl',
    start_date = datetime(2020,9,11),
    schedule_interval = '0 0 * * *',
    default_args=default_args
)

# ETL with bash 

bash_etl1 = BashOperator(
    task_id='beers_etl',
    bash_command='python3 /home/iqbal_hanif_ipb/gcp/docker-local/pipeline/batch-beers.py --runner DataFlowRunner --project amiable-crane-330914 --temp_location gs://blankspace89783/batch/temp --staging_location gs://blankspace89783/batch/stag --region us-central1 --job_name drinkbeer',
    dag=dag,
)

bash_etl2 = BashOperator(
    task_id='citizens_etl',
    bash_command='python3 /home/iqbal_hanif_ipb/gcp/docker-local/pipeline/batch-citizen.py --runner DataFlowRunner --project amiable-crane-330914 --temp_location gs://blankspace89783/batch/temp --staging_location gs://blankspace89783/batch/stag --region us-central1 --job_name citizensregister',
    dag=dag,
)

bash_etl3 = BashOperator(
    task_id='flight_etl',
    bash_command='python3 /home/iqbal_hanif_ipb/gcp/docker-local/pipeline//batch-flight.py --runner DataFlowRunner --project amiable-crane-330914 --temp_location gs://blankspace89783/batch/temp --staging_location gs://blankspace89783/batch/stag --region us-central1 --job_name flight',
    dag=dag,
)


#DAG order

bash_etl1 >> bash_etl2 >> bash_etl3
