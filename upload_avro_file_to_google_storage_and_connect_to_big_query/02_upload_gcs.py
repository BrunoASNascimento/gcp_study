from google.cloud import storage

#! Only need this if you're running this code locally.
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def upload_csv(INPUT_PATH, bucket_name, file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    bucket.blob(file_name).upload_from_filename(
        INPUT_PATH)

    print(f'Document uploaded {file_name} in {bucket_name}')

    return


#! Executation
INPUT_PATH = 'data/data_test.avro'
bucket_name = 'test_function_weather'
file_name = 'data_test.avro'
upload_csv(INPUT_PATH, bucket_name, file_name)
