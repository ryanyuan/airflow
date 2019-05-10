import airflow
from airflow.models import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryDeleteModelOperator, BigQueryGetModelOperator, BigQueryListModelOperator, BigQueryPatchModelOperator


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='bq_model',
    default_args=args,
)

# bq_delete_model = BigQueryDeleteModelOperator(
#     task_id='bq_delete_model',
#     dag=dag,
#     project_id='apiproject-980',
#     dataset_id='bqml_tutorial',
#     model_id='sample_model'
# )

bq_list_model = BigQueryListModelOperator(
    task_id='bq_list_model',
    dag=dag,
    project_id='apiproject-980',
    dataset_id='bqml_tutorial'
)

bq_get_model = BigQueryGetModelOperator(
    task_id='bq_get_model',
    dag=dag,
    project_id='apiproject-980',
    dataset_id='bqml_tutorial',
    model_id='sample_model'
)

bq_patch_model = BigQueryPatchModelOperator(
    task_id='bq_patch_model',
    dag=dag,
    project_id='apiproject-980',
    dataset_id='bqml_tutorial',
    model_id='sample_model',
    description="this is my description",
    friendly_name='haha',
    labels={"a": "b"}
)

bq_list_model >> bq_get_model >> bq_patch_model
