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

# [START retail_search_for_products_with_query_parameter]
# Call Retail API to search for a products in a catalog using only search query.
#

import google.auth
from google.cloud.retail import SearchRequest, SearchServiceClient

project_id = google.auth.default()[1]


# get search service request:
def get_search_request(query: str):
    default_search_placement = (
        "projects/"
        + project_id
        + "/locations/global/catalogs/default_catalog/placements/default_search"
    )

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.page_size = 10

    print("---search request:---")
    print(search_request)

    return search_request


# call the Retail Search:
def search():
    # TRY DIFFERENT QUERY PHRASES HERE:
    query_phrase = "Hoodie"

    search_request = get_search_request(query_phrase)
    search_response = SearchServiceClient().search(search_request)

    print("---search response---")
    print(search_response)
    return search_response


search()
# [END retail_search_for_products_with_query_parameter]
