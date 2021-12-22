import os
from airflow import DAG
from airflow.providers.apache.beam.operators.beam import BeamRunPythonPipelineOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowConfiguration
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow import configuration
from airflow.models import Variable
from datetime import datetime


args = {
 
    'owner': 'iqbalhanif',
    'start_date': datetime(2021,10,30),
    'retries' : 1,
}

PROJECT_ID = 'amiable-crane-330914'
PY_FILE = ('gs://blankspace89783/batch-flight.py')

pipeline_options = {'tempLocation': "gs://blankspace89783/batch/stag" ,
                    'stagingLocation': "gs://blankspace89783/batch/temp",
                        }


dag = DAG(dag_id = 'dag_etl_gcp', default_args=args,catchup=False, schedule_interval='@daily')
 
with dag:
    dataflow_task = BeamRunPythonPipelineOperator(
        task_id='job_keyword_search_gcs_to_bigquery',
        runner='DataflowRunner',
        gcp_conn_id='google_cloud_default',
        py_file=PY_FILE,
        py_requirements=['apache-beam[gcp]==2.34.0'],
        py_system_site_packages=True,
        py_interpreter='python3',
        pipeline_options=pipeline_options,
        dataflow_config=DataflowConfiguration(
            job_name="job_keyword_search_{{ ds_nodash }}",
            project_id=PROJECT_ID,
            location="asia-southeast1",
            wait_until_finished=True
        )
    )
    dataflow_task