from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'charan',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='s3_to_snowflake_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Load CSV from S3 to Snowflake'
) as dag:

    load_data = SnowflakeOperator(
        task_id='load_data_to_snowflake',
        sql="""
            COPY INTO adult_data
            FROM @my_s3_stage/eda_cleaned_adult.csv
            FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);
        """,
        snowflake_conn_id='snowflake_default'
    )

    load_data

