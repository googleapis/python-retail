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


# [START retail_import_user_events_from_inline_source]
# Import user events into a catalog from inline source using Retail API
#
import datetime
import os
import random
import string
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail import UserEvent, UserEventInlineSource, \
    UserEventInputConfig, UserEventServiceClient, \
    ImportUserEventsRequest
from google.protobuf.timestamp_pb2 import Timestamp

project_number = os.getenv('PROJECT_NUMBER')

endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_number)


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get user events for import
def get_user_events():
    user_events = []
    for x in range(3):
        timestamp = Timestamp()
        timestamp.seconds = int(datetime.datetime.now().timestamp())

        user_event = UserEvent()
        user_event.event_type = "home-page-view"
        user_event.visitor_id = ''.join(
            random.sample(string.ascii_lowercase, 4)) + 'event_' + x
        user_event.event_time = timestamp
        user_events.append(user_event)

    print(user_events)
    return user_events


# get import user events from inline source request
def get_import_events_inline_source_request(user_events_to_import):
    inline_source = UserEventInlineSource()
    inline_source.user_events = user_events_to_import

    input_config = UserEventInputConfig()
    input_config.user_event_inline_source = inline_source

    import_request = ImportUserEventsRequest()
    import_request.parent = default_catalog
    import_request.input_config = input_config

    print("---import user events from inline source request---")
    print(import_request)

    return import_request


# call the Retail API to import user events
def import_user_events_from_inline_source():
    import_inline_request = get_import_events_inline_source_request(
        get_user_events())
    import_operation = get_user_events_service_client().import_user_events(
        import_inline_request)

    print("---the operation was started:----")
    print(import_operation.operation.name)

    while not import_operation.done():
        print("---please wait till operation is done---")
        time.sleep(5)

    print("---import user events operation is done---")
    print("---number of successfully imported events---")
    print(import_operation.metadata.success_count)
    print("---number of failures during the importing---")
    print(import_operation.metadata.failure_count)
    print("---operation result:---")
    print(import_operation.result())


import_user_events_from_inline_source()

# [END retail_import_user_events_from_inline_source]
