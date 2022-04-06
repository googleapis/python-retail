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

## Prediction service. Filter the recommendations

Filter the recommendations returned by Recommendations AI by using the `filter` field in the `PredictRequest`.

The filter field accepts two forms of filter specification:
    - filterOutOfStockItems    
    - tag expressions

You can combine these two types of filters, only items that satisfy all specified filter expressions are returned.

## Filter out of stock products

The `filterOutOfStockItems` flag filters out any products with `OUT_OF_STOCK` availability.

Add the field `filter` to a `PredictRequest` in the code sample, and set the `filterOutOfStockItems` flag:
```python
filter: "filterOutOfStockItems"
```

Run the code and check the list of recommended products in the response:
    ```bash
    python predict/<...>.py
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
    python predict/<...>.py
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

## Error handling

The error message could be received if the filtering expression is written with the syntax error.
Try to ser the following filtering expression to the `fiter` field:
```python
filter: 'tags="promotional", "premium"'
```
Run the code sample and check the following error message is returned:

```
//TODO
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to experiment with getting predictions by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>

### Do more with the Retail Recommendations

<walkthrough-tutorial-card tutorialid="retail__retail_api_v2_<...>" icon="LOGO_PYTHON" title="<...>" keepPrevious=true>
<...></walkthrough-tutorial-card>
