import datetime
from airflow import DAG

default_args = {'start_date': datetime(2016, 1, 1),
                'owner': 'Airflow'
                }

dag = DAG('my_dag')


