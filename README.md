# ETL/ELT with Google Cloud Platform


This is ETL/ELT script for Google Cloud Platform.

## Tools:
1. Google Cloud Platform (GCP) including: <br />
  · GCP Instance <br />
  · GCP Bucket/Cloud Storage <br />
  · GCP BigQuery <br />
  · GCP DataFlow <br />
2. Docker
3. Airflow
4. Python

## Dataset:
1. Search Engine Result (on Flight & Ticker keyword) datasets

## Setup The GCP Service Account & Project
1. Login to your GCP account
2. Go to IAM & Admin > Service Accounts
3. Create a Service Account (Give minimum access to BigQuery (BigQuery Job User role) and Dataflow (Dataflow Worker role))
4. Get and keep key-file.json
5. Create a project

## Setup The GCP Instance
1. Go to Compute Engine > VM Instances
2. Create a Instance with spec: e2-standard-2 (2vCPU, 8GB memory), OS Debian 10, 50 GB HDD

## Setup the GCP Bucker/Google Cloud Storage
1. Go to Cloud Storage
2. Create Bucket
3. Upload the data files

## Setup GCP connection firewall
1. Go to VPC Network > Firewall
2. Create airflow-port rule (IPv4 ranges 0.0.0.0/0, tcp 8080)
3. On your instance, check all the firewall boxes, and add the airflow-port into the network tags) 

source: https://medium.com/apache-airflow/a-simple-guide-to-start-using-apache-airflow-2-on-google-cloud-1811c2127445

## Setup the Docker & Airflow
1. Go to your instance and start the instance 
2. Go to SSH > open the command window
3. Install the docker in your GCP instance
4. Install the docker compose
5. Create (or download) the docker-compose (.yaml) file
6. Initalizing the Airflow Environment (docker-compose up airflow-init)
7. Start the services (docker-compose up -d), make sure that the airflow didn't have any trouble.
8. Open the Airflow GUI on (gcp-external-ip):8080
9. Create GCP connection in Airflow Connection menu (conn type: Google Cloud, keyfile json: copy paste from the gcp json key file) 

source: https://medium.com/codebrace/working-on-on-prem-external-airflow-with-google-cloud-platform-gcp-5b2e77b0e3ba

## Settup the GCP Dataflow & Bigquery

