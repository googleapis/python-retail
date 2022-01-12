# Filter tutorial

## Get started

Filtering in the Retail service is a powerful and convenient search feature.
It lets you fine-tune search requests according to your or your customer's needs.
You can:

- Filter by single or multiple fields.
- Filter by text or numeric fields, or both.
- Use an expression language to construct a predicate for each field.
- Combine different expressions using logical operators.

In this tutorial you will learn some examples of product filtering.

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

In your own project, create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it `<YOUR_PROJECT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file, run the following command in the Terminal:

    ```bash
    python product/setup/product_create_gcs_bucket.py
    ```

    Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the files are uploaded.

1. The name of the created Cloud Storage bucket is printed in the Terminal. Copy the name and set it as the environment variable BUCKET_NAME:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail Catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Filter by text field: filtering expression

You can write a simple expression that applies to the text field and looks like this:

```(textual_field,":", "ANY", "(",literal,{",",literal},")"```

Function `ANY` returns true if the field contains any literals.

An example of such an expression is
```'(colorFamilies: ANY("Black"))'```

1. To see the whole request with the filtering applied, open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">search_with_filtering.py</walkthrough-editor-select-regex>.

1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

1. Note that the results contain only items that satisfy the filtering expression.

## Filter by text field: Use case

Now you can try filtering by a text field yourself in the Cloud Shell environment.

1. To do that, replace the condition under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> with one of the following samples:
    ```
    filter = '(brands: ANY("YouTube"))'
    ```

    or
    ```
    filter = '(colorFamilies: ANY("White","Gray"))'
    ```
1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

For a complete list of the text fields you can apply filters to, see the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter).

## Filter by a numeric field: IN range

To filter by a numeric field, you can write the filtering expression in two ways:
- To check whether the field value is within a range, use the function `IN`.
- To compare a field value with a double value, use operators `<=`,  `<`,  `>=`, `>` and `=`.

1. To use the function `IN` to search for products with a price between $15 and $45, change the filter expression under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> to the following:


    ```
    filter = 'price: IN(15.0, 45.0)'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

1. Check the search response. Now it contains only items with prices in the range of $15 to $45.

To see the complete list of the numeric fields you can apply filters to, see the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter).

## Filter by a numeric field: comparison operators

All comparison operators (`<=`,  `<`,  `>=`, `>` and `=`) are available for filtering expressions.

1. Change the filter expression under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> to the following:
    ```
    filter = 'price >= 15.0 AND price < 45.0'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

1. Check the search response. Now it contains only items with prices in the range between $15 and $45.

## Filter by multiple fields

To filter the search results by multiple fields, you can combine the expressions with `AND` or `OR` operators:

```filter = expression { " AND " | " OR " } expression```

1. Change the filter expression under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> to the following:
    ```
    filter = '(categories: ANY("Apparel")) AND (price: IN(30.0, *))'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

1. Check the search response. Now it contains only items from the `Apparel` category with prices more than $30.

## Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.

To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

To check a list of text and numeric fields that support filtering, use the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

If you try to filter the search results by a field that is not intended for filtering, for example, the `name` field, you will get an error message.

1. Change the variable `filter` value under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> to the following:

    ```
    filter = '(name: ANY("some_random"))'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_with_filtering.py
    ```

1. You should see the following error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(name: ANY("some_random"))'. Parsing filter failed with error: Unsupported field "name" on ":" operator.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the filtering by yourself and try different combinations of various filter expressions.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
