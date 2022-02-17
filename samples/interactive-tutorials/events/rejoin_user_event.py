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


# [START retail_rejoin_user_event]
# Import user events into a catalog from inline source using Retail API
#
import os

from google.api_core.client_options import ClientOptions
from google.cloud.retail import UserEventServiceClient, RejoinUserEventsRequest

from setup.setup_cleanup import write_user_event, purge_user_event

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")

endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_id
)
visitor_id = "test_visitor_id"


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get rejoin user event request
def get_rejoin_user_event_request():
    # TO CHECK THE ERROR HANDLING TRY TO PASS INVALID CATALOG:
    # default_catalog = "projects/{0}/locations/global/catalogs/invalid_catalog".format(project_number)
    rejoin_user_event_request = RejoinUserEventsRequest()
    rejoin_user_event_request.parent = default_catalog
    rejoin_user_event_request.user_event_rejoin_scope = (
        RejoinUserEventsRequest.UserEventRejoinScope.UNJOINED_EVENTS
    )
    print("---rejoin user events request---")
    print(rejoin_user_event_request)
    return rejoin_user_event_request


# call the Retail API to rejoin user event
def call_rejoin_user_events():
    rejoin_operation = get_user_events_service_client().rejoin_user_events(
        get_rejoin_user_event_request()
    )

    print("---the rejoin operation was started:----")
    print(rejoin_operation.operation.name)


write_user_event(visitor_id)
call_rejoin_user_events()
purge_user_event(visitor_id)

# [END retail_rejoin_user_event]
