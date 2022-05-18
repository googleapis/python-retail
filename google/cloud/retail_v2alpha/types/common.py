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
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "AttributeConfigLevel",
        "SolutionType",
        "SearchSolutionUseCase",
        "Condition",
        "Rule",
        "Audience",
        "ColorInfo",
        "CustomAttribute",
        "FulfillmentInfo",
        "Image",
        "Interval",
        "PriceInfo",
        "Rating",
        "UserInfo",
        "LocalInventory",
    },
)


class AttributeConfigLevel(proto.Enum):
    r"""At which level we offer configuration for attributes."""
    ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED = 0
    PRODUCT_LEVEL_ATTRIBUTE_CONFIG = 1
    CATALOG_LEVEL_ATTRIBUTE_CONFIG = 2


class SolutionType(proto.Enum):
    r"""The type of solution."""
    SOLUTION_TYPE_UNSPECIFIED = 0
    SOLUTION_TYPE_RECOMMENDATION = 1
    SOLUTION_TYPE_SEARCH = 2


class SearchSolutionUseCase(proto.Enum):
    r"""The use case of Cloud Retail Search."""
    SEARCH_SOLUTION_USE_CASE_UNSPECIFIED = 0
    SEARCH_SOLUTION_USE_CASE_SEARCH = 1
    SEARCH_SOLUTION_USE_CASE_BROWSE = 2


class Condition(proto.Message):
    r"""Metadata that is used to define a condition that triggers an action.
    A valid condition must specify at least one of 'query_terms' or
    'products_filter'. If multiple fields are specified, the condition
    is met if all the fields are satisfied e.g. if a set of query terms
    and product_filter are set, then only items matching the
    product_filter for requests with a query matching the query terms
    wil get boosted.

    Attributes:
        query_terms (Sequence[google.cloud.retail_v2alpha.types.Condition.QueryTerm]):
            A list (up to 10 entries) of terms to match
            the query on. If not specified, match all
            queries. If many query terms are specified, the
            condition is matched if any of the terms is a
            match (i.e. using the OR operator).
        active_time_range (Sequence[google.cloud.retail_v2alpha.types.Condition.TimeRange]):
            Range of time(s) specifying when Condition is
            active. Condition true if any time range
            matches.
    """

    class QueryTerm(proto.Message):
        r"""Query terms that we want to match on.

        Attributes:
            value (str):
                The value of the term to match on.
                Value cannot be empty.
                Value can have at most 3 terms if specified as a
                partial match. Each space separated string is
                considered as one term. Example) "a b c" is 3
                terms and allowed, " a b c d" is 4 terms and not
                allowed for partial match.
            full_match (bool):
                Whether this is supposed to be a full or
                partial match.
        """

        value = proto.Field(
            proto.STRING,
            number=1,
        )
        full_match = proto.Field(
            proto.BOOL,
            number=2,
        )

    class TimeRange(proto.Message):
        r"""Used for time-dependent conditions.
        Example: Want to have rule applied for week long sale.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start of time range. Range is inclusive.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                End of time range. Range is inclusive.
        """

        start_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        end_time = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    query_terms = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=QueryTerm,
    )
    active_time_range = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=TimeRange,
    )


