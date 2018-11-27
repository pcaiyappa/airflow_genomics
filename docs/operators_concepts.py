# from datetime import datetime, timedelta
#
# from airflow import DAG
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.python_operator import PythonOperator
# from airflow.operators.bash_operator import BashOperator
#
#
#
# """default arguments"""
# default_args = {'start_date': datetime(2016, 1, 1),
#                 'owner': 'Airflow'
#                 }
#
#
# """dags must be in global scope to be imported from a DAGfile -> a file that contains 'airflow' and 'DAG' strings in it.
# For example, a common pattern with SubDagOperator is to define the subdag inside a function so that Airflow
# doesn’t try to load it as a standalone DAG."""
# dag = DAG('my_dag', default_args=default_args)
# op = DummyOperator(task_id='dummy', dag=dag)
# print(op.owner)
#
#
# """ DAGs can be used as context managers to automatically assign new operators to that DAG."""
# with DAG('my_dag', start_date=datetime(2016, 1, 1)) as dag:
#         op = DummyOperator('op')
#
# op.dag is dag  # should be true
#
# """DAG assignment. explicit, deferred or inferred from other operators"""
# dag = DAG('my_dag', start_date=datetime(2016, 1, 1))
#
# # sets the DAG explicitly
# explicit_op = DummyOperator(task_id='op1', dag=dag)
#
# # deferred DAG assignment
# deferred_op = DummyOperator(task_id='op2')
# deferred_op.dag = dag
#
# # inferred DAG assignment (linked operators must be in the same DAG)
# inferred_op = DummyOperator(task_id='op3')
# inferred_op.set_upstream(deferred_op)
#
#
# """Bitshift Composition. The following four statements are all functionally equivalent."""
# op1 = DummyOperator('op1')
# op2 = DummyOperator('op2')
# op3 = DummyOperator('op3')
# op4 = DummyOperator('op4')
#
# op1 >> op2
# op1.set_downstream(op2)
#
# op2 << op1
# op2.set_upstream(op1)
#
# op1 >> op2 >> op3 << op4
# op1.set_downstream(op2)
# op2.set_downstream(op3)
# op3.set_upstream(op4)
#
# # For convenience, the bitshift operators can also be used with DAGs. For example, functionally equivalent statements:
# dag >> op1 >> op2
# op1.dag = dag
# op1.set_downstream(op2)
#
#
# """Simple pipeline"""
# with DAG('my_dag', start_date=datetime(2016, 1, 1)) as dag:
#     (
#         DummyOperator(task_id='dummy_1')
#         >> BashOperator(
#             task_id='bash_1',
#             bash_command='echo "HELLO!"')
#         >> PythonOperator(
#             task_id='python_1',
#             python_callable=lambda: print("GOODBYE!"))
#     )
