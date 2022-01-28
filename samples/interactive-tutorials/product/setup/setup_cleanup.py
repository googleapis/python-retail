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

import os
import re
import shlex
import subprocess

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import NotFound

from google.cloud import storage
from google.cloud.retail_v2 import CreateProductRequest, DeleteProductRequest, \
    FulfillmentInfo, GetProductRequest, PriceInfo, Product, ProductServiceClient

project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_number)
default_branch_name = "projects/" + project_number + "/locations/global/catalogs/default_catalog/branches/default_branch"


def generate_product() -> Product:
    price_info = PriceInfo()
    price_info.price = 30.0
    price_info.original_price = 35.5
    price_info.currency_code = "USD"
    fulfillment_info = FulfillmentInfo()
    fulfillment_info.type_ = "pickup-in-store"
    fulfillment_info.place_ids = ["store0", "store1"]
    return Product(
        title='Nest Mini',
        type_=Product.Type.PRIMARY,
        categories=['Speakers and displays'],
        brands=['Google'],
        price_info=price_info,
        fulfillment_info=[fulfillment_info],
        availability="IN_STOCK",
    )


def create_product(product_id: str) -> object:
    create_product_request = CreateProductRequest()
    create_product_request.product = generate_product()
    create_product_request.product_id = product_id
    create_product_request.parent = default_branch_name

    created_product = ProductServiceClient().create_product(
        create_product_request)
    print("---product is created:---")
    print(created_product)

    return created_product


def delete_product(product_name: str):
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name
    ProductServiceClient().delete_product(delete_product_request)

    print("---product " + product_name + " was deleted:---")


def get_product(product_name: str):
    get_product_request = GetProductRequest()
    get_product_request.name = product_name
    try:
        product = ProductServiceClient().get_product(get_product_request)
        print("---get product response:---")
        print(product)
        return product
    except NotFound as e:
        print(e.message)
        return e.message


def try_to_delete_product_if_exists(product_name: str):
    get_product_request = GetProductRequest()
    get_product_request.name = product_name
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name
    print(
        "---delete product from the catalog, if the product already exists---")
    try:
        product = ProductServiceClient().get_product(get_product_request)
        ProductServiceClient().delete_product(product.name)
    except NotFound as e:
        print(e.message)


def get_project_id():
    get_project_command = "gcloud config get-value project --format json"
    config = subprocess.check_output(shlex.split(get_project_command))
    project_id = re.search('\"(.*?)\"', str(config)).group(1)
    return project_id


def create_bucket(bucket_name: str):
    """Create a new bucket in Cloud Storage"""
    print("Creating new bucket:" + bucket_name)
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


def delete_bucket(bucket_name: str):
    """Delete a bucket from Cloud Storage"""
    storage_client = storage.Client()
    print("Deleting bucket name:" + bucket_name)
    buckets_in_your_project = str(list_buckets())
    if bucket_name in buckets_in_your_project:
        blobs = storage_client.list_blobs(bucket_name)
        for blob in blobs:
            blob.delete()
        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()
        print("Bucket {} is deleted".format(bucket.name))
    else:
        print("Bucket {} is not found".format(bucket_name))


def list_buckets():
    """Lists all buckets"""
    bucket_list = []
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        bucket_list.append(str(bucket))
    return bucket_list


def upload_blob(bucket_name, source_file_name):
    """Uploads a file to the bucket."""
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    print("Uploading data form {} to the bucket {}".format(source_file_name,
                                                           bucket_name))
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
    print("Creating dataset {}".format(dataset_name))
    if dataset_name not in list_bq_datasets():
        create_dataset_command = 'bq --location=US mk -d --default_table_expiration 3600 --description "This is my dataset." {}:{}'.format(
            get_project_id(), dataset_name)
        subprocess.check_output(shlex.split(create_dataset_command))
        print("dataset is created")
    else:
        print("dataset {} already exists".format(dataset_name))


def list_bq_datasets():
    """List BigQuery datasets in the project"""
    list_dataset_command = "bq ls --project_id {}".format(get_project_id())
    datasets = subprocess.check_output(shlex.split(list_dataset_command))
    return str(datasets)


def create_bq_table(dataset, table_name, schema):
    """Create a BigQuery table"""
    print("Creating BigQuery table {}".format(table_name))
    if table_name not in list_bq_tables(dataset):
        create_table_command = "bq mk --table {}:{}.{} {}".format(
            get_project_id(),
            dataset,
            table_name, schema)
        output = subprocess.check_output(shlex.split(create_table_command))
        print(output)
        print("table is created")
    else:
        print("table {} already exists".format(table_name))


def list_bq_tables(dataset):
    """List BigQuery tables in the dataset"""
    list_tables_command = "bq ls {}:{}".format(get_project_id(), dataset)
    tables = subprocess.check_output(shlex.split(list_tables_command))
    return str(tables)


def upload_data_to_bq_table(dataset, table_name, source, schema):
    """Upload data to the table from specified source file"""
    print("Uploading data form {} to the table {}.{}".format(source, dataset,
                                                             table_name))
    upload_data_command = "bq load --source_format=NEWLINE_DELIMITED_JSON {}:{}.{} {} {}".format(
        get_project_id(), dataset, table_name, source, schema)
    output = subprocess.check_output(shlex.split(upload_data_command))
    print(output)
