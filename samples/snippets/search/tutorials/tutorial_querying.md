# Query tutorial

## Get started

This tutorial shows you how to send a simple search query to the Retail Service and analyze the response.


<walkthrough-tutorial-duration duration="4"></walkthrough-tutorial-duration>

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

Another file, `resources/products_some_invalid.json`, contains both valid and invalid products, and you use it to check the error handling.

In your own project you need to create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it the same as your project ID.

1. To create the bucket and upload the JSON file run the following command in the Terminal:

    ```bash
    python product/setup/product_create_gcs_bucket.py
    ```

    Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the files are uploaded.

1. The name of the created GRS bucket is printed in the Terminal. Copy the name and set it as the environment variable `BUCKET_NAME`:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail Catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Simple query request

The simple search request contains only the following required fields:
- `placement` — a resource name of the search engine placement.
- `visitor_id` — a unique identifier to track visitors.
- `query` — a raw search query or search phrase.

To check the results right away, you need to run a request on a products catalog.

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_simple_query.py" regex="TRY DIFFERENT QUERY PHRASES HERE">search_simple_query.py</walkthrough-editor-select-regex> to review the request.

1. To request the search service with a `Hoodie` query, run the following command in Terminal:
    ```bash
    python search/search_simple_query.py
    ```

1. Notee that the results contain a list of matched items returned by the Retail Search service.

    - `total_size` is the estimated total count of matched items.

    - `attribution_token` is a unique search token that enables accurate attribution of the search model performance.

    - `next_page_token` is a token that forwards to the next page in the search response. By default, the number of products per page is 100. If this field is omitted, there are no subsequent pages.

## Simple query: query phrase calibrating

Next, try to experiment with the query phrases.

1. Find the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_simple_query.py" regex="TRY DIFFERENT QUERY PHRASES HERE">comment</walkthrough-editor-select-regex> and replace the value of `query_phrase` with the following samples:

    ```
    query_phrase= "Zip Hoodie"
    ```

    and
    ```
    query_phrase= "Unisex Zip Hoodie"
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_simple_query.py
    ```

Adding one more word to the query phrase makes your request more accurate. You can expect fewer products in the response, and the most relevant products will appear on the top of the response list.

## Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

In this tutorial, you will get an error message when trying to request the Search Service without setting the `visitorId`, which is a required field.

1. To check it, comment out a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_simple_query.py" regex="123456">line</walkthrough-editor-select-regex> `search_request.visitor_id = "123456"`:

1. Run the following command in Terminal:
    ```bash
    python search/search_simple_query.py
    ```

1. You should see the following error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Field "visitorId" is a required field, but no value is found.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the search by yourself and try different combinations of different search queries.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
