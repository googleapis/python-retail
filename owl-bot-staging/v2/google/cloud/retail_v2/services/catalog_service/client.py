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
from collections import OrderedDict
import os
import re
from typing import Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union, cast

from google.cloud.retail_v2 import gapic_version as package_version

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials             # type: ignore
from google.auth.transport import mtls                            # type: ignore
from google.auth.transport.grpc import SslCredentials             # type: ignore
from google.auth.exceptions import MutualTLSChannelError          # type: ignore
from google.oauth2 import service_account                         # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.location import locations_pb2 # type: ignore
from google.cloud.retail_v2.services.catalog_service import pagers
from google.cloud.retail_v2.types import catalog
from google.cloud.retail_v2.types import catalog as gcr_catalog
from google.cloud.retail_v2.types import catalog_service
from google.cloud.retail_v2.types import common
from google.cloud.retail_v2.types import import_config
from google.longrunning import operations_pb2
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import CatalogServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import CatalogServiceGrpcTransport
from .transports.grpc_asyncio import CatalogServiceGrpcAsyncIOTransport
from .transports.rest import CatalogServiceRestTransport


class CatalogServiceClientMeta(type):
    """Metaclass for the CatalogService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry = OrderedDict()  # type: Dict[str, Type[CatalogServiceTransport]]
    _transport_registry["grpc"] = CatalogServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = CatalogServiceGrpcAsyncIOTransport
    _transport_registry["rest"] = CatalogServiceRestTransport

    def get_transport_class(cls,
            label: Optional[str] = None,
        ) -> Type[CatalogServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class CatalogServiceClient(metaclass=CatalogServiceClientMeta):
    """Service for managing catalog configuration."""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "retail.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CatalogServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CatalogServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> CatalogServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CatalogServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def attributes_config_path(project: str,location: str,catalog: str,) -> str:
        """Returns a fully-qualified attributes_config string."""
        return "projects/{project}/locations/{location}/catalogs/{catalog}/attributesConfig".format(project=project, location=location, catalog=catalog, )

    @staticmethod
    def parse_attributes_config_path(path: str) -> Dict[str,str]:
        """Parses a attributes_config path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/catalogs/(?P<catalog>.+?)/attributesConfig$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def branch_path(project: str,location: str,catalog: str,branch: str,) -> str:
        """Returns a fully-qualified branch string."""
        return "projects/{project}/locations/{location}/catalogs/{catalog}/branches/{branch}".format(project=project, location=location, catalog=catalog, branch=branch, )

    @staticmethod
    def parse_branch_path(path: str) -> Dict[str,str]:
        """Parses a branch path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/catalogs/(?P<catalog>.+?)/branches/(?P<branch>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def catalog_path(project: str,location: str,catalog: str,) -> str:
        """Returns a fully-qualified catalog string."""
        return "projects/{project}/locations/{location}/catalogs/{catalog}".format(project=project, location=location, catalog=catalog, )

    @staticmethod
    def parse_catalog_path(path: str) -> Dict[str,str]:
        """Parses a catalog path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/catalogs/(?P<catalog>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def completion_config_path(project: str,location: str,catalog: str,) -> str:
        """Returns a fully-qualified completion_config string."""
        return "projects/{project}/locations/{location}/catalogs/{catalog}/completionConfig".format(project=project, location=location, catalog=catalog, )

    @staticmethod
    def parse_completion_config_path(path: str) -> Dict[str,str]:
        """Parses a completion_config path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/catalogs/(?P<catalog>.+?)/completionConfig$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str, ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(billing_account=billing_account, )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str,str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str, ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder, )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str,str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str, ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization, )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str,str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str, ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project, )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str,str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str, ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(project=project, location=location, )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str,str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[client_options_lib.ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError("Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`")
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError("Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`")

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (use_mtls_endpoint == "auto" and client_cert_source):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Optional[Union[str, CatalogServiceTransport]] = None,
            client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the catalog service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, CatalogServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        client_options = cast(client_options_lib.ClientOptions, client_options)

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(client_options)

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError("client_options.api_key and credentials are mutually exclusive")

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, CatalogServiceTransport):
            # transport is a CatalogServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError("When providing a transport instance, "
                                 "provide its credentials directly.")
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(google.auth._default, "get_api_key_credentials"):
                credentials = google.auth._default.get_api_key_credentials(api_key_value)

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=client_options.api_audience,
            )

    def list_catalogs(self,
            request: Optional[Union[catalog_service.ListCatalogsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCatalogsPager:
        r"""Lists all the [Catalog][google.cloud.retail.v2.Catalog]s
        associated with the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_list_catalogs():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.ListCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_catalogs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.ListCatalogsRequest, dict]):
                The request object. Request for
                [CatalogService.ListCatalogs][google.cloud.retail.v2.CatalogService.ListCatalogs]
                method.
            parent (str):
                Required. The account resource name with an associated
                location.

                If the caller does not have permission to list
                [Catalog][google.cloud.retail.v2.Catalog]s under this
                location, regardless of whether or not this location
                exists, a PERMISSION_DENIED error is returned.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.services.catalog_service.pagers.ListCatalogsPager:
                Response for
                   [CatalogService.ListCatalogs][google.cloud.retail.v2.CatalogService.ListCatalogs]
                   method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.ListCatalogsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.ListCatalogsRequest):
            request = catalog_service.ListCatalogsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_catalogs]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCatalogsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_catalog(self,
            request: Optional[Union[catalog_service.UpdateCatalogRequest, dict]] = None,
            *,
            catalog: Optional[gcr_catalog.Catalog] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> gcr_catalog.Catalog:
        r"""Updates the [Catalog][google.cloud.retail.v2.Catalog]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_update_catalog():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                catalog = retail_v2.Catalog()
                catalog.name = "name_value"
                catalog.display_name = "display_name_value"

                request = retail_v2.UpdateCatalogRequest(
                    catalog=catalog,
                )

                # Make the request
                response = client.update_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.UpdateCatalogRequest, dict]):
                The request object. Request for
                [CatalogService.UpdateCatalog][google.cloud.retail.v2.CatalogService.UpdateCatalog]
                method.
            catalog (google.cloud.retail_v2.types.Catalog):
                Required. The [Catalog][google.cloud.retail.v2.Catalog]
                to update.

                If the caller does not have permission to update the
                [Catalog][google.cloud.retail.v2.Catalog], regardless of
                whether or not it exists, a PERMISSION_DENIED error is
                returned.

                If the [Catalog][google.cloud.retail.v2.Catalog] to
                update does not exist, a NOT_FOUND error is returned.

                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Indicates which fields in the provided
                [Catalog][google.cloud.retail.v2.Catalog] to update.

                If an unsupported or unknown field is provided, an
                INVALID_ARGUMENT error is returned.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.Catalog:
                The catalog configuration.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([catalog, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.UpdateCatalogRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.UpdateCatalogRequest):
            request = catalog_service.UpdateCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if catalog is not None:
                request.catalog = catalog
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_catalog]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("catalog.name", request.catalog.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_default_branch(self,
            request: Optional[Union[catalog_service.SetDefaultBranchRequest, dict]] = None,
            *,
            catalog: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Set a specified branch id as default branch. API methods such as
        [SearchService.Search][google.cloud.retail.v2.SearchService.Search],
        [ProductService.GetProduct][google.cloud.retail.v2.ProductService.GetProduct],
        [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
        will treat requests using "default_branch" to the actual branch
        id set as default.

        For example, if ``projects/*/locations/*/catalogs/*/branches/1``
        is set as default, setting
        [SearchRequest.branch][google.cloud.retail.v2.SearchRequest.branch]
        to ``projects/*/locations/*/catalogs/*/branches/default_branch``
        is equivalent to setting
        [SearchRequest.branch][google.cloud.retail.v2.SearchRequest.branch]
        to ``projects/*/locations/*/catalogs/*/branches/1``.

        Using multiple branches can be useful when developers would like
        to have a staging branch to test and verify for future usage.
        When it becomes ready, developers switch on the staging branch
        using this API while keeping using
        ``projects/*/locations/*/catalogs/*/branches/default_branch`` as
        [SearchRequest.branch][google.cloud.retail.v2.SearchRequest.branch]
        to route the traffic to this staging branch.

        CAUTION: If you have live predict/search traffic, switching the
        default branch could potentially cause outages if the ID space
        of the new branch is very different from the old one.

        More specifically:

        -  PredictionService will only return product IDs from branch
           {newBranch}.
        -  SearchService will only return product IDs from branch
           {newBranch} (if branch is not explicitly set).
        -  UserEventService will only join events with products from
           branch {newBranch}.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_set_default_branch():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.SetDefaultBranchRequest(
                )

                # Make the request
                client.set_default_branch(request=request)

        Args:
            request (Union[google.cloud.retail_v2.types.SetDefaultBranchRequest, dict]):
                The request object. Request message to set a specified
                branch as new default_branch.
            catalog (str):
                Full resource name of the catalog, such as
                ``projects/*/locations/global/catalogs/default_catalog``.

                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([catalog])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.SetDefaultBranchRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.SetDefaultBranchRequest):
            request = catalog_service.SetDefaultBranchRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if catalog is not None:
                request.catalog = catalog

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_default_branch]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("catalog", request.catalog),
            )),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_default_branch(self,
            request: Optional[Union[catalog_service.GetDefaultBranchRequest, dict]] = None,
            *,
            catalog: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog_service.GetDefaultBranchResponse:
        r"""Get which branch is currently default branch set by
        [CatalogService.SetDefaultBranch][google.cloud.retail.v2.CatalogService.SetDefaultBranch]
        method under a specified parent catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_get_default_branch():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.GetDefaultBranchRequest(
                )

                # Make the request
                response = client.get_default_branch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.GetDefaultBranchRequest, dict]):
                The request object. Request message to show which branch
                is currently the default branch.
            catalog (str):
                The parent catalog resource name, such as
                ``projects/*/locations/global/catalogs/default_catalog``.

                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.GetDefaultBranchResponse:
                Response message of
                   [CatalogService.GetDefaultBranch][google.cloud.retail.v2.CatalogService.GetDefaultBranch].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([catalog])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.GetDefaultBranchRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.GetDefaultBranchRequest):
            request = catalog_service.GetDefaultBranchRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if catalog is not None:
                request.catalog = catalog

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_default_branch]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("catalog", request.catalog),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_completion_config(self,
            request: Optional[Union[catalog_service.GetCompletionConfigRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.CompletionConfig:
        r"""Gets a
        [CompletionConfig][google.cloud.retail.v2.CompletionConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_get_completion_config():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.GetCompletionConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_completion_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.GetCompletionConfigRequest, dict]):
                The request object. Request for
                [CatalogService.GetCompletionConfig][google.cloud.retail.v2.CatalogService.GetCompletionConfig]
                method.
            name (str):
                Required. Full CompletionConfig resource name. Format:
                ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/completionConfig``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.CompletionConfig:
                Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.GetCompletionConfigRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.GetCompletionConfigRequest):
            request = catalog_service.GetCompletionConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_completion_config]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_completion_config(self,
            request: Optional[Union[catalog_service.UpdateCompletionConfigRequest, dict]] = None,
            *,
            completion_config: Optional[catalog.CompletionConfig] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.CompletionConfig:
        r"""Updates the
        [CompletionConfig][google.cloud.retail.v2.CompletionConfig]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_update_completion_config():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                completion_config = retail_v2.CompletionConfig()
                completion_config.name = "name_value"

                request = retail_v2.UpdateCompletionConfigRequest(
                    completion_config=completion_config,
                )

                # Make the request
                response = client.update_completion_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.UpdateCompletionConfigRequest, dict]):
                The request object. Request for
                [CatalogService.UpdateCompletionConfig][google.cloud.retail.v2.CatalogService.UpdateCompletionConfig]
                method.
            completion_config (google.cloud.retail_v2.types.CompletionConfig):
                Required. The
                [CompletionConfig][google.cloud.retail.v2.CompletionConfig]
                to update.

                If the caller does not have permission to update the
                [CompletionConfig][google.cloud.retail.v2.CompletionConfig],
                then a PERMISSION_DENIED error is returned.

                If the
                [CompletionConfig][google.cloud.retail.v2.CompletionConfig]
                to update does not exist, a NOT_FOUND error is returned.

                This corresponds to the ``completion_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Indicates which fields in the provided
                [CompletionConfig][google.cloud.retail.v2.CompletionConfig]
                to update. The following are the only supported fields:

                -  [CompletionConfig.matching_order][google.cloud.retail.v2.CompletionConfig.matching_order]
                -  [CompletionConfig.max_suggestions][google.cloud.retail.v2.CompletionConfig.max_suggestions]
                -  [CompletionConfig.min_prefix_length][google.cloud.retail.v2.CompletionConfig.min_prefix_length]
                -  [CompletionConfig.auto_learning][google.cloud.retail.v2.CompletionConfig.auto_learning]

                If not set, all supported fields are updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.CompletionConfig:
                Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([completion_config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.UpdateCompletionConfigRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.UpdateCompletionConfigRequest):
            request = catalog_service.UpdateCompletionConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if completion_config is not None:
                request.completion_config = completion_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_completion_config]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("completion_config.name", request.completion_config.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_attributes_config(self,
            request: Optional[Union[catalog_service.GetAttributesConfigRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.AttributesConfig:
        r"""Gets an
        [AttributesConfig][google.cloud.retail.v2.AttributesConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_get_attributes_config():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.GetAttributesConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_attributes_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.GetAttributesConfigRequest, dict]):
                The request object. Request for
                [CatalogService.GetAttributesConfig][google.cloud.retail.v2.CatalogService.GetAttributesConfig]
                method.
            name (str):
                Required. Full AttributesConfig resource name. Format:
                ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.GetAttributesConfigRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.GetAttributesConfigRequest):
            request = catalog_service.GetAttributesConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_attributes_config]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_attributes_config(self,
            request: Optional[Union[catalog_service.UpdateAttributesConfigRequest, dict]] = None,
            *,
            attributes_config: Optional[catalog.AttributesConfig] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.AttributesConfig:
        r"""Updates the
        [AttributesConfig][google.cloud.retail.v2.AttributesConfig].

        The catalog attributes in the request will be updated in the
        catalog, or inserted if they do not exist. Existing catalog
        attributes not included in the request will remain unchanged.
        Attributes that are assigned to products, but do not exist at
        the catalog level, are always included in the response. The
        product attribute is assigned default values for missing catalog
        attribute fields, e.g., searchable and dynamic facetable
        options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_update_attributes_config():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                attributes_config = retail_v2.AttributesConfig()
                attributes_config.name = "name_value"

                request = retail_v2.UpdateAttributesConfigRequest(
                    attributes_config=attributes_config,
                )

                # Make the request
                response = client.update_attributes_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.UpdateAttributesConfigRequest, dict]):
                The request object. Request for
                [CatalogService.UpdateAttributesConfig][google.cloud.retail.v2.CatalogService.UpdateAttributesConfig]
                method.
            attributes_config (google.cloud.retail_v2.types.AttributesConfig):
                Required. The
                [AttributesConfig][google.cloud.retail.v2.AttributesConfig]
                to update.

                This corresponds to the ``attributes_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Indicates which fields in the provided
                [AttributesConfig][google.cloud.retail.v2.AttributesConfig]
                to update. The following is the only supported field:

                -  [AttributesConfig.catalog_attributes][google.cloud.retail.v2.AttributesConfig.catalog_attributes]

                If not set, all supported fields are updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([attributes_config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.UpdateAttributesConfigRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.UpdateAttributesConfigRequest):
            request = catalog_service.UpdateAttributesConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if attributes_config is not None:
                request.attributes_config = attributes_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_attributes_config]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("attributes_config.name", request.attributes_config.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def add_catalog_attribute(self,
            request: Optional[Union[catalog_service.AddCatalogAttributeRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.AttributesConfig:
        r"""Adds the specified
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] to
        the [AttributesConfig][google.cloud.retail.v2.AttributesConfig].

        If the
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] to
        add already exists, an ALREADY_EXISTS error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_add_catalog_attribute():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                catalog_attribute = retail_v2.CatalogAttribute()
                catalog_attribute.key = "key_value"

                request = retail_v2.AddCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    catalog_attribute=catalog_attribute,
                )

                # Make the request
                response = client.add_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.AddCatalogAttributeRequest, dict]):
                The request object. Request for
                [CatalogService.AddCatalogAttribute][google.cloud.retail.v2.CatalogService.AddCatalogAttribute]
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.AddCatalogAttributeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.AddCatalogAttributeRequest):
            request = catalog_service.AddCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_catalog_attribute]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("attributes_config", request.attributes_config),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def remove_catalog_attribute(self,
            request: Optional[Union[catalog_service.RemoveCatalogAttributeRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.AttributesConfig:
        r"""Removes the specified
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] from
        the [AttributesConfig][google.cloud.retail.v2.AttributesConfig].

        If the
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] to
        remove does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_remove_catalog_attribute():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                request = retail_v2.RemoveCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    key="key_value",
                )

                # Make the request
                response = client.remove_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.RemoveCatalogAttributeRequest, dict]):
                The request object. Request for
                [CatalogService.RemoveCatalogAttribute][google.cloud.retail.v2.CatalogService.RemoveCatalogAttribute]
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.RemoveCatalogAttributeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.RemoveCatalogAttributeRequest):
            request = catalog_service.RemoveCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_catalog_attribute]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("attributes_config", request.attributes_config),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def replace_catalog_attribute(self,
            request: Optional[Union[catalog_service.ReplaceCatalogAttributeRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> catalog.AttributesConfig:
        r"""Replaces the specified
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] in
        the [AttributesConfig][google.cloud.retail.v2.AttributesConfig]
        by updating the catalog attribute with the same
        [CatalogAttribute.key][google.cloud.retail.v2.CatalogAttribute.key].

        If the
        [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] to
        replace does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2

            def sample_replace_catalog_attribute():
                # Create a client
                client = retail_v2.CatalogServiceClient()

                # Initialize request argument(s)
                catalog_attribute = retail_v2.CatalogAttribute()
                catalog_attribute.key = "key_value"

                request = retail_v2.ReplaceCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    catalog_attribute=catalog_attribute,
                )

                # Make the request
                response = client.replace_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.retail_v2.types.ReplaceCatalogAttributeRequest, dict]):
                The request object. Request for
                [CatalogService.ReplaceCatalogAttribute][google.cloud.retail.v2.CatalogService.ReplaceCatalogAttribute]
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.retail_v2.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a catalog_service.ReplaceCatalogAttributeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, catalog_service.ReplaceCatalogAttributeRequest):
            request = catalog_service.ReplaceCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.replace_catalog_attribute]

         # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("attributes_config", request.attributes_config),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "CatalogServiceClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

    def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response










DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "CatalogServiceClient",
)
