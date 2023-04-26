import pandas
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
import boto3

# Paste your recorded ENDPOINT and PORT in the variables below
ENDPOINT="ENDPOINT"
PORT="PORT"
USER="admin"
PASS="password"
DBNAME="mockdatabase"

fake = Faker()

mock_data = defaultdict(list)

for _ in range(2000):
    mock_data["first_name"].append( fake.first_name() )
    mock_data["last_name"].append( fake.last_name() )
    mock_data["job"].append( fake.job() )
    mock_data["dob"].append( fake.date_of_birth() )
    mock_data["country"].append( fake.country() )
    
df_mock_data = pandas.DataFrame(mock_data)

engine = create_engine(f'mysql+pymysql://{USER}:{PASS}@{ENDPOINT}:{PORT}/{DBNAME}', echo=False)

df_mock_data.to_sql('users', con=engine,index=False)
