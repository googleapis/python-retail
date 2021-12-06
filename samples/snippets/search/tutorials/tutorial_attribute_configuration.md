# Attribute Configuration tutorial

## Get started

Retail Search allows you to configure the product attributes for the search purpose.

If you want the Retail Search to be able to filter and facet your catalog using a product attribute, you should set it as indexable.

If you want to enable the search by some product attribute, you should make this attribute searchable. Note, that only text attributes can be searchable.

In this tutorial you will learn how to configure the product attributes to make them searchable and indexable for the Retail Search service.

<walkthrough-tutorial-duration duration="7"></walkthrough-tutorial-duration>

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
The bucket name must be unique. For convenience, you can name it `<YOUR_PROJECT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file, run the following command in the Terminal:

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

## Filter by unindexable field

There are several products in the catalog with the attribute "eco-friendly".  The attribute field `indexable` is set to `false`.

```json
 "ecofriendly":{
      "indexable":"false",
      "searchable":"false",
      "text":[
         "recycled fabrics",
         "recycled packaging",
         "plastic-free packaging",
         "ethically made"
      ]
   }
```

Try to search for a sweater and filter the search results by this field.

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_attribute_config.py" regex="attributes.ecofriendly">search_attribute_config.py</walkthrough-editor-select-regex> to review the request.

1. The filter is set to the following value:
    ```
    '(attributes.eco-friendly: ANY("recycled packaging"))'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_attribute_config.py
    ```
1. Check the search response printed out in the Terminal.

    The attribute was not indexed, so the filter was not applied to this field and the following error message is expected:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(attributes.ecofriendly: ANY("recycled packaging"))'. Parsing filter failed with error: Unsupported field "attributes.ecofriendly" on ":" operator..
    ```

## Make the product attribute indexable

1. To make the attribute indexable, set the `indexable` field to `true`.
    We will use the `update_product()` method in <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/update_attribute_configuration.py" regex="# update the product attribute">update_attribute_configuration.py</walkthrough-editor-select-regex>.

1. Run the following command in Terminal:
    ```bash
    python search/update_attribute_configuration.py
    ```
**Note**: as you have changed the catalog data, the Retail Search needs some time to index products.
The time depends on the catalog size, and it usually takes up to 5 minutes.

## Filter by indexable field

Now, as you have configured the product attribute `eco-friendly` as `indexable`, check how the Retail API recognizes it now.

1. Request the Search Service again using the same request with the filter:
    ```
    '(attributes.eco-friendly: ANY("recycled packaging"))'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_attribute_config.py
    ```

Once you run the search by indexable field, the filter applies to the search response. You can see the requested product in the results list.

## Search for non-searchable attribute value

Next, request the Retail Search using the `ethically made sweater` query. This is one of the values of the `eco-friendly` attribute, which is still non-searchable.

The search response should be empty because the Retail Search doesn't take this attribute into account while performing the search.

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_attribute_config.py" regex="attributes.ecofriendly">search_attribute_config.py</walkthrough-editor-select-regex> to review the request.

1. Change the value in the `search_request.query` field:
    ```
     search_request.query = "ethically made sweater"
    ```

1. Comment out the following line to avoid the narrowing search results down:
    ```
    search_request.filter = '(attributes.eco-friendly: ANY("recycled packaging"))'
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_attribute_config.py
    ```

1. Check the results: it should be empty.

## Make the attribute searchable

1. Open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/update_attribute_configuration.py" regex="# update the product attribute">update_attribute_configuration.py</walkthrough-editor-select-regex> and change the value of  `attribute.searchable` to `true`:
    ```
     attribute.searchable = "true"
    ```

1. Run the following command in Terminal to update the product:
    ```bash
    python search/update_attribute_configuration.py
    ```

The changes will take an effect after the Retail Search will index them, it might take approximately 5 minutes.

## Search for searchable attribute value

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_attribute_config.py" regex="attributes.ecofriendly">search_attribute_config.py</walkthrough-editor-select-regex>.

1. Check that the value in the `search_request.query` field is the following:
    ```
     search_request.query = "ethically made sweater"
    ```

1. Run the following command in Terminal:
    ```bash
    python search/search_attribute_config.py
    ```

This time the service should return the matched product.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the attribute configurations by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>

