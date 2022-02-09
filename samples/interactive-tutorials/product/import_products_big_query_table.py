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

# [START retail_import_products_from_big_query]
# Import products into a catalog from big query table using Retail API
#
import os
import time

from google.cloud.retail import (
    BigQuerySource,
    ImportProductsRequest,
    ProductInputConfig,
    ProductServiceClient,
)

project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]

default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/default_branch".format(
    project_number
)
dataset_id = "products"
table_id = "products"


# TO CHECK ERROR HANDLING USE THE TABLE WITH INVALID PRODUCTS:
# table_id = "products_some_invalid"


# get import products from big query request
def get_import_products_big_query_request(reconciliation_mode):
    # TO CHECK ERROR HANDLING PASTE THE INVALID CATALOG NAME HERE:
    # default_catalog = "invalid_catalog_name"
    big_query_source = BigQuerySource()
    big_query_source.project_id = project_id
    big_query_source.dataset_id = dataset_id
    big_query_source.table_id = table_id
    big_query_source.data_schema = "product"

    input_config = ProductInputConfig()
    input_config.big_query_source = big_query_source

    import_request = ImportProductsRequest()
    import_request.parent = default_catalog
    import_request.reconciliation_mode = reconciliation_mode
    import_request.input_config = input_config

    print("---import products from big query table request---")
    print(import_request)

    return import_request


# call the Retail API to import products
def import_products_from_big_query():
    # TRY THE FULL RECONCILIATION MODE HERE:
    reconciliation_mode = ImportProductsRequest.ReconciliationMode.INCREMENTAL

    import_big_query_request = get_import_products_big_query_request(
        reconciliation_mode
    )
    big_query_operation = ProductServiceClient().import_products(
        import_big_query_request
    )

    print("---the operation was started:----")
    print(big_query_operation.operation.name)

    while not big_query_operation.done():
        print("---please wait till operation is done---")
        time.sleep(30)
    print("---import products operation is done---")

    if big_query_operation.metadata is not None:
        print("---number of successfully imported products---")
        print(big_query_operation.metadata.success_count)
        print("---number of failures during the importing---")
        print(big_query_operation.metadata.failure_count)
    else:
        print("---operation.metadata is empty---")

    if big_query_operation.result is not None:
        print("---operation result:---")
        print(big_query_operation.result())
    else:
        print("---operation.result is empty---")


import_products_from_big_query()

# [END retail_import_products_from_big_query]
