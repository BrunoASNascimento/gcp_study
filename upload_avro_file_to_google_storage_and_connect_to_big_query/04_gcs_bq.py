from google.cloud import bigquery
import os

#! Only need this if you're running this code locally.
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def upload_gs_to_gbq(dataset, table, bucket_name, file_name):
    client = bigquery.Client()
    table_ref = client.dataset(dataset).table(table)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.AVRO
    )

    uri = f'gs://{bucket_name}/{file_name}'
    load_job = client.load_table_from_uri(
        uri,
        table_ref,
        job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(table_ref)
    print(f"Loaded {destination_table.num_rows} rows in {table}.")
    return


#! Executation
dataset = 'test'
table = 'test_avro'
bucket_name = 'test_function_weather'
file_name = 'data_test.avro'

upload_gs_to_gbq(dataset, table, bucket_name, file_name)
