# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers_async
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2  # type: ignore
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.retail_v2.types import serving_config
from google.cloud.retail_v2.types import serving_config as gcr_serving_config
from google.cloud.retail_v2.types import serving_config_service

from .base import DEFAULT_CLIENT_INFO, ServingConfigServiceTransport
from .grpc import ServingConfigServiceGrpcTransport


class ServingConfigServiceGrpcAsyncIOTransport(ServingConfigServiceTransport):
    """gRPC AsyncIO backend transport for ServingConfigService.

    Service for modifying ServingConfig.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[aio.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.CreateServingConfigRequest],
        Awaitable[gcr_serving_config.ServingConfig],
    ]:
        r"""Return a callable for the create serving config method over gRPC.

        Creates a ServingConfig.

        A maximum of 100
        [ServingConfig][google.cloud.retail.v2.ServingConfig]s are
        allowed in a [Catalog][google.cloud.retail.v2.Catalog],
        otherwise a FAILED_PRECONDITION error is returned.

        Returns:
            Callable[[~.CreateServingConfigRequest],
                    Awaitable[~.ServingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_serving_config" not in self._stubs:
            self._stubs["create_serving_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/CreateServingConfig",
                request_serializer=serving_config_service.CreateServingConfigRequest.serialize,
                response_deserializer=gcr_serving_config.ServingConfig.deserialize,
            )
        return self._stubs["create_serving_config"]

    @property
    def delete_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.DeleteServingConfigRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete serving config method over gRPC.

        Deletes a ServingConfig.
        Returns a NotFound error if the ServingConfig does not
        exist.

        Returns:
            Callable[[~.DeleteServingConfigRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_serving_config" not in self._stubs:
            self._stubs["delete_serving_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/DeleteServingConfig",
                request_serializer=serving_config_service.DeleteServingConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_serving_config"]

    @property
    def update_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.UpdateServingConfigRequest],
        Awaitable[gcr_serving_config.ServingConfig],
    ]:
        r"""Return a callable for the update serving config method over gRPC.

        Updates a ServingConfig.

        Returns:
            Callable[[~.UpdateServingConfigRequest],
                    Awaitable[~.ServingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_serving_config" not in self._stubs:
            self._stubs["update_serving_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/UpdateServingConfig",
                request_serializer=serving_config_service.UpdateServingConfigRequest.serialize,
                response_deserializer=gcr_serving_config.ServingConfig.deserialize,
            )
        return self._stubs["update_serving_config"]

    @property
    def get_serving_config(
        self,
    ) -> Callable[
        [serving_config_service.GetServingConfigRequest],
        Awaitable[serving_config.ServingConfig],
    ]:
        r"""Return a callable for the get serving config method over gRPC.

        Gets a ServingConfig.
        Returns a NotFound error if the ServingConfig does not
        exist.

        Returns:
            Callable[[~.GetServingConfigRequest],
                    Awaitable[~.ServingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_serving_config" not in self._stubs:
            self._stubs["get_serving_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/GetServingConfig",
                request_serializer=serving_config_service.GetServingConfigRequest.serialize,
                response_deserializer=serving_config.ServingConfig.deserialize,
            )
        return self._stubs["get_serving_config"]

    @property
    def list_serving_configs(
        self,
    ) -> Callable[
        [serving_config_service.ListServingConfigsRequest],
        Awaitable[serving_config_service.ListServingConfigsResponse],
    ]:
        r"""Return a callable for the list serving configs method over gRPC.

        Lists all ServingConfigs linked to this catalog.

        Returns:
            Callable[[~.ListServingConfigsRequest],
                    Awaitable[~.ListServingConfigsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_serving_configs" not in self._stubs:
            self._stubs["list_serving_configs"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/ListServingConfigs",
                request_serializer=serving_config_service.ListServingConfigsRequest.serialize,
                response_deserializer=serving_config_service.ListServingConfigsResponse.deserialize,
            )
        return self._stubs["list_serving_configs"]

    @property
    def add_control(
        self,
    ) -> Callable[
        [serving_config_service.AddControlRequest],
        Awaitable[gcr_serving_config.ServingConfig],
    ]:
        r"""Return a callable for the add control method over gRPC.

        Enables a Control on the specified ServingConfig. The control is
        added in the last position of the list of controls it belongs to
        (e.g. if it's a facet spec control it will be applied in the
        last position of servingConfig.facetSpecIds) Returns a
        ALREADY_EXISTS error if the control has already been applied.
        Returns a FAILED_PRECONDITION error if the addition could exceed
        maximum number of control allowed for that type of control.

        Returns:
            Callable[[~.AddControlRequest],
                    Awaitable[~.ServingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_control" not in self._stubs:
            self._stubs["add_control"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/AddControl",
                request_serializer=serving_config_service.AddControlRequest.serialize,
                response_deserializer=gcr_serving_config.ServingConfig.deserialize,
            )
        return self._stubs["add_control"]

    @property
    def remove_control(
        self,
    ) -> Callable[
        [serving_config_service.RemoveControlRequest],
        Awaitable[gcr_serving_config.ServingConfig],
    ]:
        r"""Return a callable for the remove control method over gRPC.

        Disables a Control on the specified ServingConfig. The control
        is removed from the ServingConfig. Returns a NOT_FOUND error if
        the Control is not enabled for the ServingConfig.

        Returns:
            Callable[[~.RemoveControlRequest],
                    Awaitable[~.ServingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_control" not in self._stubs:
            self._stubs["remove_control"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2.ServingConfigService/RemoveControl",
                request_serializer=serving_config_service.RemoveControlRequest.serialize,
                response_deserializer=gcr_serving_config.ServingConfig.deserialize,
            )
        return self._stubs["remove_control"]

    def close(self):
        return self.grpc_channel.close()

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]


__all__ = ("ServingConfigServiceGrpcAsyncIOTransport",)
