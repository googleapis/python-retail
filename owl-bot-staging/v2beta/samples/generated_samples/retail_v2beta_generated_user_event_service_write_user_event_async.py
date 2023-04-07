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
# Snippet for WriteUserEvent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-retail


# [START retail_v2beta_generated_UserEventService_WriteUserEvent_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import retail_v2beta


async def sample_write_user_event():
    # Create a client
    client = retail_v2beta.UserEventServiceAsyncClient()

    # Initialize request argument(s)
    user_event = retail_v2beta.UserEvent()
    user_event.event_type = "event_type_value"
    user_event.visitor_id = "visitor_id_value"

    request = retail_v2beta.WriteUserEventRequest(
        parent="parent_value",
        user_event=user_event,
    )

    # Make the request
    response = await client.write_user_event(request=request)

    # Handle the response
    print(response)

# [END retail_v2beta_generated_UserEventService_WriteUserEvent_async]
