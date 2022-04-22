#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
# [START tutorial]
# [START import_module]
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.providers.sftp.operators.sftp import SFTPOperator

# [END import_module]


# [START instantiate_dag]
with DAG(
    'SFTP-Hack-a-ton',
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['ruud.cools@tennet.eu'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        # 'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    # [END default_args]
    description='A dag that ingests a file from a sftp source',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    # [END instantiate_dag]

    # [START basic_task]
    get_file = SFTPOperator(
        task_id="get_file",
        ssh_conn_id="sftp-hack-a-ton",
        local_filepath="/tmp/file.txt",
        remote_filepath="/stuff.txt",
        operation="get",
        create_intermediate_dirs=True,
        dag=dag
    )

    put_file = SFTPOperator(
        task_id="put_file",
        ssh_conn_id="sftp-hack-a-ton",
        local_filepath="/tmp/file.txt",
        remote_filepath="/tmp/tmp1/tmp2/file.txt",
        operation="put",
        create_intermediate_dirs=True,
        dag=dag
    )

# [END tutorial]