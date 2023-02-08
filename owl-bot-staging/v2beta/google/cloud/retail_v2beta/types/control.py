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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.retail_v2beta.types import common
from google.cloud.retail_v2beta.types import search_service


__protobuf__ = proto.module(
    package='google.cloud.retail.v2beta',
    manifest={
        'Control',
    },
)


class Control(proto.Message):
    r"""Configures dynamic metadata that can be linked to a
    [ServingConfig][google.cloud.retail.v2beta.ServingConfig] and affect
    search or recommendation results at serving time.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        facet_spec (google.cloud.retail_v2beta.types.SearchRequest.FacetSpec):
            A facet specification to perform faceted search.

            Note that this field is deprecated and will throw
            NOT_IMPLEMENTED if used for creating a control.

            This field is a member of `oneof`_ ``control``.
        rule (google.cloud.retail_v2beta.types.Rule):
            A rule control - a condition-action pair.
            Enacts a set action when the condition is
            triggered. For example: Boost "gShoe" when query
            full matches "Running Shoes".

            This field is a member of `oneof`_ ``control``.
        name (str):
            Immutable. Fully qualified name
            ``projects/*/locations/global/catalogs/*/controls/*``
        display_name (str):
            Required. The human readable control display name. Used in
            Retail UI.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is thrown.
        associated_serving_config_ids (MutableSequence[str]):
            Output only. List of [serving
            config][google.cloud.retail.v2beta.ServingConfig] ids that
            are associated with this control in the same
            [Catalog][google.cloud.retail.v2beta.Catalog].

            Note the association is managed via the
            [ServingConfig][google.cloud.retail.v2beta.ServingConfig],
            this is an output only denormalized view.
        solution_types (MutableSequence[google.cloud.retail_v2beta.types.SolutionType]):
            Required. Immutable. The solution types that the control is
            used for. Currently we support setting only one type of
            solution at creation time.

            Only ``SOLUTION_TYPE_SEARCH`` value is supported at the
            moment. If no solution type is provided at creation time,
            will default to
            [SOLUTION_TYPE_SEARCH][google.cloud.retail.v2beta.SolutionType.SOLUTION_TYPE_SEARCH].
        search_solution_use_case (MutableSequence[google.cloud.retail_v2beta.types.SearchSolutionUseCase]):
            Specifies the use case for the control. Affects what
            condition fields can be set. Only settable by search
            controls. Will default to
            [SEARCH_SOLUTION_USE_CASE_SEARCH][google.cloud.retail.v2beta.SearchSolutionUseCase.SEARCH_SOLUTION_USE_CASE_SEARCH]
            if not specified. Currently only allow one
            search_solution_use_case per control.
    """

    facet_spec: search_service.SearchRequest.FacetSpec = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='control',
        message=search_service.SearchRequest.FacetSpec,
    )
    rule: common.Rule = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='control',
        message=common.Rule,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    associated_serving_config_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    solution_types: MutableSequence[common.SolutionType] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=common.SolutionType,
    )
    search_solution_use_case: MutableSequence[common.SearchSolutionUseCase] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=common.SearchSolutionUseCase,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
