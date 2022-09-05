# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for BatchRemoveCatalogAttributes
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-retail


from google.cloud import retail_v2beta


def sample_batch_remove_catalog_attributes():
    # Create a client
    client = retail_v2beta.CatalogServiceClient()

    # Initialize request argument(s)
    request = retail_v2beta.BatchRemoveCatalogAttributesRequest(
        attributes_config="attributes_config_value",
        attribute_keys=['attribute_keys_value_1', 'attribute_keys_value_2'],
    )

    # Make the request
    response = client.batch_remove_catalog_attributes(request=request)

    # Handle the response
    print(response)