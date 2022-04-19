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

# [START retail_prediction_get_prediction_with_filtering]
# Call Retail API to get predictions from Recommendation AI using filtering.
#
import os

import google.auth
from google.cloud.retail_v2 import (
    PredictionServiceClient,
    UserEvent,
    ProductDetail,
    Product,
    PredictRequest,
)


project_id = google.auth.default()[1]
placement_id = os.environ["GOOGLE_CLOUD_PLACEMENT"]


# get prediction service client
def get_search_service_client():
    return PredictionServiceClient()


# get prediction service request:
def get_predict_request(_filter: str, params: dict):
    default_predict_placement = (
        f"projects/{project_id}/locations/global/catalogs/"
        f"default_catalog/placements/{placement_id}"
    )

    # create product object
    product = Product()
    product.id = "55106"  # An id of real product

    # create product detail object
    product_details = ProductDetail()
    product_details.product = product

    # create user event object
    user_event = UserEvent()
    user_event.event_type = "detail-page-view"
    user_event.visitor_id = "281790"  # A unique identifier to track visitors
    user_event.product_details = [product_details]

    predict_request = PredictRequest()
    predict_request.placement = default_predict_placement  # Placement is used to identify the Serving Config name
    predict_request.user_event = user_event
    predict_request.filter = _filter
    # add `returnProduct` param to return the associated product object
    predict_request.params = {"returnProduct": True}
    predict_request.params.update(params)

    print("---predict request---")
    print(predict_request)

    return predict_request


# call the prediction:
def predict():
    # TRY DIFFERENT FILTER HERE:
    _filter = "filterOutOfStockItems"

    # TRY TO UPDATE `strictFiltering` HERE:
    params = {"strictFiltering": True}

    predict_request = get_predict_request(_filter, params)
    predict_response = get_search_service_client().predict(predict_request)

    print("---predict response---")
    print(predict_response)

    return predict_response


predict()
# [END retail_prediction_get_prediction_with_filtering]
