# Pagination tutorial

## Get started

Using pagination, you can view and navigate the search results effortlessly. Moreover, it decreases both the lookup time and the size of responses.

This tutorial shows you how to control pagination in your search request.

There are three fields in the search request that give you all the possibilities of navigating through the search results:
- **```page_size```**
- **```next_page_token```**
- **```offset```**

This tutorial describes how each of them works.

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

1. The name of the created GRS bucket is printed in the Terminal. Copy the name and set it as the environment variable `BUCKET_NAME`:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail Catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Page size

The ```page_size``` request field lets you limit the number of items in the search response.

1. To view the request with ```page_size```, open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_pagination.py" regex="TRY DIFFERENT PAGINATION PARAMETERS HERE">search_with_pagination.py</walkthrough-editor-select-regex>.

1. Run the sample in a terminal using the command:

    ```bash
    python search/search_with_pagination.py
    ```

As you can see now, the results contain the exact number of products you have set as the page size.

The **```total_size```** is not equal to the page size; it's the number of items matching the search query, and it doesn't change as you adjust the number of products per page.

## Next page token

After you have received a response in the previous step, you can request the next page.

You need to receive the ```next_page_token```, set it to a request field ```page_token```, and call the Search service again.

1. Find the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_pagination.py" regex="PASTE CALL WITH NEXT PAGE TOKEN HERE">comment</walkthrough-editor-select-regex> and paste this piece of code:

    ```
        next_page_token = search_response_first_page.next_page_token
        search_request_next_page = get_search_request("Hoodie", page_size, offset, next_page_token)
        search_response_next_page = get_search_service_client().search(search_request_next_page)

        print("---next page search results---")
        print(search_response_next_page)
    ```

1. Run the code sample again:
    ```bash
    python search/search_with_pagination.py
    ```

You can see the next page of <page_size> products in the response.

The field **```next_page_token```** has a value that forwards you to the next page. You can use this field in further results navigation.

## Offset

In other cases, instead of navigating from page to page or getting results with top relevance, you can directly jump to a particular position using the offset.

You have requested the second page with 6 products per page using ```next_page_token``` in the previous step .

1. To reproduce the same effect using <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_pagination.py" regex="offset = \d">offset</walkthrough-editor-select-regex>, configure the field ```page_size``` with the same value, which is 6.
1. Perform a small calculation to get the offset value:

    `offset = 6 * (2 - 1) = 6`

    where 6 is a page size, and 2 is the page number of the page you would like to switch to.

## Offset use case

1. Find the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_pagination.py" regex="PASTE CALL WITH OFFSET HERE">comment</walkthrough-editor-select-regex> and paste this piece of code:
    ```
        offset = 6
        search_request_second_page = get_search_request("Hoodie", page_size, offset, page_token)
        search_response_second_page = get_search_service_client().search(search_request_second_page)

        print("---second page search results---")
        print(search_response_second_page)
    ```

1. Run the code sample again:
    ```bash
    python search/search_with_pagination.py
    ```

1. Take a look at both `next page search results` and `second page search results`. You can compare the lists of received products using both the `next_page_token` and `offset`, which should be equal.

Now you know how the offset works. Perform the calculation one more time to make it clear.

1. If you want to jump to the seventh page with a page size of 12, the offset value you need to set should be calculated this way:

    `offset = 12 * (7 - 1) = 72`

## Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

If you try to request the Search Service with a negative page size, you get an error message.

1. Change the value of the variable ```page_size``` to any negative value and run the code one more time.
    ```bash
    python search/search_with_pagination.py
    ```

1. You should see the following error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 `page_size` must be nonnegative, but is set to -6.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the pagination by yourself right here in the Cloud Shell environment using different combinations of values for pagination parameters.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