class Rule(proto.Message):
    r"""A rule is a condition-action pair

    -  A condition defines when a rule is to be triggered.
    -  An action specifies what occurs on that trigger. Currently only
       boost rules are supported. Currently only supported by the search
       endpoint.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        boost_action (google.cloud.retail_v2alpha.types.Rule.BoostAction):
            A boost action.

            This field is a member of `oneof`_ ``action``.
        redirect_action (google.cloud.retail_v2alpha.types.Rule.RedirectAction):
            Redirects a shopper to a specific page.

            This field is a member of `oneof`_ ``action``.
        oneway_synonyms_action (google.cloud.retail_v2alpha.types.Rule.OnewaySynonymsAction):
            Treats specific term as a synonym with a
            group of terms. Group of terms will not be
            treated as synonyms with the specific term.

            This field is a member of `oneof`_ ``action``.
        do_not_associate_action (google.cloud.retail_v2alpha.types.Rule.DoNotAssociateAction):
            Prevents term from being associated with
            other terms.

            This field is a member of `oneof`_ ``action``.
        replacement_action (google.cloud.retail_v2alpha.types.Rule.ReplacementAction):
            Replaces specific terms in the query.

            This field is a member of `oneof`_ ``action``.
        ignore_action (google.cloud.retail_v2alpha.types.Rule.IgnoreAction):
            Ignores specific terms from query during
            search.

            This field is a member of `oneof`_ ``action``.
        filter_action (google.cloud.retail_v2alpha.types.Rule.FilterAction):
            Filters results.

            This field is a member of `oneof`_ ``action``.
        twoway_synonyms_action (google.cloud.retail_v2alpha.types.Rule.TwowaySynonymsAction):
            Treats a set of terms as synonyms of one
            another.

            This field is a member of `oneof`_ ``action``.
        condition (google.cloud.retail_v2alpha.types.Condition):
            Required. The condition that triggers the
            rule. If the condition is empty, the rule will
            always apply.
    """

    class BoostAction(proto.Message):
        r"""A boost action to apply to results matching condition
        specified above.

        Attributes:
            boost (float):
                Strength of the condition boost, which must be in [-1, 1].
                Negative boost means demotion. Default is 0.0.

                Setting to 1.0 gives the item a big promotion. However, it
                does not necessarily mean that the boosted item will be the
                top result at all times, nor that other items will be
                excluded. Results could still be shown even when none of
                them matches the condition. And results that are
                significantly more relevant to the search query can still
                trump your heavily favored but irrelevant items.

                Setting to -1.0 gives the item a big demotion. However,
                results that are deeply relevant might still be shown. The
                item will have an upstream battle to get a fairly high
                ranking, but it is not blocked out completely.

                Setting to 0.0 means no boost applied. The boosting
                condition is ignored.
            products_filter (str):
                The filter can have a max size of 5000 characters. An
                expression which specifies which products to apply an action
                to. The syntax and supported fields are the same as a filter
                expression. See
                [SearchRequest.filter][google.cloud.retail.v2alpha.SearchRequest.filter]
                for detail syntax and limitations.

                Examples:

                -  To boost products with product ID "product_1" or
                   "product_2", and color "Red" or "Blue": *(id:
                   ANY("product_1", "product_2"))* *AND* *(colorFamilies:
                   ANY("Red", "Blue"))*
        """

        boost = proto.Field(
            proto.FLOAT,
            number=1,
        )
        products_filter = proto.Field(
            proto.STRING,
            number=2,
        )

    class FilterAction(proto.Message):
        r"""-  Rule Condition:

           -  No [Condition][query_terms] provided is a global match.
           -  1 or more [Condition][query_terms] provided is combined with
              OR operator.

        -  Action Input: The request query and filter that will be applied
           to the retrieved products, in addition to any filters already
           provided with the SearchRequest. The AND operator is used to
           combine the query's existing filters with the filter rule(s).
           NOTE: May result in 0 results when filters conflict.
        -  Action Result: Filters the returned objects to be ONLY those that
           passed the filter.

        Attributes:
            filter (str):
                A filter to apply on the matching condition results.
                Supported features:

                -  [filter][google.cloud.retail.v2alpha.Rule.FilterAction.filter]
                   must be set.
                -  Filter syntax is identical to
                   [SearchRequest.filter][google.cloud.retail.v2alpha.SearchRequest.filter].
                   See more details at the Retail Search `user
                   guide </retail/search/docs/filter-and-order#filter>`__.
                -  To filter products with product ID "product_1" or
                   "product_2", and color "Red" or "Blue": *(id:
                   ANY("product_1", "product_2"))* *AND* *(colorFamilies:
                   ANY("Red", "Blue"))*
        """

        filter = proto.Field(
            proto.STRING,
            number=1,
        )

    class RedirectAction(proto.Message):
        r"""Redirects a shopper to a specific page.

        -  Rule Condition:

           -  Must specify [Condition][query_terms].

        -  Action Input: Request Query
        -  Action Result: Redirects shopper to provided uri.

        Attributes:
            redirect_uri (str):
                URL must have length equal or less than 2000
                characters.
        """

        redirect_uri = proto.Field(
            proto.STRING,
            number=1,
        )

    class TwowaySynonymsAction(proto.Message):
        r"""Creates a set of terms that will be treated as synonyms of each
        other. Example: synonyms of "sneakers" and "shoes".

        -  "sneakers" will use a synonym of "shoes".
        -  "shoes" will use a synonym of "sneakers".

        Attributes:
            synonyms (Sequence[str]):
                Defines a set of synonyms.
                Can specify up to 100 synonyms.
                Must specify at least 2 synonyms.
        """

        synonyms = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class OnewaySynonymsAction(proto.Message):
        r"""Maps a set of terms to a set of synonyms. Set of synonyms will be
        treated as synonyms of each query term only. ``query_terms`` will
        not be treated as synonyms of each other. Example: "sneakers" will
        use a synonym of "shoes". "shoes" will not use a synonym of
        "sneakers".

        Attributes:
            query_terms (Sequence[str]):
                Terms from the search query.
                Will treat synonyms as their synonyms.
                Not themselves synonyms of the synonyms.
                Can specify up to 100 terms.
            synonyms (Sequence[str]):
                Defines a set of synonyms.
                Cannot contain duplicates.
                Can specify up to 100 synonyms.
            oneway_terms (Sequence[str]):
                Will be [deprecated = true] post migration;
        """

        query_terms = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        synonyms = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        oneway_terms = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class DoNotAssociateAction(proto.Message):
        r"""Prevents ``query_term`` from being associated with specified terms
        during search. Example: Don't associate "gShoe" and "cheap".

        Attributes:
            query_terms (Sequence[str]):
                Terms from the search query. Will not consider
                do_not_associate_terms for search if in search query. Can
                specify up to 100 terms.
            do_not_associate_terms (Sequence[str]):
                Cannot contain duplicates or the query term.
                Can specify up to 100 terms.
            terms (Sequence[str]):
                Will be [deprecated = true] post migration;
        """

        query_terms = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        do_not_associate_terms = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        terms = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class ReplacementAction(proto.Message):
        r"""Replaces a term in the query. Multiple replacement candidates can be
        specified. All ``query_terms`` will be replaced with the replacement
        term. Example: Replace "gShoe" with "google shoe".

        Attributes:
            query_terms (Sequence[str]):
                Terms from the search query.
                Will be replaced by replacement term.
                Can specify up to 100 terms.
            replacement_term (str):
                Term that will be used for replacement.
            term (str):
                Will be [deprecated = true] post migration;
        """

        query_terms = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        replacement_term = proto.Field(
            proto.STRING,
            number=3,
        )
        term = proto.Field(
            proto.STRING,
            number=1,
        )

    class IgnoreAction(proto.Message):
        r"""Prevents a term in the query from being used in search.
        Example: Don't search for "shoddy".

        Attributes:
            ignore_terms (Sequence[str]):
                Terms to ignore in the search query.
        """

        ignore_terms = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    boost_action = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message=BoostAction,
    )
    redirect_action = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message=RedirectAction,
    )
    oneway_synonyms_action = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message=OnewaySynonymsAction,
    )
    do_not_associate_action = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message=DoNotAssociateAction,
    )
    replacement_action = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message=ReplacementAction,
    )
    ignore_action = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message=IgnoreAction,
    )
    filter_action = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="action",
        message=FilterAction,
    )
    twoway_synonyms_action = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="action",
        message=TwowaySynonymsAction,
    )
    condition = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Condition",
    )


