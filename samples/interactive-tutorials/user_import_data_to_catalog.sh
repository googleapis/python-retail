#!/bin/bash

# Copyright 2022 Google Inc. All Rights Reserved.
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

# Change the working directory
current_path=$(pwd)
temp_path="${current_path%cloudshell_open*}"
full_path=$temp_path"cloudshell_open/python-retail/samples/interactive-tutorials/product"
cd $full_path
# Create a GCS bucket and upload the product data to the bucket
output=$(python setup_product/products_create_gcs_bucket.py)

# Get the bucket name and store it in the env variable BUCKET_NAME
temp="${output#*The gcs bucket }"
bucket_name="${temp% was created*}"
export BUCKET_NAME=$bucket_name

# Import products to the Retail catalog
python import_products_gcs.py
echo "Products are successfully imported to catalog"
echo "Your Retail catalog is ready to use!"
