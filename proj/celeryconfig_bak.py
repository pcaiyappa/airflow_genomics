## Broker settings.
broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
# imports = ('tasks',)

## Using the database to store task state and results.
result_backend = 'db+postgresql://postgres:blindmelon@localhost:5432/celery_backend'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
