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

# [START retail_import_products_from_gcs]
# Import products into a catalog from gcs using Retail API
#
import os
import time

from google.cloud.retail import (
    GcsSource,
    ImportErrorsConfig,
    ImportProductsRequest,
    ProductInputConfig,
    ProductServiceClient,
)


# Read the project number from the environment variable
project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
bucket_name = os.environ["BUCKET_NAME"]

# You can change the branch here. The "default_branch" is set to point to the branch "0"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/default_branch".format(
    project_number
)

gcs_bucket = "gs://{}".format(bucket_name)
gcs_errors_bucket = "{}/error".format(gcs_bucket)
gcs_products_object = "products.json"


# TO CHECK ERROR HANDLING USE THE JSON WITH INVALID PRODUCT
# gcs_products_object = "products_some_invalid.json"


# get import products from gcs request
def get_import_products_gcs_request(gcs_object_name: str):
    # TO CHECK ERROR HANDLING PASTE THE INVALID CATALOG NAME HERE:
    # default_catalog = "invalid_catalog_name"
    gcs_source = GcsSource()
    gcs_source.input_uris = ["{0}/{1}".format(gcs_bucket, gcs_object_name)]

    input_config = ProductInputConfig()
    input_config.gcs_source = gcs_source
    print("GRS source:")
    print(gcs_source.input_uris)

    errors_config = ImportErrorsConfig()
    errors_config.gcs_prefix = gcs_errors_bucket

    import_request = ImportProductsRequest()
    import_request.parent = default_catalog
    import_request.reconciliation_mode = (
        ImportProductsRequest.ReconciliationMode.INCREMENTAL
    )
    import_request.input_config = input_config
    import_request.errors_config = errors_config

    print("---import products from google cloud source request---")
    print(import_request)

    return import_request


# call the Retail API to import products
def import_products_from_gcs():
    import_gcs_request = get_import_products_gcs_request(gcs_products_object)
    gcs_operation = ProductServiceClient().import_products(import_gcs_request)

    print("---the operation was started:----")
    print(gcs_operation.operation.name)

    while not gcs_operation.done():
        print("---please wait till operation is done---")
        time.sleep(30)
    print("---import products operation is done---")

    if gcs_operation.metadata is not None:
        print("---number of successfully imported products---")
        print(gcs_operation.metadata.success_count)
        print("---number of failures during the importing---")
        print(gcs_operation.metadata.failure_count)
    else:
        print("---operation.metadata is empty---")

    if gcs_operation.result is not None:
        print("---operation result:---")
        print(gcs_operation.result())
    else:
        print("---operation.result is empty---")

    # The imported products needs to be indexed in the catalog before they become available for search.
    print(
        "Wait 2-5 minutes till products become indexed in the catalog, after that they will be available for search"
    )


import_products_from_gcs()

# [END retail_import_products_from_gcs]
