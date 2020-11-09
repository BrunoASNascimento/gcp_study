# Google Cloud Plataform study

The codes present in the repository are for the use of [Google Cloud Platform](https://console.cloud.google.com/freetrial).

## Upload Avro file to Google Storage and connect to Big Query

### Create data:

Before the update, it is necessary to create the dataset in the `data` directory, the code `00_make_data_csv_random.py` creates a csv with random data.

### Convert csv to Avro:

After the data generated it is necessary to convert csv to Avro, the code `01_csv_to_avro.py` does this. A very important point, if your data contains fields with date, datetime or timestamp it is necessary to convert these fields, the code has an example.

### Upload Avro file to Google Storage

The `02_upload_gcs.py` code does this, but it is necessary to do `.env` with the `export GOOGLE_APPLICATION_CREDENTIALS = <your_gcp_key.json>` parameter.

### Create table in Big Query

The `03_create_table_bq.py` code does this, but it is necessary to do `.env` with the `export GOOGLE_APPLICATION_CREDENTIALS = <your_gcp_key.json>` parameter.

### Google storage connected to Big Query

The `04_gcs_bq.py` code does this, but it is necessary to do `.env` with the `export GOOGLE_APPLICATION_CREDENTIALS = <your_gcp_key.json>` parameter.

## Comments

The codes present in the repository have no connection with any company or group, the codes are for exclusive use for study with Google Cloud Platform.

## More

- [pandavro](https://github.com/ynqa/pandavro)
- [python dotenv](https://github.com/theskumar/python-dotenv)
- [(GCP) creating column partitions](https://cloud.google.com/bigquery/docs/creating-column-partitions#python)
- [(GCP) loading data cloud storage avro](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#python)
