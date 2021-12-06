# Search with boosting tutorial

## Get started

Boosting is a powerful and convenient feature that lets you prioritize products that match certain conditions.
To specify a condition, you can use filtering expressions.

A boosting specification can be based on a single field condition or on multiple fields. Also, you can combine several specifications into one boosting request.

In this tutorial you will learn some examples of product boosting.

<walkthrough-tutorial-duration duration="7"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Select your project and enable the Retail API

Google Cloud organizes resources into projects. This lets you
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet or you're not the owner of an existing one, you can
[create a new project](https://console.cloud.google.com/projectcreate).

After the project is created, set your PROJECT_ID to a ```project``` variable.
1. Run the following command in Terminal:
    ```bash
    gcloud config set project <YOUR_PROJECT_ID>
    ```

1. Check that the Retail API is enabled for your Project in the [Admin Console](https://console.cloud.google.com/ai/retail/).

### Set up authentication

To run a code sample from the Cloud Shell, you need to authenticate. To do this, use the Application Default Credentials.

1. Set your user credentials to authenticate your requests to the Retail API

    ```bash
    gcloud auth application-default login
    ```

1. Type `Y` and press **Enter**. Click the link in Terminal. A browser window should appear asking you to log in using your Gmail account.

1. Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

1. Run the code sample and check the Retail API in action.

**Note**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

### Set the PROJECT_NUMBER environment variable

Because you are going to run the code samples in your own Google Cloud project, you should specify the **project_number** as an environment variable. It will be used in every request to the Retail API.

1. You can find the ```project_number``` in the Project Info card displayed on **Home/Dashboard**.

1. Set the environment variable with the following command:
    ```bash
    export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
    ```

### Install Google Cloud Retail libraries

To run Python code samples for the Retail API tutorial, you need to set up your virtual environment.

1. Run the following commands in a Terminal to create an isolated Python environment:
    ```bash
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
    ```
1. Next, install Google packages:
    ```bash
    pip install google
    pip install google-cloud-retail
    pip install google.cloud.storage
    pip install google.cloud.bigquery

    ```

## Clone the Retail code samples

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

Clone the Git repository with all the code samples to learn the Retail features and check them in action.

<!-- TODO(ianan): change the repository link -->
1. Run the following command in the Terminal:
    ```bash
    git clone https://github.com/t-karasova/grs-samples-python.git
    ```

    The code samples for each of the Retail services are stored in different directories.

1. Go to the ```grs-samples-python``` directory. It's our starting point to run more commands.
    ```bash
    cd grs-samples-python
    ```

## Import catalog data

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Upload catalog data to Cloud Storage

There is a JSON file with valid products prepared in the `product` directory:
`resources/products.json`.

Another file, `resources/products_some_invalid.json`, contains both valid and invalid products, and you will use it to check the error handling.

In your own project, create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it `<YOUR_PROJECT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file, run the following command in the Terminal:

    ```bash
    python product/setup/product_create_gcs_bucket.py
    ```

    Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the files are uploaded.

1. The name of the created Retail Search bucket is printed in the Terminal. Copy the name and set it as the environment variable `BUCKET_NAME`:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail Catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Boost by one criterion: condition and filtering expression

The boosting specification looks like this:

```
  condition_boost_specs {
         condition: string
         boost: double [-1;1]
    }
```

1. To set the **```condition```**, you should use a filtering expression like the following:

    ```'(colorFamily: ANY("blue"))'```

    or
    ```'(rating: IN(4.0, 5.0))'```

    <!-- TODO(ianan): change Filtering Tutorial link -->
    You can learn how to use filters in the [Filtering Tutorial](retail_api_v2_filtering_python.md)
    or read about it in the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

    The field **```boost```** defines the strength of the condition boost, which should be in the range of -1 to 1. Negative boost means demotion.

1. Now open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="boost.*0">search_with_boost_spec.py</walkthrough-editor-select-regex>.


    In the initial request, the boost strength is set to zero: ```boost = 0.0```,
    so the boosting will not affect the order of the   products in the response.


## Boost by one criterion: Boost results

1. Run the sample in a terminal with the following command:
    ```bash
    python search/search_with_boost_spec.py
    ```
1. Check the response to see the original order of products depending on their relevance to the query phrase.

1. Next, change the value of the field **boost** and run the code sample again:
    ```boost = 1.0```

1. Now you can check the results. The products corresponding to the boost condition became reranked. Now blue products are on the top of the list.

1. If you set ```boost = -1.0```, blue products will appear at the bottom of the search result.

## Some notes about boosting

Setting the boost strength to 1.0 gives the item a strong promotion. However, it does not necessarily mean that the boosted item will be the top result at all times, nor that other items will be excluded.
Results could still be shown even when none of them matches the condition.

Also, results that are significantly more relevant to the search query can still be ranked higher than your heavily favored but irrelevant items.

You can combine up to 10 boost specifications in one search request. In this way, you can apply really sophisticated boosting rules to your search request.

## Try different boosting conditions

Feel free to test product boosting yourself right now in the Cloud Shell environment.

Replace the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="condition = '.*'">condition</walkthrough-editor-select-regex> expression with something like this:

```
condition = '(categories: ANY("Office"))'
```

Or
```
condition = '(attributes.material: ANY("Cotton", "Polyester")) AND (brands: ANY("Google"))'
```

At the same time, you can test the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="boost = (\D)?\d.*">boost strength</walkthrough-editor-select-regex> by setting any value from -1 to 1.

## Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice).

To check the list of text and numeric fields that support boosting, use the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter).

## Error handling results

If you try to boost the search results and set a condition in the field that is not supported for boosting (for example, the **name** field), you will get an error message.

1. Change the variable <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="condition = '.*'">condition</walkthrough-editor-select-regex> value to the following:
    ``` condition = '(name: ANY("some_random"))'```

1. Run the code again:
    ```bash
    python search/search_with_boost_spec.py
    ```

1. You should see the following error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(name: ANY("some_random"))'. Parsing filter failed with error: Unsupported field "name" on ":" operator.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the boosting by yourself and try different combinations of various filter expressions.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
