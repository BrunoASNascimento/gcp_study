from google.cloud import bigquery


#! Only need this if you're running this code locally.
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def create_table_bq(dataset, table_name, schema, field):

    client = bigquery.Client()
    project = client.project
    dataset_ref = bigquery.DatasetReference(project, dataset)

    table_ref = dataset_ref.table(table_name)
    schema = [
        bigquery.SchemaField(key, value)
        for key, value in schema.items()
    ]
    table = bigquery.Table(table_ref, schema=schema)
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field=field,  # name of column to use for partitioning
        require_partition_filter=True
    )

    table = client.create_table(table)

    print(
        f"Created table {table.table_id}, partitioned on column {table.time_partitioning.field}")

    return


#! Executation
dataset = 'test'
table_name = 'test_avro'
field = 'test_datetime'
schema = {
    'test_string': 'STRING',
    'test_boolean': 'BOOLEAN',
    'test_datetime': 'TIMESTAMP',
    'test_date': 'INTEGER',
    'test_float': 'FLOAT',
    'test_integer': 'INTEGER',
    'control_integer': 'INTEGER'
}

create_table_bq(dataset, table_name, schema, field)
