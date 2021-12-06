#  Importing products from the BigQuery table tutorial

## Get started

The Retail API offers you a convenient way to import your catalog data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive catalog data with no limits.

Moreover, you can specify the Retail schema that has more product attributes than other import options including
key/value custom attributes.

You can choose one of the reconciliation modes, `INCREMENTAL` or `FULL`, using the BigQuery table as an import source:
- Incremental import creates products that didn't exist in a catalog before importing and updates all current products.
- Full import deletes current products if they aren't present in the BigQuery source, adds new products and updates.
  current products that existed in the catalog before importing and in the BigQuery table.

To find more information about different import types, their restrictions, and use cases, check the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations).

<walkthrough-tutorial-duration duration="5"></walkthrough-tutorial-duration>

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

1. Go to the ```grs-samples-python``` directory. This is our starting point to run more commands.
    ```bash
    cd grs-samples-python
    ```

## Create the BigQuery table and upload products

Before you import products to your catalog, you need to upload the data to the BigQuery table first. There are two ways to do it:
- create [an empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition) using the Retail schema and products in this table using SQL.
- create a BigQuery table using the prepared JSON file with products. You can define the [Retail schema](https://cloud.google.com/retail/docs/catalog#expandable-1) or use an autodetect option.

To upload the data to the BigQuery table you need to create a dataset first, then create table with specific Retail data schema.
Next, upload data to the table from prepared JSON file. The data in the file should correspond the Retail schema as well.

There is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/resources/products.json" regex="id">`product/resources/products.json`</walkthrough-editor-select-regex> file with valid products. It should be uploaded to the `products` dataset and `products` table.

Also, there is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/resources/products_some_invalid.json" regex="id">`product/resources/products_some_invalid.json`</walkthrough-editor-select-regex> file containing some invalid products along with valid ones. It should be uploaded to the `products` dataset and `products_some_invalid` table. This table will be used to demonstrate the error handling.

1. Run the following code in the Terminal to create tables and import data:
    ```bash
    python product/setup/create_bigquery_table.py
    ```
1. The dataset `products` with both tables are created, check them in [Cloud Console](https://console.cloud.google.com/bigquery).

**Note**: In case if you don't have permissions to run the ```bq``` command and you got `Permission denied` error, you can create the table and upload your data from UI admin console.


## Create the BigQuery table and upload products from UI admin console

In case if you do not have permissions to run the ```bq``` command, you can create the table and upload your data from UI admin console.

### Upload catalog data to Cloud Storage

There is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/resources/products.json" regex="id">product/resources/products.json</walkthrough-editor-select-regex> file with valid products prepared in the `product` directory.

The other file, <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/resources/products_some_invalid.json" regex="id">product/resources/products_some_invalid.json</walkthrough-editor-select-regex>, contains both valid and invalid products. You will use it to check the error handling.

In your own project create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique, for convenience it can be named as `<YOUR_PROJUCT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file run the following command in the Terminal:
    ```bash
    python product/setup/create_gcs_bucket.py
    ```
    The bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the file is uploaded.

1. Save the name of the created Cloud Storage bucket printed in the Terminal for the next steps.

### Create the BigQuery table and upload products

1. Go to the [BigQuery in Cloud Console](https://console.cloud.google.com/bigquery).

1. In the Explorer panel you see the list of your projects.

1. Click the View actions button next to the current project name and chose **Create Dataset** option.

1. Set the Dataset ID and click **Create Dataset**.

1. Expand node of your current project

1. Click View actions button next to your new dataset and choose **Create table**.

1. Set the Source: in the field **Create table from** choose **Google Cloud Storage** option.

1. Click **Browse** in the **Select file from GCS bucket** and choose the bucket you have created on the previous step.

1. Choose the **`products.json`** and click **Select**.

1. Set the **Destination** field **Table** with a value ```products```.

1. Provide a table **Schema**: activate toggle **Edit as a text** and paste in the field the schema which you can find in the **`product/resources/product_schema.json`** file.

1. Click **Create table**.

As a result the BigQuery table is created. You can proceed and import products to the catalog.


## Import products from the BigQuery table

1. Open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_big_query_table.py" regex="# get import products from big query request">`product/import_products_big_query_table.py`</walkthrough-editor-select-regex> file and look at the example of the import product request.

    The field `parent` contains a catalog name along with a branch number where you are going to import your
    products to.

    The field `input_config` defines the `BigQuerySource` as an import source.

1. To import products, open the Terminal and run the following command:
    ```bash
    python product/import_products_big_query_table.py
    ```

## Response analysis

Once you have called the import products method, the import operation has started.

Importing may take some time depending on the size of your BigQuery table.

The operation is completed when the field `operation.done()` is set to true.

1. Check the result, one of the following fields should be present:
    - `error`, if the operation failed.
    - `result`, if the operation was successful.

1. Check the `big_query_operation.metadata.success_count` field to get the total number of the successfully imported products. Their expected number is 316.

    The number of failures during the product import is returned in `big_query_operation.metadata.failure_count` field. Their expected number is 0.

    The operation is successful, and the operation object contains a `result` field.

1. Check it printed out in th Terminal:
    ```
    errors_config {
      gcs_prefix: "gs://945579214386_us_import_product/errors7399332380794639317"
    }
    ```

## Errors appeared during product importing

Try to import a couple of invalid product objects and check the error message in the operation response.

The title field is required, so if you remove it, you get the invalid product object.
Another example of an invalid product is a product with an incorrect value of the `product.availability` field.
There is a `products_for_import_invalid` table in the BigQuery dataset that contains such invalid products.

Use it for importing to get an error message.

1. Go to the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_big_query_table.py" regex="# TO CHECK ERROR HANDLING USE THE TABLE WITH INVALID PRODUCTS:">`product/import_products_big_query_table.py`</walkthrough-editor-select-regex> file and assign the `table_id` value to the table with invalid products:
    ```
    table_id = "products_for_import_invalid"
    ```
1. Run the code sample and wait till the operation is completed:
    ```bash
    python product/import_products_big_query_table.py
    ```

Next, check the operation printed out to the Terminal.

## Errors appeared during the importing: output analysis

If the operation is completed successfully, you can find `result`field. Otherwise, there would be an `error` field instead.

The operation is considered as successful, and the `big_query_operation.metadata.success_count` field contains the number of the successfully imported products, which is `2`.

There are `2` invalid products in the BigQuery table, and the number of failures during the product import in the `big_query_operation.metadata.failure_count` field is `1`.

The `operation.result` field points to the errors bucket where you can find a json file with all the importing errors.

The error is the following:
```json
{"code":3,"message":"Invalid value at 'availability' (type.googleapis.com/google.cloud.retail.v2main.Product.Availability): \"INVALID_VALUE\"","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":1}}]}
```

## Errors appeared due to invalid request

Send invalid import request to make the operation fail.

1. In the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_big_query_table.py" regex="# TO CHECK ERROR HANDLING USE THE TABLE WITH INVALID PRODUCTS:">`product/import_products_big_query_table.py`</walkthrough-editor-select-regex> file, open the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_big_query_table.py" regex="get_import_products_big_query_request">`get_import_products_big_query_request()`</walkthrough-editor-select-regex> method, and add there a local variable `default_catalog` with an invalid catalog name.

1. Tun the code again and check the error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to prepare data and to test the importing products from BigQuery table by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
