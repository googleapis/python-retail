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
import subprocess

from setup.setup_cleanup import create_bucket, delete_bucket, upload_blob


def test_import_products_gcs():
    bucket_name = os.environ["BUCKET_NAME"]
    create_bucket(bucket_name)
    upload_blob(bucket_name, "../resources/products.json")

    output = str(
        subprocess.check_output("python import_products_gcs.py", shell=True))

    delete_bucket(bucket_name)

    assert re.match(".*import products from google cloud source request.*",
                    output)
    assert re.match('.*input_uris: "gs://.*/products.json".*', output)
    assert re.match(".*the operation was started.*", output)
    assert re.match(
        ".*projects/.*/locations/global/catalogs/default_catalog/branches/0/operations/import-products.*",
        output,
    )

    assert re.match(".*number of successfully imported products.*?316.*",
                    output)
    assert re.match(".*number of failures during the importing.*?0.*", output)
