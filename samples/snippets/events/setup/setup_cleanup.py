# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime
import os
import re
import shlex
import subprocess

from google.api_core.client_options import ClientOptions
from google.cloud import storage
from google.cloud.retail import ProductDetail, PurgeUserEventsRequest, \
    UserEvent, UserEventServiceClient, WriteUserEventRequest
from google.cloud.retail_v2 import Product
from google.protobuf.timestamp_pb2 import Timestamp

project_number = os.getenv('PROJECT_NUMBER')
endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_number)


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get user event
def get_user_event(visitor_id):
    timestamp = Timestamp()
    timestamp.seconds = int(datetime.datetime.now().timestamp())

    product = Product()
    product.id = 'test_id'

    product_detail = ProductDetail()
    product_detail.product = product

    user_event = UserEvent()
    user_event.event_type = "detail-page-view"
    user_event.visitor_id = visitor_id
    user_event.event_time = timestamp
    user_event.product_details = [product_detail]

    print(user_event)
    return user_event


# write user event
def write_user_event(visitor_id):
    write_user_event_request = WriteUserEventRequest()
    write_user_event_request.user_event = get_user_event(visitor_id)
    write_user_event_request.parent = default_catalog
    user_event = get_user_events_service_client().write_user_event(
        write_user_event_request)
    print("---the user event is written---")
    print(user_event)
    return user_event


# purge user event
def purge_user_event(visitor_id):
    purge_user_event_request = PurgeUserEventsRequest()
    purge_user_event_request.filter = 'visitorId="{}"'.format(visitor_id)
    purge_user_event_request.parent = default_catalog
    purge_user_event_request.force = True
    purge_operation = get_user_events_service_client().purge_user_events(
        purge_user_event_request)

    print("---the purge operation was started:----")
    print(purge_operation.operation.name)


def get_project_id():
    get_project_command = "gcloud config get-value project --format json"
    config = subprocess.check_output(shlex.split(get_project_command))
    project_id = re.search('\"(.*?)\"', str(config)).group(1)
    return project_id


def create_bucket(bucket_name: str):
    """Create a new bucket in Cloud Storage"""
    print("bucket name:" + bucket_name)
    buckets_in_your_project = str(list_buckets())
    if bucket_name in buckets_in_your_project:
        print("Bucket {} already exists".format(bucket_name))
    else:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = "STANDARD"
        new_bucket = storage_client.create_bucket(bucket, location="us")
        print(
            "Created bucket {} in {} with storage class {}".format(
                new_bucket.name, new_bucket.location, new_bucket.storage_class
            )
        )
        return new_bucket


def list_buckets():
    """Lists all buckets"""
    bucket_list = []
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        bucket_list.append(str(bucket))
        print(bucket.name)
    return bucket_list


def upload_blob(bucket_name, source_file_name):
    """Uploads a file to the bucket."""
    # The path to your file to upload
    # source_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    object_name = re.search('resources/(.*?)$', source_file_name).group(1)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, object_name
        )
    )


def create_bq_dataset(dataset_name):
    """Create a BigQuery dataset"""
    if dataset_name not in list_bq_datasets():
        create_dataset_command = 'bq --location=US mk -d --default_table_expiration 3600 --description "This is my dataset." {}:{}'.format(
            get_project_id(), dataset_name)
        subprocess.check_output(shlex.split(create_dataset_command))
    else:
        print("dataset {} already exists".format(dataset_name))


def list_bq_datasets():
    """List BigQuery datasets in the project"""
    list_dataset_command = "bq ls --project_id {}".format(get_project_id())
    datasets = subprocess.check_output(shlex.split(list_dataset_command))
    print(datasets)
    return str(datasets)


def create_bq_table(dataset, table_name, schema):
    """Create a BigQuery table"""
    if table_name not in list_bq_tables(dataset):
        create_table_command = "bq mk --table {}:{}.{} {}".format(
            get_project_id(),
            dataset,
            table_name, schema)
        output = subprocess.check_output(shlex.split(create_table_command))
        print(output)
    else:
        print("table {} already exists".format(table_name))


def list_bq_tables(dataset):
    """List BigQuery tables in the dataset"""
    list_tables_command = "bq ls {}:{}".format(get_project_id(), dataset)
    tables = subprocess.check_output(shlex.split(list_tables_command))
    print("tables:")
    print(tables)
    return str(tables)


def upload_data_to_bq_table(dataset, table_name, source, schema):
    """Upload data to the table from specified source file"""
    upload_data_command = "bq load --source_format=NEWLINE_DELIMITED_JSON {}:{}.{} {} {}".format(
        get_project_id(), dataset, table_name, source, schema)
    output = subprocess.check_output(shlex.split(upload_data_command))
    print(output)
