# ETL/ELT with Airflow (Google Cloud Platform)


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

![image](https://user-images.githubusercontent.com/18484807/140650529-c0ab00d8-f5e2-4636-9766-aaee2b5dbf80.png)


## Setup the GCP Bucker/Google Cloud Storage
1. Go to Cloud Storage
2. Create Bucket
3. Upload the data files

![image](https://user-images.githubusercontent.com/18484807/140650483-506d6862-8c15-4495-b06b-32ff85076e16.png)


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
1. For Dataflow, go to Dataflow menu in Big Data section
2. You can create job based on template or create it by code in your instance
3. For Big Query, go to Big Query menu in Big Data section
4. You can create your data sets and tables on your data sets

![image](https://user-images.githubusercontent.com/18484807/140650574-e45dc50b-d3eb-472b-a294-b24920689b20.png)

## Creating Data Pipeline
Main Goal: Create ETL (pipeline) process for uploading data .csv from google cloud stiorage (bucket) to google big query table

ETL (pipeline) process details:
1. Read Data (from google cloud storage)
2. Split Data (using delimiter ',')
3. Format to Dict (convert to python dictionary/JSON like format)
4. Delete Incomplete Data (remove row with NULL)
5. Change Data Type (convert data type into suitable data type such as string to int, string to date)
6. Delete Unwanted Data (drop unrelevant columns)
7. Write to Big Query (create big query table and upload final data)

reference:  https://towardsdatascience.com/apache-beam-pipeline-for-cleaning-batch-data-using-cloud-dataflow-and-bigquery-f9272cd89eba

pipeline scripts are in /pipeline folder

How to implement the ETL:
1. Upload data into Google cloud storage:
2. Create new data set in Google Big Query (note: make sure that cloud storage and big query dataset is in same/relevant region)
3. Create pipeline script
4. Run the pipeline script and monetize it in Google Data Flow
5. If it successly executed, create a DAG for airflow
6. Test and schedule the Airflow DAG

DAG script is in /dags folder 

![image](https://user-images.githubusercontent.com/18484807/141685135-7643a675-4465-4a59-b080-b1f209035d51.png)

![image](https://user-images.githubusercontent.com/18484807/141685167-c72d4229-328f-42b2-b835-6e603528309a.png)

![image](https://user-images.githubusercontent.com/18484807/141685277-e545ac4e-8bd0-4832-ab84-abb2ba180ac6.png)

![image](https://user-images.githubusercontent.com/18484807/141685292-dc89cd43-af0c-4d50-8484-81b23aa8e644.png)



