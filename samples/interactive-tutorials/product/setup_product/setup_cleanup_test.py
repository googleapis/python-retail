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
import google.auth

from google.cloud import bigquery

import pytest

from setup_cleanup import create_bq_dataset

project_id = google.auth.default()[1]


@pytest.fixture()
def dq_dataset_resource():
    dataset_name = "my_random_dataset_name"
    yield dataset_name
    # cleaning up after test done
    bq = bigquery.Client()
    bq.delete_dataset(dataset_name)


def test_bq_dataset_creation(table_id_prefix, dq_dataset_resource, capfd):
    # Test BQ Dataset creation.

    # creating dataset
    dataset_name = dq_dataset_resource
    create_bq_dataset(dataset_name)

    output, err = capfd.readouterr()

    assert f'Creating dataset {project_id}.{dataset_name}' in output
    assert 'dataset is created' in output
    assert err == ''


def test_repeated_bq_dataset_creation(table_id_prefix, dq_dataset_resource, capfd):
    # Test BQ Dataset creation if it already exists.

    # creating dataset
    dataset_name = dq_dataset_resource
    create_bq_dataset(dataset_name)
    create_bq_dataset(dataset_name)

    output, err = capfd.readouterr()

    assert f'Creating dataset {project_id}.{dataset_name}' in output
    assert f'dataset {project_id}.{dataset_name} already exists' in output
    assert err == ''
