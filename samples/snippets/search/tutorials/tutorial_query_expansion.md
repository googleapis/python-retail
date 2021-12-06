# Query Expansion tutorial

## Get started

This tutorial shows you how to enable the query expansion feature to increase the efficiency for search for ambiguous or long-tail query terms.

Disabling the query expansion results in using only the exact search query, even if the total number of search results is zero.

You can enable the query expansion feature and let the Google Retail Search build an automatic query expansion.

You can also pin unexpanded products so that they always appear at the top of search results followed by products enlisted via expansion.

This feature helps you to enhance a customer experience.

<walkthrough-tutorial-duration duration="5"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Select your project and enable the Retail API

Google Cloud organizes resources into projects. This lets you
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet or you're not the Owner of an existing one, you can
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

1. You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

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

In your own project you need to create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it as <YOUR_PROJECT_ID>_<TIMESTAMP>.

1. To create the bucket and upload the JSON file run the following command in the Terminal:

    ```bash
    python product/setup/product_create_gcs_bucket.py
    ```

    Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the files are uploaded.

1. The name of the created GRS bucket is printed in the Terminal. Copy the name and set it as the environment variable  `BUCKET_NAME`:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail Catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Query expansion: AUTO condition

1. Open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_query_expansion_spec.py" regex="TRY DIFFERENT QUERY EXPANSION CONDITION HERE">search_with_query_expansion_spec.py</walkthrough-editor-select-regex>.

1. Here you can see the query expansion condition set with value `AUTO`. The setting enables the query expansion feature and expands the search results.

1. Run the sample in the Terminal using the command:
    ```bash
    python search/search_with_query_expansion_spec.py
    ```

As you can see, the results contain products that do not exactly match the search query but are close to it.

## Query expansion: DISABLED condition

Change the condition value to `DISABLED`.

1. Change the condition under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_query_expansion_spec.py" regex="TRY DIFFERENT QUERY EXPANSION CONDITION HERE">comment</walkthrough-editor-select-regex> to the following:

    ```condition = SearchRequest.QueryExpansionSpec.Condition.DISABLED```

1. Run the sample in the Terminal using the command:

    ```bash
    python search/search_with_query_expansion_spec.py
    ```

As you can see, the results contain only items that exactly match the search query.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the query expansion by yourself and try different search phrases with and without query expansion.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
