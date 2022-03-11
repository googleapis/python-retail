#!/bin/bash

cd product
output=$(python setup_product/products_create_gcs_bucket.py)

temp="${output#*The gcs bucket }"
bucket_name="${temp% was created}"
export BUCKET_NAME=$bucket_name

python import_products_gcs.py
echo "Your product data are successfully imported to catalog"