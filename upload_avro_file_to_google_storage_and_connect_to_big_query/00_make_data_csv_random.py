import random
from datetime import datetime, timedelta, date
import pandas as pd


def create_asv(rows_data):
    list_boolean = [True, False]

    data = [
        {
            'test_string': 'Test',
            'test_boolean': random.choice(list_boolean),
            'test_datetime': datetime.utcnow(),
            'test_date': date.today(),
            'test_float': round(random.random(), 10),
            'test_integer': random.randint(0, 1000000000),
            'control_integer': i
        }
        for i in range(rows_data)
    ]

    # Create data frame
    df = pd.DataFrame(data)
    print(df.head(10))
    print(f'Shape: {df.shape}')

    # Save data frame
    df.to_csv('data/data_test.csv', index=False)

    return


#! Executation
rows_data = 5000  # Number rows
create_asv(rows_data)