class Audience(proto.Message):
    r"""An intended audience of the
    [Product][google.cloud.retail.v2alpha.Product] for whom it's sold.

    Attributes:
        genders (Sequence[str]):
            The genders of the audience. Strongly encouraged to use the
            standard values: "male", "female", "unisex".

            At most 5 values are allowed. Each value must be a UTF-8
            encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `gender <https://support.google.com/merchants/answer/6324479>`__.
            Schema.org property
            `Product.audience.suggestedGender <https://schema.org/suggestedGender>`__.
        age_groups (Sequence[str]):
            The age groups of the audience. Strongly encouraged to use
            the standard values: "newborn" (up to 3 months old),
            "infant" (3–12 months old), "toddler" (1–5 years old),
            "kids" (5–13 years old), "adult" (typically teens or older).

            At most 5 values are allowed. Each value must be a UTF-8
            encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `age_group <https://support.google.com/merchants/answer/6324463>`__.
            Schema.org property
            `Product.audience.suggestedMinAge <https://schema.org/suggestedMinAge>`__
            and
            `Product.audience.suggestedMaxAge <https://schema.org/suggestedMaxAge>`__.
    """

    genders = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    age_groups = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ColorInfo(proto.Message):
    r"""The color information of a
    [Product][google.cloud.retail.v2alpha.Product].

    Attributes:
        color_families (Sequence[str]):
            The standard color families. Strongly recommended to use the
            following standard color groups: "Red", "Pink", "Orange",
            "Yellow", "Purple", "Green", "Cyan", "Blue", "Brown",
            "White", "Gray", "Black" and "Mixed". Normally it is
            expected to have only 1 color family. May consider using
            single "Mixed" instead of multiple values.

            A maximum of 5 values are allowed. Each value must be a
            UTF-8 encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `color <https://support.google.com/merchants/answer/6324487>`__.
            Schema.org property
            `Product.color <https://schema.org/color>`__.
        colors (Sequence[str]):
            The color display names, which may be different from
            standard color family names, such as the color aliases used
            in the website frontend. Normally it is expected to have
            only 1 color. May consider using single "Mixed" instead of
            multiple values.

            A maximum of 25 colors are allowed. Each value must be a
            UTF-8 encoded string with a length limit of 128 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Google Merchant Center property
            `color <https://support.google.com/merchants/answer/6324487>`__.
            Schema.org property
            `Product.color <https://schema.org/color>`__.
    """

    color_families = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    colors = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CustomAttribute(proto.Message):
    r"""A custom attribute that is not explicitly modeled in
    [Product][google.cloud.retail.v2alpha.Product].

    Attributes:
        text (Sequence[str]):
            The textual values of this custom attribute. For example,
            ``["yellow", "green"]`` when the key is "color".

            Empty string is not allowed. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Exactly one of
            [text][google.cloud.retail.v2alpha.CustomAttribute.text] or
            [numbers][google.cloud.retail.v2alpha.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
        numbers (Sequence[float]):
            The numerical values of this custom attribute. For example,
            ``[2.3, 15.4]`` when the key is "lengths_cm".

            Exactly one of
            [text][google.cloud.retail.v2alpha.CustomAttribute.text] or
            [numbers][google.cloud.retail.v2alpha.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
        searchable (bool):
            This field will only be used when
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2alpha.AttributesConfig.attribute_config_level]
            of the [Catalog][google.cloud.retail.v2alpha.Catalog] is
            'PRODUCT_LEVEL_ATTRIBUTE_CONFIG', if true, custom attribute
            values are searchable by text queries in
            [SearchService.Search][google.cloud.retail.v2alpha.SearchService.Search].

            This field is ignored in a
            [UserEvent][google.cloud.retail.v2alpha.UserEvent].

            Only set if type
            [text][google.cloud.retail.v2alpha.CustomAttribute.text] is
            set. Otherwise, a INVALID_ARGUMENT error is returned.

            This field is a member of `oneof`_ ``_searchable``.
        indexable (bool):
            This field will only be used when
            [AttributesConfig.attribute_config_level][google.cloud.retail.v2alpha.AttributesConfig.attribute_config_level]
            of the [Catalog][google.cloud.retail.v2alpha.Catalog] is
            'PRODUCT_LEVEL_ATTRIBUTE_CONFIG', if true, custom attribute
            values are indexed, so that it can be filtered, faceted or
            boosted in
            [SearchService.Search][google.cloud.retail.v2alpha.SearchService.Search].

            This field is ignored in a
            [UserEvent][google.cloud.retail.v2alpha.UserEvent].

            See
            [SearchRequest.filter][google.cloud.retail.v2alpha.SearchRequest.filter],
            [SearchRequest.facet_specs][google.cloud.retail.v2alpha.SearchRequest.facet_specs]
            and
            [SearchRequest.boost_spec][google.cloud.retail.v2alpha.SearchRequest.boost_spec]
            for more details.

            This field is a member of `oneof`_ ``_indexable``.
    """

    text = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    numbers = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )
    searchable = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    indexable = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class FulfillmentInfo(proto.Message):
    r"""Fulfillment information, such as the store IDs for in-store
    pickup or region IDs for different shipping methods.

    Attributes:
        type_ (str):
            The fulfillment type, including commonly used types (such as
            pickup in store and same day delivery), and custom types.
            Customers have to map custom types to their display names
            before rendering UI.

            Supported values:

            -  "pickup-in-store"
            -  "ship-to-store"
            -  "same-day-delivery"
            -  "next-day-delivery"
            -  "custom-type-1"
            -  "custom-type-2"
            -  "custom-type-3"
            -  "custom-type-4"
            -  "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.
        place_ids (Sequence[str]):
            The IDs for this
            [type][google.cloud.retail.v2alpha.FulfillmentInfo.type],
            such as the store IDs for
            [FulfillmentInfo.type.pickup-in-store][google.cloud.retail.v2alpha.FulfillmentInfo.type]
            or the region IDs for
            [FulfillmentInfo.type.same-day-delivery][google.cloud.retail.v2alpha.FulfillmentInfo.type].

            A maximum of 3000 values are allowed. Each value must be a
            string with a length limit of 30 characters, matching the
            pattern ``[a-zA-Z0-9_-]+``, such as "store1" or "REGION-2".
            Otherwise, an INVALID_ARGUMENT error is returned.
    """

    type_ = proto.Field(
        proto.STRING,
        number=1,
    )
    place_ids = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Image(proto.Message):
    r"""[Product][google.cloud.retail.v2alpha.Product] image.
    Recommendations AI and Retail Search do not use product images to
    improve prediction and search results. However, product images can
    be returned in results, and are shown in prediction or search
    previews in the console.

    Attributes:
        uri (str):
            Required. URI of the image.

            This field must be a valid UTF-8 encoded URI with a length
            limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Google Merchant Center property
            `image_link <https://support.google.com/merchants/answer/6324350>`__.
            Schema.org property
            `Product.image <https://schema.org/image>`__.
        height (int):
            Height of the image in number of pixels.

            This field must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
        width (int):
            Width of the image in number of pixels.

            This field must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
    )
    height = proto.Field(
        proto.INT32,
        number=2,
    )
    width = proto.Field(
        proto.INT32,
        number=3,
    )


class Interval(proto.Message):
    r"""A floating point interval.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        minimum (float):
            Inclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        exclusive_minimum (float):
            Exclusive lower bound.

            This field is a member of `oneof`_ ``min``.
        maximum (float):
            Inclusive upper bound.

            This field is a member of `oneof`_ ``max``.
        exclusive_maximum (float):
            Exclusive upper bound.

            This field is a member of `oneof`_ ``max``.
    """

    minimum = proto.Field(
        proto.DOUBLE,
        number=1,
        oneof="min",
    )
    exclusive_minimum = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="min",
    )
    maximum = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="max",
    )
    exclusive_maximum = proto.Field(
        proto.DOUBLE,
        number=4,
        oneof="max",
    )


class PriceInfo(proto.Message):
    r"""The price information of a
    [Product][google.cloud.retail.v2alpha.Product].

    Attributes:
        currency_code (str):
            The 3-letter currency code defined in `ISO
            4217 <https://www.iso.org/iso-4217-currency-codes.html>`__.

            If this field is an unrecognizable currency code, an
            INVALID_ARGUMENT error is returned.

            The
            [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2alpha.Product]s with the
            same
            [Product.primary_product_id][google.cloud.retail.v2alpha.Product.primary_product_id]
            must share the same
            [currency_code][google.cloud.retail.v2alpha.PriceInfo.currency_code].
            Otherwise, a FAILED_PRECONDITION error is returned.
        price (float):
            Price of the product.

            Google Merchant Center property
            `price <https://support.google.com/merchants/answer/6324371>`__.
            Schema.org property
            `Offer.price <https://schema.org/price>`__.
        original_price (float):
            Price of the product without any discount. If zero, by
            default set to be the
            [price][google.cloud.retail.v2alpha.PriceInfo.price].
        cost (float):
            The costs associated with the sale of a particular product.
            Used for gross profit reporting.

            -  Profit =
               [price][google.cloud.retail.v2alpha.PriceInfo.price] -
               [cost][google.cloud.retail.v2alpha.PriceInfo.cost]

            Google Merchant Center property
            `cost_of_goods_sold <https://support.google.com/merchants/answer/9017895>`__.
        price_effective_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the
            [price][google.cloud.retail.v2alpha.PriceInfo.price] starts
            to be effective. This can be set as a future timestamp, and
            the [price][google.cloud.retail.v2alpha.PriceInfo.price] is
            only used for search after
            [price_effective_time][google.cloud.retail.v2alpha.PriceInfo.price_effective_time].
            If so, the
            [original_price][google.cloud.retail.v2alpha.PriceInfo.original_price]
            must be set and
            [original_price][google.cloud.retail.v2alpha.PriceInfo.original_price]
            is used before
            [price_effective_time][google.cloud.retail.v2alpha.PriceInfo.price_effective_time].

            Do not set if
            [price][google.cloud.retail.v2alpha.PriceInfo.price] is
            always effective because it will cause additional latency
            during search.
        price_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the
            [price][google.cloud.retail.v2alpha.PriceInfo.price] stops
            to be effective. The
            [price][google.cloud.retail.v2alpha.PriceInfo.price] is used
            for search before
            [price_expire_time][google.cloud.retail.v2alpha.PriceInfo.price_expire_time].
            If this field is set, the
            [original_price][google.cloud.retail.v2alpha.PriceInfo.original_price]
            must be set and
            [original_price][google.cloud.retail.v2alpha.PriceInfo.original_price]
            is used after
            [price_expire_time][google.cloud.retail.v2alpha.PriceInfo.price_expire_time].

            Do not set if
            [price][google.cloud.retail.v2alpha.PriceInfo.price] is
            always effective because it will cause additional latency
            during search.
        price_range (google.cloud.retail_v2alpha.types.PriceInfo.PriceRange):
            Output only. The price range of all the child
            [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2alpha.Product]s grouped
            together on the
            [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product]. Only
            populated for
            [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product]s.

            Note: This field is OUTPUT_ONLY for
            [ProductService.GetProduct][google.cloud.retail.v2alpha.ProductService.GetProduct].
            Do not set this field in API requests.
    """

    class PriceRange(proto.Message):
        r"""The price range of all
        [variant][google.cloud.retail.v2alpha.Product.Type.VARIANT]
        [Product][google.cloud.retail.v2alpha.Product] having the same
        [Product.primary_product_id][google.cloud.retail.v2alpha.Product.primary_product_id].

        Attributes:
            price (google.cloud.retail_v2alpha.types.Interval):
                The inclusive
                [Product.pricing_info.price][google.cloud.retail.v2alpha.PriceInfo.price]
                interval of all
                [variant][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2alpha.Product] having the
                same
                [Product.primary_product_id][google.cloud.retail.v2alpha.Product.primary_product_id].
            original_price (google.cloud.retail_v2alpha.types.Interval):
                The inclusive
                [Product.pricing_info.original_price][google.cloud.retail.v2alpha.PriceInfo.original_price]
                internal of all
                [variant][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2alpha.Product] having the
                same
                [Product.primary_product_id][google.cloud.retail.v2alpha.Product.primary_product_id].
        """

        price = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Interval",
        )
        original_price = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Interval",
        )

    currency_code = proto.Field(
        proto.STRING,
        number=1,
    )
    price = proto.Field(
        proto.FLOAT,
        number=2,
    )
    original_price = proto.Field(
        proto.FLOAT,
        number=3,
    )
    cost = proto.Field(
        proto.FLOAT,
        number=4,
    )
    price_effective_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    price_expire_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    price_range = proto.Field(
        proto.MESSAGE,
        number=7,
        message=PriceRange,
    )


class Rating(proto.Message):
    r"""The rating of a [Product][google.cloud.retail.v2alpha.Product].

    Attributes:
        rating_count (int):
            The total number of ratings. This value is independent of
            the value of
            [rating_histogram][google.cloud.retail.v2alpha.Rating.rating_histogram].

            This value must be nonnegative. Otherwise, an
            INVALID_ARGUMENT error is returned.
        average_rating (float):
            The average rating of the
            [Product][google.cloud.retail.v2alpha.Product].

            The rating is scaled at 1-5. Otherwise, an INVALID_ARGUMENT
            error is returned.
        rating_histogram (Sequence[int]):
            List of rating counts per rating value (index = rating - 1).
            The list is empty if there is no rating. If the list is
            non-empty, its size is always 5. Otherwise, an
            INVALID_ARGUMENT error is returned.

            For example, [41, 14, 13, 47, 303]. It means that the
            [Product][google.cloud.retail.v2alpha.Product] got 41
            ratings with 1 star, 14 ratings with 2 star, and so on.
    """

    rating_count = proto.Field(
        proto.INT32,
        number=1,
    )
    average_rating = proto.Field(
        proto.FLOAT,
        number=2,
    )
    rating_histogram = proto.RepeatedField(
        proto.INT32,
        number=3,
    )


class UserInfo(proto.Message):
    r"""Information of an end user.

    Attributes:
        user_id (str):
            Highly recommended for logged-in users. Unique identifier
            for logged-in user, such as a user name.

            Always use a hashed value for this ID.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        ip_address (str):
            The end user's IP address. This field is used to extract
            location information for personalization.

            This field must be either an IPv4 address (e.g.
            "104.133.9.80") or an IPv6 address (e.g.
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334"). Otherwise, an
            INVALID_ARGUMENT error is returned.

            This should not be set when:

            -  setting
               [SearchRequest.user_info][google.cloud.retail.v2alpha.SearchRequest.user_info].
            -  using the JavaScript tag in
               [UserEventService.CollectUserEvent][google.cloud.retail.v2alpha.UserEventService.CollectUserEvent]
               or if
               [direct_user_request][google.cloud.retail.v2alpha.UserInfo.direct_user_request]
               is set.
        user_agent (str):
            User agent as included in the HTTP header. Required for
            getting
            [SearchResponse.sponsored_results][google.cloud.retail.v2alpha.SearchResponse.sponsored_results].

            The field must be a UTF-8 encoded string with a length limit
            of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            This should not be set when using the client side event
            reporting with GTM or JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.retail.v2alpha.UserEventService.CollectUserEvent]
            or if
            [direct_user_request][google.cloud.retail.v2alpha.UserInfo.direct_user_request]
            is set.
        direct_user_request (bool):
            True if the request is made directly from the end user, in
            which case the
            [ip_address][google.cloud.retail.v2alpha.UserInfo.ip_address]
            and
            [user_agent][google.cloud.retail.v2alpha.UserInfo.user_agent]
            can be populated from the HTTP request. This flag should be
            set only if the API request is made directly from the end
            user such as a mobile app (and not if a gateway or a server
            is processing and pushing the user events).

            This should not be set when using the JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.retail.v2alpha.UserEventService.CollectUserEvent].
    """

    user_id = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address = proto.Field(
        proto.STRING,
        number=2,
    )
    user_agent = proto.Field(
        proto.STRING,
        number=3,
    )
    direct_user_request = proto.Field(
        proto.BOOL,
        number=4,
    )


class LocalInventory(proto.Message):
    r"""The inventory information at a place (e.g. a store)
    identified by a place ID.

    Attributes:
        place_id (str):
            The place ID for the current set of inventory
            information.
        price_info (google.cloud.retail_v2alpha.types.PriceInfo):
            Product price and cost information.

            Google Merchant Center property
            `price <https://support.google.com/merchants/answer/6324371>`__.
        attributes (Mapping[str, google.cloud.retail_v2alpha.types.CustomAttribute]):
            Additional local inventory attributes, for example, store
            name, promotion tags, etc.

            This field needs to pass all below criteria, otherwise an
            INVALID_ARGUMENT error is returned:

            -  At most 30 attributes are allowed.
            -  The key must be a UTF-8 encoded string with a length
               limit of 32 characters.
            -  The key must match the pattern:
               ``[a-zA-Z0-9][a-zA-Z0-9_]*``. For example, key0LikeThis
               or KEY_1_LIKE_THIS.
            -  The attribute values must be of the same type (text or
               number).
            -  Only 1 value is allowed for each attribute.
            -  For text values, the length limit is 256 UTF-8
               characters.
            -  The attribute does not support search. The ``searchable``
               field should be unset or set to false.
            -  The max summed total bytes of custom attribute keys and
               values per product is 5MiB.
        fulfillment_types (Sequence[str]):
            Input only. Supported fulfillment types. Valid fulfillment
            type values include commonly used types (such as pickup in
            store and same day delivery), and custom types. Customers
            have to map custom types to their display names before
            rendering UI.

            Supported values:

            -  "pickup-in-store"
            -  "ship-to-store"
            -  "same-day-delivery"
            -  "next-day-delivery"
            -  "custom-type-1"
            -  "custom-type-2"
            -  "custom-type-3"
            -  "custom-type-4"
            -  "custom-type-5"

            If this field is set to an invalid value other than these,
            an INVALID_ARGUMENT error is returned.

            All the elements must be distinct. Otherwise, an
            INVALID_ARGUMENT error is returned.
    """

    place_id = proto.Field(
        proto.STRING,
        number=1,
    )
    price_info = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PriceInfo",
    )
    attributes = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message="CustomAttribute",
    )
    fulfillment_types = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
