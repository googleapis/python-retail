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

from google.cloud.retail_v2.services.catalog_service.async_client import (
    CatalogServiceAsyncClient,
)
from google.cloud.retail_v2.services.catalog_service.client import CatalogServiceClient
from google.cloud.retail_v2.services.completion_service.async_client import (
    CompletionServiceAsyncClient,
)
from google.cloud.retail_v2.services.completion_service.client import (
    CompletionServiceClient,
)
from google.cloud.retail_v2.services.prediction_service.async_client import (
    PredictionServiceAsyncClient,
)
from google.cloud.retail_v2.services.prediction_service.client import (
    PredictionServiceClient,
)
from google.cloud.retail_v2.services.product_service.async_client import (
    ProductServiceAsyncClient,
)
from google.cloud.retail_v2.services.product_service.client import ProductServiceClient
from google.cloud.retail_v2.services.search_service.async_client import (
    SearchServiceAsyncClient,
)
from google.cloud.retail_v2.services.search_service.client import SearchServiceClient
from google.cloud.retail_v2.services.user_event_service.async_client import (
    UserEventServiceAsyncClient,
)
from google.cloud.retail_v2.services.user_event_service.client import (
    UserEventServiceClient,
)
from google.cloud.retail_v2.types.catalog import Catalog, ProductLevelConfig
from google.cloud.retail_v2.types.catalog_service import (
    GetDefaultBranchRequest,
    GetDefaultBranchResponse,
    ListCatalogsRequest,
    ListCatalogsResponse,
    SetDefaultBranchRequest,
    UpdateCatalogRequest,
)
from google.cloud.retail_v2.types.common import (
    Audience,
    ColorInfo,
    CustomAttribute,
    FulfillmentInfo,
    Image,
    Interval,
    LocalInventory,
    PriceInfo,
    Rating,
    UserInfo,
)
from google.cloud.retail_v2.types.completion_service import (
    CompleteQueryRequest,
    CompleteQueryResponse,
)
from google.cloud.retail_v2.types.import_config import (
    BigQuerySource,
    CompletionDataInputConfig,
    GcsSource,
    ImportCompletionDataRequest,
    ImportCompletionDataResponse,
    ImportErrorsConfig,
    ImportMetadata,
    ImportProductsRequest,
    ImportProductsResponse,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
    ProductInlineSource,
    ProductInputConfig,
    UserEventImportSummary,
    UserEventInlineSource,
    UserEventInputConfig,
)
from google.cloud.retail_v2.types.prediction_service import (
    PredictRequest,
    PredictResponse,
)
from google.cloud.retail_v2.types.product import Product
from google.cloud.retail_v2.types.product_service import (
    AddFulfillmentPlacesMetadata,
    AddFulfillmentPlacesRequest,
    AddFulfillmentPlacesResponse,
    AddLocalInventoriesMetadata,
    AddLocalInventoriesRequest,
    AddLocalInventoriesResponse,
    CreateProductRequest,
    DeleteProductRequest,
    GetProductRequest,
    ListProductsRequest,
    ListProductsResponse,
    RemoveFulfillmentPlacesMetadata,
    RemoveFulfillmentPlacesRequest,
    RemoveFulfillmentPlacesResponse,
    RemoveLocalInventoriesMetadata,
    RemoveLocalInventoriesRequest,
    RemoveLocalInventoriesResponse,
    SetInventoryMetadata,
    SetInventoryRequest,
    SetInventoryResponse,
    UpdateProductRequest,
)
from google.cloud.retail_v2.types.promotion import Promotion
from google.cloud.retail_v2.types.purge_config import (
    PurgeMetadata,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from google.cloud.retail_v2.types.search_service import SearchRequest, SearchResponse
from google.cloud.retail_v2.types.user_event import (
    CompletionDetail,
    ProductDetail,
    PurchaseTransaction,
    UserEvent,
)
from google.cloud.retail_v2.types.user_event_service import (
    CollectUserEventRequest,
    RejoinUserEventsMetadata,
    RejoinUserEventsRequest,
    RejoinUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "CatalogServiceClient",
    "CatalogServiceAsyncClient",
    "CompletionServiceClient",
    "CompletionServiceAsyncClient",
    "PredictionServiceClient",
    "PredictionServiceAsyncClient",
    "ProductServiceClient",
    "ProductServiceAsyncClient",
    "SearchServiceClient",
    "SearchServiceAsyncClient",
    "UserEventServiceClient",
    "UserEventServiceAsyncClient",
    "Catalog",
    "ProductLevelConfig",
    "GetDefaultBranchRequest",
    "GetDefaultBranchResponse",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "SetDefaultBranchRequest",
    "UpdateCatalogRequest",
    "Audience",
    "ColorInfo",
    "CustomAttribute",
    "FulfillmentInfo",
    "Image",
    "Interval",
    "LocalInventory",
    "PriceInfo",
    "Rating",
    "UserInfo",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "BigQuerySource",
    "CompletionDataInputConfig",
    "GcsSource",
    "ImportCompletionDataRequest",
    "ImportCompletionDataResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportProductsRequest",
    "ImportProductsResponse",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "ProductInlineSource",
    "ProductInputConfig",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventInputConfig",
    "PredictRequest",
    "PredictResponse",
    "Product",
    "AddFulfillmentPlacesMetadata",
    "AddFulfillmentPlacesRequest",
    "AddFulfillmentPlacesResponse",
    "AddLocalInventoriesMetadata",
    "AddLocalInventoriesRequest",
    "AddLocalInventoriesResponse",
    "CreateProductRequest",
    "DeleteProductRequest",
    "GetProductRequest",
    "ListProductsRequest",
    "ListProductsResponse",
    "RemoveFulfillmentPlacesMetadata",
    "RemoveFulfillmentPlacesRequest",
    "RemoveFulfillmentPlacesResponse",
    "RemoveLocalInventoriesMetadata",
    "RemoveLocalInventoriesRequest",
    "RemoveLocalInventoriesResponse",
    "SetInventoryMetadata",
    "SetInventoryRequest",
    "SetInventoryResponse",
    "UpdateProductRequest",
    "Promotion",
    "PurgeMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "SearchRequest",
    "SearchResponse",
    "CompletionDetail",
    "ProductDetail",
    "PurchaseTransaction",
    "UserEvent",
    "CollectUserEventRequest",
    "RejoinUserEventsMetadata",
    "RejoinUserEventsRequest",
    "RejoinUserEventsResponse",
    "WriteUserEventRequest",
)
