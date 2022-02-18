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

import re
import subprocess


def test_create_bigquery_table():
    output = str(
        subprocess.check_output(
            'python setup/events_create_bigquery_table.py',
            shell=True))
    assert re.match(
        '.*Creating dataset .*?user_events.*', output)
    assert re.match(
        '(.*dataset .*?user_events already exists.*|.*dataset is created.*)',
        output)
    assert re.match(
        '.*Creating BigQuery table .*?user_events.events.*', output)
    assert re.match(
        '(.*table .*?user_events.events already exists.*|.*table is created.*)',
        output)
    assert re.match(
        '.*Uploading data from ../resources/user_events.json to the table .*?user_events.events.*',
        output)

    assert re.match(
        '.*Creating BigQuery table .*?events_some_invalid.*',
        output)
    assert re.match(
        '(.*table .*?events_some_invalid already exists.*|.*table is created.*)',
        output)
    assert re.match(
        '.*Uploading data from ../resources/user_events_some_invalid.json to the table .*?user_events.events_some_invalid.*',
        output)
