<walkthrough-metadata>
  <meta name="title" content="Getting The Recommendations. Prediction Service" />
  <meta name="description" content="Prediction service features" />
  <meta name="component_id" content="593554" />
  <meta name="short_id" content="true" />
</walkthrough-metadata>

# Getting The Recommendations. Prediction service features

## Introduction

This is the third part of the complex tutorial "Getting The Recommendation".

Before you can request predictions from Recommendations AI, you need a trained and tuned recommendation model and one or more active serving configurations.

//TODO - add the linc to the tutorial
To learn how to prepare the data in a Retail catalog and to ingest the historical user events, go through the tutorial <...>

To create and train a recommendation model, proceed with the video tutorial: <...>


The detailed information about the recommendation service could be found in the [Retail API documentation](https://cloud.google.com/retail/docs/predict#recommendations-predict-java).

<walkthrough-tutorial-duration duration="10"></walkthrough-tutorial-duration>

<<_shared/_set_up_env_python.md>>

## Prediction service. Simple request

//TODO check the file path
1. Open <walkthrough-editor-select-regex filePath="cloudshell_open/python-retail/samples/interactive-tutorials/prediction/get_prediction.py" regex="# get prodciction request">prediction/get_prediction.py</walkthrough-editor-select-regex> file and check the `PredictRequest` request.

1. Set the following fields to send the `PredictRequest` request:
    - `placement`—the ID of the Recommendations AI placement. Before you can request predictions from your model, you must create at least one placement for it.
    - `user_event`—context about the user, what they are looking at and what action they took to trigger the predict request.
    - `page_size`—maximum number of results to return per page. If zero, the service will choose a reasonable default. The maximum allowed value is 100.
    - `page_token`—the previous PredictResponse.next_page_token.
    - `filter`—filter for restricting prediction results with a length limit of 5,000 characters. The filter can be applied to the field `tags` or can be used the `filterOutOfStockItems` flag.
    - `params`—additional domain specific parameters for the predictions.
    - `labels`—the labels applied to a resource. More about the labels could be found in the [documentation](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).
   
1. To send simplest PredictRequest to the Retail API, run the code sample:

    ```bash
    python predict/get_prediction.py
    ```

1. Check the response in the Terminal. The PredictionResult consists of the following fields:
   -`results[]`-a list of recommended products. The products are ordered by relevance - from the most relevant product to the least.
   -`attribution_token`-a unique attribution token. The attribute which is used to track the recommendation model performance.
   -`missing_ids[]`-IDs of products in the request that were missing from the inventory.
   
## Prediction service. Price reranking

Price reranking causes recommended products with a similar recommendation probability to be ordered by price. 
Recommendation relevance is still a main reranking factor, enabling price reranking is not the same as sorting by price.

The price reranking can be set when creating a serving configuration in Cloud Console, 
that setting applies to all recommendations served by that configuration, without any further action required.

If you need to control the price reranking of a particular recommendation, you can do so via the Retail API using the PredictRequest.params field. 
This overrides any configuration-level reranking setting that would otherwise apply to this recommendation.

To rerank the products on the request-level, adjust the request with the field
`params.priceRerankLevel`, the value of this field should to be one of the following:
   -`no-price-reranking`, 
   -`low-price-reranking`, 
   -`medium-price-reranking`, 
   -`high-price-reranking`. 

Edit the PredictRequest in the <...> - add the following field to the request and check the recommended products:

```params.priceRerankLevel = low-price-reranking```

Run the code sample:
    ```bash
    python predict/get_prediction.py
    ```

Next, change the parameter value to `high-price-reranking`, run the code again and check how the order of the products in the response is changed.

## Prediction service. Recommendation diversity

Diversification affects whether results returned in single prediction response are from different categories of your product catalog.

Diversification can be set on the serving configuration level, or per prediction request.
If a diversification is set when creating a serving configuration in Cloud Console, 
that setting applies to all recommendations served by that configuration by default, 
without any further action required.

If it is needed to control the diversity of a particular recommendation, it can be made via the Retail API using the `PredictRequest.params` field. 
This overrides any configuration-level diversification setting that would otherwise apply to this recommendation.

To adjusts prediction results based on product category, set the `params.diversityLevel` field with one of the following values:
-`no-diversity`, 
-`low-diversity`, 
-`medium-diversity`, 
-`high-diversity`, 
-`auto-diversity`.

Edit the PredictRequest in the <...> - add the following field to the request and check the recommended products, they should belong to the same product category:

```params.diversityLevel = low-diversity```

Run the code sample:
    ```bash
    python predict/get_prediction.py
    ```
Next, change the parameter value to `high-diversity`, run the code again and check the products in the response belongs to different categories.

## Prediction service. Using recommendation filters

Filter the recommendations returned by Recommendations AI by using the `filter` field in the `PredictRequest`.

The filter field accepts two forms of filter specification:
    - filterOutOfStockItems    
    - tag expressions

You can combine these two types of filters; only items that satisfy all specified filter expressions are returned.

## Filter out of stock products

The `filterOutOfStockItems` flag filters out any products with `OUT_OF_STOCK` availability.

Add the field `filter` to a `PredictRequest` in the code sample, and set the `filterOutOfStockItems` flag:
```python
filter: "filterOutOfStockItems"
```

Run the code and check the list of recommended products in the response:
    ```bash
    python predict/get_prediction.py
    ```
The prediction response contains only products, which `availability` status other than `OUT_OF_STOCK`.

Next, remove the filter, run the code gain and compare the results. 
All the products, even those that are out of stock are returned.

## Filter with tag expressions 

To apply the filtering by tag expressions, the products in a catalog should have the field `tags`.

Simple tag expression, which can be applied in this tutorial, is the following:
```python
filter: 'tag="promotional"'
```
Run the code sample and check the response contains only products with this tag:
    ```bash
    python predict/get_prediction.py
    ```

When filtering by several tags, only products, that satisfy **all** specified filter expressions are returned.

To check that, add one more tag to the filter and rerun the code sample:
//TODO - check if such products exists
```python
filter: 'tag="promotional" tag="season sale"'
```

**Note:** "Recently viewed" models don't support tag filtering at the moment.

## Use boolean operators in tag expressions

Tag expressions can contain the boolean operators `OR` or `NOT`, in such case the expressions must be enclosed in parentheses. 
* A dash (-) symbol is an equivalent to the `NOT` operator.

Set the following filter expression:
//TODO - check if such products exists
```python
filter: 'tag=("promotional" OR "premium") tag=(-"season sale") filterOutOfStockItems'
```
Check the response, the Prediction service returns only items that are in stock, that have either the `premium` or the `promotional` tag (or both) and also does not have the `season sale` tag.

## Strict filtering

If your filter blocks all prediction results, the API will return generic (unfiltered) popular products. 

Set the filter expression which definitely results in an empty product set:
```python
filter: 'tag="promotional" tag=(-"promotional")'
```
Set the parameter `strictFiltering` to false:
```python
params.strictFiltering = False
```
Run the code sample and check the prediction response contains some (popular) recommended products.

If you only want results strictly matching the filters, set `params.strictFiltering` to `True` in the PredictRequest to receive empty results instead. 
```python
params.strictFiltering = True
```
Run the code sample again, the prediction response now is empty.

**Note:** the API will never return items with storageStatus of "EXPIRED" or "DELETED" regardless of filter choices.

## Return products or scores

There are two parameters in the `PredictionRequest` which define either the response will contain the product objects or only the products scores:
    - returnProduct - If set to true, the associated product object will be returned in the `results.metadata` field in the prediction response.
    - returnScore - If set to true, the prediction 'score' corresponding to each returned product will be set in the `results.metadata` field in the prediction response. 
                    The given 'score' indicates the probability of a product being clicked/purchased given the user's context and history.

Add the `returnProduct` parameter to the `ProdictRequest`:
```python
params.returnProduct = True
```
Run the code sample and check the product objects are returned.

Next, set the `returnScore` parameter and check the response:
```python
params.returnScore = True
```
Now the response contains only the probability score, like this:

//TODO add the example of a response
