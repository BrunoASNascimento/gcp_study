from avro.datafile import DataFileReader
from avro.io import DatumReader

reader = DataFileReader(open("data/data_test.avro", "rb"), DatumReader())
for user in reader:
    print(user)
