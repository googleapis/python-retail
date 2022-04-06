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

```params.priceRerankLevel = 'low-price-reranking'```

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

    ```params.diversityLevel = 'low-diversity'```

Run the code sample:
    ```bash
    python predict/get_prediction.py
    ```
Next, change the parameter value to `high-diversity`, run the code again and check the products in the response belongs to different categories.

## Error handling

The error message could be received if the `params` field is set with invalid parameter value.
Try to request predictions the following parameter:
    ```python
    params.diversityLevel = 'invald-diversity'
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
