import pandas as pd
import pandavro as pdx


def converter_csv_to_avro(INPUT_PATH, OUTPUT_PATH, converter_to_datetime):
    df = pd.read_csv(INPUT_PATH)

    # Trasnform columns string to datetime
    for columns_to_converter in converter_to_datetime:
        df[columns_to_converter] = pd.to_datetime(df[columns_to_converter])

    print(df.info())

    pdx.to_avro(OUTPUT_PATH, df)  # Converter
    saved = pdx.read_avro(OUTPUT_PATH)  # Only read to control

    print(saved)

    return


#! Executation
INPUT_PATH = 'data/data_test.csv'
OUTPUT_PATH = 'data/data_test.avro'
converter_to_datetime = ['test_datetime', 'test_date']
converter_csv_to_avro(INPUT_PATH, OUTPUT_PATH, converter_to_datetime)
